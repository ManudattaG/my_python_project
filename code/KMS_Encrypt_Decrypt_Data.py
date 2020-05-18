"""
This python code will encrypt sensitive data being stored into DynamoDB table and decrypts it whenever needed.

AWS Services used:
1. AWS Lambda functions
2. KMS (Key Management Service)
3. DynamoDB

Type of KMS encryption used : AWS managed key for DynamoDB
"""

import json
import boto3
import base64
from botocore.exceptions import ClientError

def decrypt(session, secret):
    client = session.client('kms')
    plaintext = client.decrypt(
        CiphertextBlob=bytes(base64.b64decode(secret))
    )
    return plaintext["Plaintext"]

def encrypt(session, secret, alias):
    client = session.client('kms')
    ciphertext = client.encrypt(
        KeyId=alias,
        Plaintext=bytes(secret),
    )
    return base64.b64encode(ciphertext["CiphertextBlob"])

def encrypt_data_handler(event, context):
    
    salary_data =  	{
			employees: [
			{
				"name": "John",
				"value": "12000"
			},
			{
				"name": "Mary",
				"value": "15000"
			},
			{
				"name": "Mark",
				"value": "10000"
			},
			{
				"name": "Roger",
				"value": "20000"
			},
			{
				"name": "Eric",
				"value": "18500"
			}
		]
	}
    
    key_alias = 'alias/alias_name'
    table_name = 'data_table'
    
    session = boto3.session.Session()
    table = boto3.resource('dynamodb').Table(table_name)
    
    print("calling encryption function")
    
    encrypted_data = encrypt(session, salary_data, key_alias)
    print('ENCRYPTED DATA: ' + encrypted_data)
    
    item = {
        'ID': "123",
        'company_name': "XYZ",
        'employee_salary': encrypted_data
    }
    
    print('Adding new item to table.')
    
    table.put_item(Item=item)
    
    print("Item Inserted")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Encryption completed')
    }
	
	
def decrypt_data_handler(event, context):
    session = boto3.session.Session()
    dynamodb = boto3.resource('dynamodb')
    
    table_name = 'data_table'
    table = boto3.resource('dynamodb').Table(table_name)
    
    entry = table.get_item(TableName=table_name, Key={'ID': "123", 'company_name': "XYZ"})
    print("printing entry from table")
    print(entry)
    
    if 'Item' in entry:
        encrypted_data = entry['Item']['employee_salary']
        decrypted_data = decrypt(session,encrypted_data)
        print('DECRYPTED DATA: ' + str(decrypted_data))
		
		return {
        'statusCode': 200,
        'body': json.dumps('Decryption completed')
    }
        
    else:
        print("Issue fetching entry from table")
        return {
        'statusCode': 200,
        'body': json.dumps('Issue while fetching data from DB')
    }
