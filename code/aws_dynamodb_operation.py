# Get an item from DB

import boto3
from botocore.exceptions import ClientError

def get_handler(event, context):
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	alertsTable = dynamodb.Table('Alerts')
	alarmName = event['alarmname']
	accountnumber = event['acctnumber']
	action = event['action']
	description = event['description']
	commonAlertsTable = dynamodb.Table('Common-Alerts')
	try:
		if accountnumber is not None or alarmName is not None:
			response = alertsTable.get_item(
		Key={
			'Alarm_Name': alarmName,
			'AWS_AccountID': accountnumber,
			'Action': action,
			'Description': description
		}
		)
		for Item in response:
           alertItems = response['Item']
		   print(alertItems)
	
		else:
			response = commonAlertsTable.get_item(
			Key={
				'Metrics': metrics,
				'AWS_AccountID': accountnumber,
				'Action': action,
			}
			)
			for Item in response:
				commonAlertItems = response['Item']
				print(commonAlertItems)
			
	except ClientError as e:
		message=(e.response['Error']['Message'])
		code=(e.response['ResponseMetadata']['HTTPStatusCode'])
		errorresponse="Error code"+":"+str(code)+" "+"Error Message"+":"+message
		print(errorresponse)
		return(errorresponse)

	
# Update an item

def update_handler(event, context)
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('Alerts')
	alarmName = event['alarmname']
	accountnumber = event['acctnumber']
	wikiLink = event['wikiLink']
	desc = event['description']
	namespace = event['Namespace']
	response = table.update_item(
    Key={
           'Alarm_Name': alarmName,
		       'Wiki_Link': wikiLink
		       'Description': desc
    },
	UpdateExpression="set alarmName = :a, wikiLink=:w, desc=:d",
    ExpressionAttributeValues={
        ':a': event['alarmname'],
        ':w': event['wikiLink'],
        ':d': event['description']
    },
    ReturnValues="UPDATED_NEW"
 )
print("Item updated")


# Insert an item

def insert_handler(event, context):
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('Alerts')
	try:
		if accountId is not None:
			response = table.get_item(
			Key={
				'Alarm_Name': alarmName,
				'AWS_AccountID': accountId
			}
		)
		if 'Item' not in response:
			response = table.put_item(
				Item={
					'Alarm_Name': alarmName,
					'AWS_AccountID': accountId,
					'Description': 'Test insert item',
					'Function': 'testFunc',
					'Invocation_count': 0,
					'Script_Location': 's3://(bucket-name).......',
					'Threshold': 2
				},
				ConditionExpression = "(attribute_not_exists(accountId))"
			)
			print("Item created with accountId : " + str(accountId))
		else:
			print("Item already exists in DB with accountId : " + str(accountId))
			
	except ClientError as e:
		message=(e.response['Error']['Message'])
		errorresponse="Insert item error, Error Message"+":"+message
		print(errorresponse)
		return(errorresponse)
		
		
# Delete an item

def delete_handler(event, context):
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	table = dynamodb.Table('Alerts')
	try:
		if accountId is not None:
			response = table.delete_item(
				Key={
					'Alarm_Name': alarmName,
					'AWS_AccountID': accountId
				}
			)
	except ClientError as e:
		message=(e.response['Error']['Message'])
		errorresponse="Delete error, Error Message"+":"+message
		print(errorresponse)
		return(errorresponse)
		
		
# Scan the table by adding filter condition expression

def scan_filter_handler(event, context):
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
	alertsTable = dynamodb.Table('Alerts')
	alarmName = "High memory usage alert"
	accountId = 12345678
	accountIdFilter = Attr('AWS_AccountID').eq(accountId)
	alarmNameFilter = Attr('Alarm_Name').contains(alarmName)
	try:
		if accountId is not None and alarmName is not None:
			alertResponse = alertsTable.scan(FilterExpression=accountIdFilter & alarmNameFilter)
			for item in alertResponse['Items']:
				print(item)
				
			
	except ClientError as e:
		message=(e.response['Error']['Message'])
		code=(e.response['ResponseMetadata']['HTTPStatusCode'])
		errorresponse="Error code"+":"+str(code)+" "+"Error Message"+":"+message
		print(errorresponse)
		return(errorresponse)
