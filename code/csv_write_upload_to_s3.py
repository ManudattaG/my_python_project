# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:50:06 2019

@author: t_gm
"""

import json
import csv
import os
import boto3

s3_resource = boto3.resource('s3', region_name='us-west-2')
bucketname = "ec2-csv-files"
upload_path = "csv/ec2_data.csv"

def callS3Upload(file_path):
    try:
        response = s3_resource.meta.client.upload_file(file_path, bucketname, upload_path)
        print("File uploaded successfully")
        
    except Exception as e:
        print(e)

def lambda_handler(event, context):
    csv_data = ['Instance ID: i-0aea3c71f846a7f48', 'AMI ID:ami-070c5009ea5c39ab6',
                'Instance ID: i-0a2ee73f5834385fb', 'AMI ID:ami-070c5009ea5c39ab6',
                'Instance ID: i-01c3a37b41aa1343f', 'AMI ID:ami-070c5009ea5c39ab6']
    file_path = '/tmp/ec2_data.csv'
    with open(file_path, 'w') as csvFile:
        writer = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        writer.writerow(csv_data)
        csvFile.close()
        
    print(os.path.isfile(file_path))
    
    with open(file_path, 'r') as f:
        data = f.read()
        print(data)
        
    callS3Upload(file_path)
