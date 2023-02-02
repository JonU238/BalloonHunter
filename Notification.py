from twilio.rest import Client
import twilio
from requests.api import request
import json
import requests
from requests.models import Response
important = open('pass.json')
important = json.load(important)
print("Notification online")
def text_me(msg):
    client = Client(important["account_sid"], important["auth_token"])
    message = client.messages.create(body =  msg, #Message you send
                        from_ = important["from#"],#Provided phone number
                        to =    important["to#"])#Your phone number
    print("TXT msg sid" + message.sid)


