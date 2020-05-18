import boto3
import json
import datetime
from botocore.exceptions import ClientError

ses_client = boto3.client('ses')
CHARSET = "UTF-8"

def sendEmail(email_body):
    try:
        response = ses_client.send_email(
            Destination={
                'ToAddresses': [
                    "you@example.com",
                    "you@example.com"
                ],
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': CHARSET,
                        'Data': email_body,
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': "Amazon EC2 instance uptime",
                },
            },
            Source="from@example.com",
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
   
def lambda_handler(event, context):
    # Date, thirty days before runtime (Specified in timedelta() function)
    old_date = datetime.datetime.now() + datetime.timedelta(-30)
    date_format = old_date.strftime("%Y-%m-%d")
   
    ec2 = boto3.client('ec2',region_name='region-tobe-specified')
    # Print AMIs in from region owned by this account older than 30 days
    instances = ec2.describe_instances()
    response = ec2.describe_images(ExecutableUsers=['self'])
    for images in response["Images"]:
        if images["CreationDate"] < date_format:
            old_AMI = (images["ImageId"])
            # Print Instances launched by AMIs [older than 30 days]
            for reservation in instances["Reservations"]:
                for instance in reservation["Instances"]:
                    if ((instance["ImageId"]) == old_AMI):
                         tags = instance['Tags']
                         for i in tags:
                             key_name = i['Key']
                             if "Name" in key_name:
                                 instance_name = i['Value']
                                 print ("\t\tInstance ID: " + instance["InstanceId"] + "\t\tAMI ID:" +old_AMI + "\t\tIP:" + instance["PrivateIpAddress"] + "\t\tInstance Name:" + instance_name)
                                 email_body = "\t\tInstance ID: " + instance["InstanceId"] + "\t\tAMI ID:" +old_AMI + "\t\tIP:" + instance["PrivateIpAddress"] + "\t\tInstance Name:" + instance_name
                         
    # Send email function #
    sendEmail(email_body)
