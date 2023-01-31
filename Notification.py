from twilio.rest import Client
import twilio
from requests.api import request
import json
import requests
from requests.models import Response
f = open('pass.json')
important = json.load(f)

def text_me(msg):
    client = Client(important["account_sid"], important["auth_token"])
    message = client.messages.create(body =  msg, #Message you send
                        from_ = important["from#"],#Provided phone number
                        to =    important["to#"])#Your phone number
    print(message.sid)

def weather(num):
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=42.291961&lon=-71.329079&exclude=hourly,daily&appid=1ff170bc342cf4ce6ca274567226d2ec"
    response = requests.request("GET",url)
    if num==1:
        return str(response.json()["current"])
    elif num==2:
        return "Temp: " + str(round((response.json()["current"]["temp"]-273.15)*(9/5)+32,2)) +"\n"+"Wind speed: "+ str(response.json()["current"]["wind_speed"]) +"\n"+"Wind Gust: "+ str(response.json()["current"]["wind_gust"])

