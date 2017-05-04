import boto3
from boto.exception import JSONResponseError
import uuid 

class starbucks_db(object):
	def __init__(self, mode='local', endpoint='http://127.0.0.1:9090', port=8000):
		self.db = None
		self.table = None
		self.endpoint = endpoint
		if mode == 'local':
			self.db = boto3.resource('dynamodb', endpoint_url = 'http://127.0.0.1:'+str(port), region_name='us-west-1')
		elif mode == 'server':
			self.db = boto3.resource('dynamodb', region_name='us-west-1')
		self.setupDB()
	
	def setupDB(self):
		
		try:
			self.table = self.db.create_table(
				TableName = 'starbucks',
				KeySchema = [
				{
					'AttributeName': 'id',
					'KeyType': 'HASH'
				}],
				AttributeDefinitions = [
				{
					'AttributeName': 'id',
					'AttributeType': 'S'
				}],
				ProvisionedThroughput = {
					'ReadCapacityUnits': 5,
					'WriteCapacityUnits': 5
					}
				)
			table.meta.client.get_waiter('table_exists').wait(TableName='starbucks')
		except Exception as in_use:
			try:
				self.table = self.db.Table('starbucks')
			except Exception as e:
				print("Starbucks Table doesn't exist.")
	
	def addOrder(self, order, order_id=None):
		if order_id == None:
			order_id = str(uuid.uuid4())

		item = {
			'id':order_id,
			'location': order["location"],
			'items': order["items"],
			'links':
			{'payment': self.endpoint + '/SF/starbucks/order/' + order_id + '/pay',
			'order': self.endpoint + '/SF/starbucks/order/' + order_id
			},
			'status':'PLACED',
			'message':'Order has been placed.'}

		self.table.put_item(
			Item=item)
		return item
	
	def findAllOrders(self):
		response = self.table.scan()
		items = response['Items']
		return items

	def isOrderExist(self, order_id):
		response = self.table.get_item(Key={'id':order_id})
		item = response.get('Item')
		return item != None

	def findOrder(self, order_id):
		response = self.table.get_item(Key={'id':order_id})
		item = response.get('Item')
		return item

	def deleteOrder(self, order_id):
		self.table.delete_item(Key={'id':order_id})

	def updateOrder(self, new_order, order_id):
		self.deleteOrder(order_id)
		item = self.addOrder(new_order, order_id)
		return item

	def payOrder(self, order_id):
		self.table.update_item(
			Key={'id':order_id},
			UpdateExpression='SET #status = :str1',
			ExpressionAttributeValues={':str1': 'PAID'},
			ExpressionAttributeNames={'#status': 'status'})

	def isPaid(self, order_id):
		response = self.table.get_item(Key={'id':order_id})
		item = response.get('Item')
		return item.get('status') == 'PAID'