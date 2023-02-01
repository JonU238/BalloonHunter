import googlemaps
from datetime import datetime
import json
f = open('pass.json')
important = json.load(f)
gmaps = googlemaps.Client(key=important["googleKey"])
# Request directions via public transit
print("Maper online")
def time_to_destination(loc1, loc2):
    now = datetime.now()
    directions_result = gmaps.directions(loc1,loc2,
                                        mode="driving",
                                        departure_time=now)
    return(directions_result[0]["legs"][0]["duration_in_traffic"]["text"])
#print(time_to_destination("Rochester Institute of Technology","1389 Spang St extention Roaring spring PA"))