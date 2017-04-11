from flask import Flask, jsonify, make_response, request
import argparse

# reference aws TicTacToe sample app
parser = argparse.ArgumentParser(description='Run the starbucks REST API', prog='starbucks.py')
parser.add_argument('--mode', help='Whether to connect to a DynamoDB service endpoint, or to connect to DynamoDB Local. In local mode, no other configuration ' \
                    'is required. In service mode, AWS credentials and endpoint information must be provided either on the command-line or through the config file.',
                    choices=['local', 'service'], default='service')
parser.add_argument('--endpoint', help='An endpoint to connect to (the host name - without the http/https and without the port). ' \
                    'When using DynamoDB Local, defaults to localhost. If the USE_EC2_INSTANCE_METADATA environment variable is set, reads the instance ' \
                    'region using the EC2 instance metadata service, and contacts DynamoDB in that region.')
parser.add_argument('--port', help='The port of DynamoDB Local endpoint to connect to.  Defaults to 8000', type=int)
parser.add_argument('--serverPort', help='The port for this Flask web server to listen on.  Defaults to 5000 or whatever is in the config file. If the SERVER_PORT ' \
                    'environment variable is set, uses that instead.', type=int)
args = parser.parse_args()

app = Flask(__name__)

@app.route("/v3/starbucks/orders", methods=['GET'])
def orders():
	re = {}
	re['request'] = request.method
	if request.method == 'GET':
		return jsonify(re)

@app.route("/v3/starbucks/order/<order_id>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def order(order_id):
	re = {}
	re['request'] = request.method
	re['order_id'] = order_id
	if request.method == 'GET':
		return jsonify(re)
	elif request.method == 'POST':
		return jsonify(re)
	elif request.method == 'PUT':
		return jsonify(re)
	elif request.method == 'DELETE':
		return jsonify(re)
	else:
		abort(404)

@app.route("/v3/starbucks/order/<order_id>/pay", methods=['POST'])
def pay(order_id):
	re = {}
	re['request'] = request.method
	re['order_id'] = order_id
	if request.method == 'POST':
		return jsonify(re)


if __name__ == "__main__":
    app.run(debug = True)