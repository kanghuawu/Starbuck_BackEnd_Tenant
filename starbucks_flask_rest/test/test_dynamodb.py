import boto3


dynamodb = boto3.resource('dynamodb', region_name='us-west-1')

# Create the DynamoDB table.

try:
	table = dynamodb.create_table(
	    TableName='users',
	    KeySchema=[
	        {
	            'AttributeName': 'username',
	            'KeyType': 'HASH'
	        },
	        {
	            'AttributeName': 'last_name',
	            'KeyType': 'RANGE'
	        }
	    ],
	    AttributeDefinitions=[
	        {
	            'AttributeName': 'username',
	            'AttributeType': 'S'
	        },
	        {
	            'AttributeName': 'last_name',
	            'AttributeType': 'S'
	        },

	    ],
	    ProvisionedThroughput={
	        'ReadCapacityUnits': 5,
	        'WriteCapacityUnits': 5
	    }
	)
	# Wait until the table exists.
	table.meta.client.get_waiter('table_exists').wait(TableName='users')
except Exception as in_use:
	try:
		table = dynamodb.Table('users')
	except Exception as e:
		print("Starbucks Table doesn't exist.")
	

# Print out some data about the table.
print(table.item_count)

table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)


response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)

item = response['Item']

print(item)