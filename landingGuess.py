# This script trys to guess at a landing spot, idealy this will become obsolete for a more acurate method
import math
##message = {'software_name': 'radiosonde_auto_rx', 'software_version': '1.5.9', 'uploader_callsign': 'KD2EAT', 'uploader_position': '42.543179,-76.66659', 'uploader_antenna': 'Comet GP-3', 'time_received': '2023-02-02T13:07:13.160761Z', 'datetime': '2023-02-02T13:07:29.000000Z', 'manufacturer': 'Vaisala', 'type': 'RS41', 'serial': 'U3825066', 'subtype': 'RS41-NG', 'frame': 8643, 'lat': 42.76031, 'lon': -76.1974, 'alt': 16996.11399, 'temp': -58.6, 'humidity': 1.5, 'vel_v': -7.41032, 'vel_h': 45.54725, 'heading': 84.83392, 'sats': 8, 'batt': 2.5, 'frequency': 403.801, 'burst_timer': 29562, 'snr': 23.7, 'tx_frequency': 403.8, 'user-agent': 'Amazon CloudFront', 'position': '42.76031,-76.1974', 'upload_time_delta': -1.104, 'uploader_alt': 294.0}
#Just a test msg^^
def glanding(message):
    alt = message["alt"]
    lat = message["lat"]
    lon = message["lon"]
    vel_v = message["vel_v"] 
    vel_h = message["vel_h"] 
    heading = message["heading"]
    time_left = alt / abs(vel_v)
    distance_left = time_left*vel_h
    print(time_left)
    if(heading<90):
        add_x = distance_left*math.sin(math.radians(heading))
        add_y = distance_left*math.cos(math.radians(heading))
    elif(heading<180):
        add_x = distance_left*math.cos(math.radians(heading))
        add_y = distance_left*math.sin(math.radians(heading))
    elif(heading<270):
        add_x = distance_left*math.sin(math.radians(heading))
        add_y = distance_left*math.cos(math.radians(heading))
    else:   
        add_x = distance_left*math.cos(math.radians(heading))
        add_y = distance_left*math.sin(math.radians(heading))
    lat = lat+((add_y/1000)/111)
    lon = lon+((add_x/1000)/111)
    ans = [lat,lon]
    return(ans)

#print(glanding(message))

