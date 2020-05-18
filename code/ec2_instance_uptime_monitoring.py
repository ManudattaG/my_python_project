import json
import boto3
from botocore.exceptions import ClientError
import datetime

ses_client = boto3.client('ses')
ec2 = boto3.client('ec2')
CHARSET = "UTF-8"

def sendEmail(ec2_uptime):
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
                        'Data': ec2_uptime,
                    }
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': "Amazon EC2 instance uptime",
                },
            },
            Source=""you@example.com"",
    )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

def timeDiff(launch_time, current_time, InstanceId):
    running_time = current_time - launch_time
    running_time = running_time.seconds/60
    ec2_uptime = "Instance : " + str(InstanceId) + " is running for " + str(running_time) + " mins"
    print(ec2_uptime)
    return(ec2_uptime)

def lambda_handler(event, context):
    ## For getting ec2 instance uptime ##
    
    response = ec2.describe_instances()
    print(response)
    ##print(type(response))
    Reservations = response.get('Reservations', None)
    for i in Reservations:
        Instances = i['Instances']
        ##print(Instances)
        for j in Instances:
            InstanceId = j['InstanceId']
            print(InstanceId)
            LaunchTime = j['LaunchTime']
            print(LaunchTime)
            current_time = datetime.datetime.now(LaunchTime.tzinfo)
            print(current_time)
            ec2_uptime = timeDiff(LaunchTime, current_time, InstanceId)
            sendEmail(ec2_uptime)
    
    ## ec2 instances older than 30 days ##
    
    old_date = datetime.datetime.now() + datetime.timedelta(days=-30)
    print(old_date)
    
    instances = ec2.describe_instances()
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            LaunchTime = instance['LaunchTime']
            print(LaunchTime)
            LaunchTime = LaunchTime.replace(tzinfo=None)
            if(LaunchTime < old_date):
                print ("\t\tInstance ID: " + instance["InstanceId"])
                print ("\t\tCreation time: " + str(LaunchTime))
            else:
                print("No instances are older than 30 days")
            
