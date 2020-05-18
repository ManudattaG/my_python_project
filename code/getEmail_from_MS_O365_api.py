import json
import ast
from botocore.vendored import requests
from botocore.vendored.requests import *

def lambda_handler(event, context):
    r = requests.post('https://login.microsoftonline.com/67bff79e-7f91-4433-a8e5-c9252d2ddc1d/oauth2/v2.0/token',
       data = {
        'grant_type': 'client_credentials',
        'scope': 'https://graph.microsoft.com/.default',
        'client_id': 'XXXXXX',
        'client_secret': 'XXXXX'
       }
    )
    resp = r.json()
    print(resp)
    
    access_token = resp["access_token"]
    
    email_list = []
    no_email_list = []
    
    user_list = ["user_id_1", "user_id_2", "user_id_3", "user_id_4", "user_id_5"]
    for user in user_list:
        r = requests.get("https://graph.microsoft.com/v1.0/users/?$filter=mailNickname eq '"+user+"'", headers={'Authorization': 'Bearer '+ access_token})
        get_res = r.json()
        print(get_res)
        if len(get_res['value']) > 0:
            email_field = get_res['value'][0]['mail']
            email_list.append(email_field)
            
        else:
            print("No email found")
            no_email_list.append(user)
            
    print(email_list)
    print(no_email_list)
    email_list = email_list.encode("utf-8")
    email_list = ast.literal_eval(email_list)
    print(email_list)
