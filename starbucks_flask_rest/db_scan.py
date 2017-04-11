import boto3
import simplejson as json

db = boto3.resource('dynamodb', endpoint_url = "http://localhost:8000")

table = db.Table('starbucks')

response = table.scan()

items = response['Items']

print json.dumps(items, indent = 4)

response = table.get_item(Key={'id':'1'})

item = response.get('Item')
