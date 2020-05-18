"""
The python code will send a release notification of the new feature of an application to the slack users.
Whereby the below code sends a notification to the users whenever a new feature is about to release in the bot.
The bot is integrated with Slack app.

AWS Services used:
1. AWS Lambda function
2. SQS
3. DynamoDB
4. System manager parameter store

Slack API used:
1. users.lookupByEmail
2. im.list
3. chat.postMessage

"""

import requests
import boto3
from datetime import timedelta , datetime
import os
import json
import uuid
import time
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr

sqs = boto3.resource('sqs', region_name='us-east-1')
event_name = "LexKibana"
logtime = datetime.utcnow()
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
param_client = boto3.client('ssm')
lambda_name = "notification_slack_test"
event_type = "Lambda intent response to bot"

def callSlackNotificationUsersTable(department):
  if(department != None and department != ""):
    try:
      print("Calling Slack Notification Users table")
      table = dynamodb.Table('Slack_Notification_Users')
      response = table.scan(
        FilterExpression = Attr("Department").eq(department)
      )
      print(response)
    
    except ClientError as e:
        SQSmessagebodytokibana = '{{ "Event":"{}", "timestamp":"{}", "eventsource":"{}", "exception":"{}" }}'.format(event_name,logtime,"Error while getting data from Slack_Notification_Users table",str(e))
        print(SQSmessagebodytokibana)
        
    else:
        items = response['Items']
        print len(response['Items'])
        print(response['Items'])
        print(type(items))
        return(items)
        
  else:
    print("Department not specified in the payload to send the notification")
    return(None)
          
      
        
def getUserInfoByEmail(email, bot_token):
    url = "https://slack.com/api/users.lookupByEmail"
    querystring = {"token": bot_token,"email": email}
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_res = json.loads(response.text)
    print("Printing slack users.lookupByEmail api response...")
    print(json_res)
    if(json_res["ok"] == True and "user" in json_res):
      userObj = json_res.get('user', None)
      userId = userObj.get('id', None)
      profile_body = userObj.get('profile', None)
      first_name = profile_body.get('first_name', None)
      print(userId)
      print(first_name)
      return(userId, first_name)
    else:
      return(None, None)
    
def callSubFunction2(userId, bot_token, next_cursor, page, slack_imlist_api):
  try:
    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }
    querystring = {"token":bot_token, "cursor":next_cursor, "limit":300}
    response = requests.request("GET", slack_imlist_api, headers=headers, params=querystring)
    print(response.text)
    json_body = json.loads(response.text)
    if(json_body["ok"] == True):
      response = callSubFunction1(userId, bot_token, json_body, page, slack_imlist_api)
      return(response)
          
  except Exception as e:
    print(e)
    
def callSubFunction1(userId, bot_token, json_body, page, slack_imlist_api):
  ok_status = json_body.get('ok', None)
  ims = json_body.get('ims', None)
  response_metadata = json_body.get('response_metadata', None)
  next_cursor = response_metadata.get('next_cursor', None)
  if(ims and ok_status == True):
    if(page <= 2):
      print("Searching user in page : " + str(page))
      for id in ims:
        if "user" in id:
          im_user = id['user']
          im_id = id['id']
          if userId in im_user:
            return(im_id)
          
      else:
        page = page + 1
        response = callSubFunction2(userId, bot_token, next_cursor, page, slack_imlist_api)
        return(response)

def callChannelList(userId, slack_imlist_api, bot_token):
  ##url = "https://slack.com/api/im.list"
  querystring = {"token":bot_token, "limit":300}
  headers = {
    'Content-Type': "application/x-www-form-urlencoded"
  }
  page = 1
  try:
      response = requests.request("GET", slack_imlist_api, headers=headers, params=querystring)
      print(response.text)
      json_body = json.loads(response.text)
      if(json_body["ok"] == True):
        response = callSubFunction1(userId, bot_token, json_body, page, slack_imlist_api)
        print(response)
        return(response)
              
  except Exception as e:
      print(e)

def postMessageToSlackUser(im_id, post_text, slack_postMsg_api, attachments, bot_token):
  print("Sending feature update notification to the user...")
  querystring = {"token" : bot_token,"channel":im_id,"text":post_text,"attachments":json.dumps(attachments)}
  ##payload = "Content-Type=application%2Fx-www-form-urlencoded"
  headers = {
    'Content-Type': "application/x-www-form-urlencoded"
  }
  response = requests.request("POST", slack_postMsg_api, headers=headers, params=querystring)
  print(response.text)

def lambda_handler(event, context):
  for record in event['Records']:
    body = record['body']
    body = json.loads(body)
    print(body)
    
    bot_token = "xxxxxx"
    slack_imlist_api = "https://slack.com/api/im.list"
    slack_postMsg_api = "https://slack.com/api/chat.postMessage"

    feature_title = body.get("feature_title", None)
    feature_wiki_link = body.get("feature_wiki_link", None)
    feature_title_link_text = body.get("feature_title_link_text", None)
    department = body.get("feature_update_department", None)
    feature_comingsoon_title = body.get("feature_comingsoon_title", None)
      
    attachments = [
        {
            "fallback": "Feature summary of the attachment.",
            "color": "#2eb886",
            "pretext": "*_:sparkles: " + str(feature_title) + " :sparkles:_*",
            "title": feature_title_link_text,
            "title_link": feature_wiki_link,
            "text": "For more details on this feature, please click on the above link",
            "fields": [
                {
                    "title": "For queries:",
                    "value": ":slack: #channel-name \n :email: xxxx@yyyy.com",
                    "short": False
                }
            ],
            "footer": "Powered By Slack App",
            "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
            "ts": int(time.time())
        }
    ]
    
    if(feature_comingsoon_title != "" and feature_comingsoon_title != None):
      feature_comingsoon_json = {
        "fallback": "Feature summary of the attachment.",
        "pretext": "*_:sparkles: Coming Soon :: " + str(feature_comingsoon_title) + " :sparkles:_*"
      }
      attachments.append(feature_comingsoon_json)
    
    email_list = callSlackNotificationUsersTable(department)
      
    if(email_list != None):
      count = 0
      for i in email_list:
        email = i['email']
        user_info = getUserInfoByEmail(email, bot_token)
        userId = user_info[0]
        first_name = user_info[1]
        
        if(userId != None and first_name != None):
            
          ## call im.list to get all the slack channel list ##
          im_id = callChannelList(userId, slack_imlist_api, bot_token)
          
          post_text = "Hello " + str(first_name) + ", \n\n *:rocket: What's new in Bot :rocket:*"
            
          ## call post.message to send msg to particular user ##
          postMessageToSlackUser(im_id, post_text, slack_postMsg_api, attachments, bot_token)
          
          if(count != 0 and count % 20 == 0):
            print("Printing limit value")
            print(count)
            time.sleep(30)
            
          count += 1
          print("Printing count value")
          print(count)
        
      return "Success"
      
    else:
      print("No emails to send notification")
      return "Success"
