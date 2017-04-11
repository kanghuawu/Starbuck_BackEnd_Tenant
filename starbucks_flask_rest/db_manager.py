import boto3



class starbucks_db

dynamodb = boto3.resource('dynamodb', endpoint_url = "http://localhost:8000")
table = dynamodb.Table('starbucks')