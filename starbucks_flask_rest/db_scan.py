import boto3
import simplejson as json
import argparse

parser = argparse.ArgumentParser(description='Scan or delete DB')
parser.add_argument('-d', help='Clean database', action='store_true')
parser.add_argument('--service', help='Connect to localhost use local or connect to aws use server', choices=['local', 'server'], default='local')
args = parser.parse_args()

if args.service == 'local':
	db = boto3.resource('dynamodb', endpoint_url = 'http://localhost:8000', region_name='us-west-1')
else: 
	db = boto3.resource('dynamodb', region_name='us-west-1')
table = db.Table('starbucks')

response = table.scan()

items = response['Items']

print json.dumps(items, indent = 4)

if(args.d):
	print 'Deleting....'
	for it in items:
		print json.dumps(it['id'], indent = 4)
		table.delete_item(Key={'id':it['id']})