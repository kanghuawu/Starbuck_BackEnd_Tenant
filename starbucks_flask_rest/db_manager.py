import boto3
from boto.dynamodb2.exceptions import ResourceInUseException

class starbucks_db:
	def __init__(self, mode='local', endpoint=None, port=None):
		self.db = None
		self.table = None

		if mode == 'local':
			self.db = boto3.resource('dynamodb', endpoint_url = "http://localhost:8000")
		elif mode == 'service':
			self.db = boto3.resource('dynamodb', endpoint_url=endpoint+":"+str(port))
		else:
			raise Exception("Invalid arguments, please refer to usage.")

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
				}
				# {
				# 	'AttributeName': 'location',
				# 	'AttributeType': 'S'
				# },
				# {
				# 	'AttributeName': 'items',
				# 	'AttributeType': 'L'
				# },
				# {
				# 	'AttributeName': 'links',
				# 	'AttributeType': 'M'
				# },
				# {
				# 	'AttributeName': 'status',
				# 	'AttributeType': 'S'
				# },
				# {
				# 	'AttributeName': 'message',
				# 	'AttributeType': 'S'
				# }
				],
				ProvisionedThroughput = {
					'ReadCapacityUnits': 5,
					'WriteCapacityUnits': 5
					}
				)
		
		except ResourceInUseException as in_use:
			try:
				self.table = self.db.Table('starbucks')
			except Exception as e:
				print("Games Table doesn't exist.")
	
	def addOrder(self, items):
		self.table.put_item(Item={'id':'123','location':'here','items':items,'links':{'link1':'a','link2':'b'},'message':'msg'})

	def getDB(self):
		return self.db
