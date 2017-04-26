from flask import Flask, jsonify, make_response, request
from db_manager import *
import argparse
import simplejson as json
# import json

# reference aws TicTacToe sample app
parser = argparse.ArgumentParser(description='Run the starbucks REST API', prog='starbucks.py')
parser.add_argument('--mode', help='Whether to connect to a DynamoDB service endpoint, or to connect to DynamoDB Local. In local mode, no other configuration ' \
                    'is required. In service mode, AWS credentials and endpoint information must be provided either on the command-line or through the config file.',
                    choices=['local', 'service'], default='local')
parser.add_argument('--endpoint', help='An endpoint to connect to (the host name - without the http/https and without the port). ' \
                    'When using DynamoDB Local, defaults to localhost. If the USE_EC2_INSTANCE_METADATA environment variable is set, reads the instance ' \
                    'region using the EC2 instance metadata service, and contacts DynamoDB in that region.')
parser.add_argument('--port', help='The port of DynamoDB Local endpoint to connect to.  Defaults to 8000', type=int)
parser.add_argument('--serverPort', help='The port for this Flask web server to listen on.  Defaults to 9090 or whatever is in the config file. If the SERVER_PORT ' \
                    'environment variable is set, uses that instead.', type=int, default=9090)
args = parser.parse_args()

db = starbucks_db(mode=args.mode, endpoint=args.endpoint, port=args.port)

NOT_JSON = {
	'status': 'error',
	'message': 'Must be JSON.'
}

ORDER_NOT_FOUND = {
	'status': 'error',
	'message': 'Order not found.'
}

PAID = {
	'status': 'PAID',
	'message': 'Payment succeeded.'
}

ORDER_ALREADY_PAID = {
	'status':'PAID',
	'message': 'Order Already Paid.'
}

DELETE_OK = {
	'status':'DELETED',
	'message': 'Successful Deletion.'
}

app = Flask(__name__)

@app.route("/v3/starbucks/order", methods=['POST'])
def initial_order():
	print 'Placing order...'
	print json.dumps(request.json, indent=2)
	if request.is_json:
		order = request.json
		# print type(order)
		rep = db.addOrder(order)
		return jsonify(rep)
	else:
		return jsonify(NOT_JSON)

@app.route("/v3/starbucks/orders", methods=['GET'])
def orders():
	return jsonify(db.findAllOrders())

@app.route("/v3/starbucks/order/<order_id>", methods=['GET', 'PUT', 'DELETE'])
def order(order_id):
	if not db.isOrderExist(order_id):
		return jsonify(ORDER_NOT_FOUND)
	elif db.isPaid(order_id) and request.method != 'GET':
		return jsonify(ORDER_ALREADY_PAID)

	if request.method == 'GET':
		return jsonify(db.findOrder(order_id))
	elif request.method == 'PUT':
		return jsonify(db.updateOrder(request.json, order_id))
	elif request.method == 'DELETE':
		db.deleteOrder(order_id)
		return jsonify(DELETE_OK)

@app.route("/v3/starbucks/order/<order_id>/pay", methods=['POST'])
def pay(order_id):
	if db.isPaid(order_id):
		return jsonify(ORDER_ALREADY_PAID)
	else:
		db.payOrder(order_id)
		return jsonify(PAID)


if __name__ == "__main__":
    app.run(debug = True, port=args.serverPort)