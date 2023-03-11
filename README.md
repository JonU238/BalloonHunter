# BalloonHunter
Tools to make finding them sondes easier
## Sonde alert:
Sonde alert is disigned to send you a text msg whenever there is a sonde within a given radius of your current location, is gives you details about its type, location, alt, and the ETA via car to get to it.
Required python packages:
- sondehub
- googlemaps
- twilio
- email
- smtp

## Goals:
- Have program not just exit after sending, have it wait for the next time a balloon may be over head.
- Have it send a photo of the sonde hub map along with the email/txtmsg
## Completed goals:
- ~~Have sonde alert msg you if the balloon will land in your area~~
- ~~Add other msg services that dont require payed twilio account~~
- ~~Have eta given be to the landing site instead of the balloons curent location~~
## Installation
TLDR: clone the repo and run the installer, then when your confused come back here and read the full instructions

Sonde alert can either email or text you notification. To use it simply run the sondeAlert.py script on a server and have it restart the script at 10 utc every day.(this will be phased out so its always running soon)

Program settings:
- Distance
    - The max distance from your home waypoint that you want to recive notifications for
- Notification alt
    - Is the alt at which it will notify you, in the future I hope this will not exist and it will just be based on the predicted landing zone.(there is a bug with this if you live close to one of the stations that launch the sondes... :O)    
- Message type
    - Rn you can choose email or text refferance the twilio section and the email section for more info
- Home lat and lon
    - Hopefully self explanatory


### Twilio section: 
Twilio will let you send texts from your computer to your phone: make an account and then create a number these will be needed if you want to use text message notifications. [Twilio sign up](https://www.twilio.com/try-twilio)

### Email section: 
Email is the recommended method of getting the notifications, it needs to be a gmail account as of right now. You will also need to get a google app password for it. [Google app password instructions.](https://support.google.com/accounts/answer/185833?hl=en) 

### Google maps: 
The google maps api allows the program to give you a time estamate for driving to the balloon landing cite. You need to get a google dev account to use this feature and put your api key into the installer. (or you can add it manualy to the 
pass.json file)

# Feel free to ask questions if you want to!
