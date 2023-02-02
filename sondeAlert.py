import sondehub
import math
import json
import Notification
import maper
import landingGuess
#import numpy as np

B=43.084259 #YOUR LAT
A=-77.674322 #YOUR LONG
print("Sonde Alert online")
print("Current location: "+str(B)+" ,"+str(A))
'''
def calc_angle(a,b,c,d):
    angle =  (((d-b)/(abs(d-b)))*(180*((math.acos((((math.sqrt((d-b)**2)+(c-a)**2))**2+(10**2)-(math.sqrt((d-b)**2+(c-a+10)**2))**2)/(20*((math.sqrt((d-b)**2)+(c-a)**2)))))/math.pi)))
    return angle
'''
def calc_distance(a,b,c,d):
    i = B-d
    j = A-c
    distance = math.sqrt(i**2+j**2)
    distance = distance*54.6
    return distance
def on_message(message):
    C = float((message["position"]).split(",")[1])
    D = float((message["position"]).split(",")[0])
    
    balloon_alt = message["alt"]
    dist = calc_distance(A,B,C,D)
    if(dist<100 and int(balloon_alt)<5000):
        print(message)
        balloon_frequ = ((message["frequency"]))
        balloon_type = ((message["type"]))
        print(round(dist))
        guess_landing = landingGuess.glanding(message)
        print(guess_landing)
        timeToBalloon = maper.time_to_destination(str(B)+","+str(A), str(guess_landing[0])+","+str(guess_landing[1]))
        Notification.text_me("There is a balloon("+balloon_type+") @ "+str(D)+","+str(C)+" At alt:"+str(balloon_alt)+". On:"+str(balloon_frequ)+"MHZ. ETA:"+str(timeToBalloon))
        exit()
        
    else:
        pass
test = sondehub.Stream(on_message=on_message)
while 1:
    pass