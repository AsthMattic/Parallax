#File to hold the Station objects, which will be used as trackable objects.

import json, urllib.request, datetime
from math import sin,cos,sqrt,atan2,radians

class Station:

    name = None
    type = None
    id = None
    lat = None
    lon = None
    alt = None
    speed = None
    target = None
    target_distance = None

    def __init__(self, name, type, id, lat, lon, alt, speed, target, target_distance):
        self.name = name
        self.type = type
        self.id = id
        self.lat = lat
        self.lon = lon
        self.alt = alt
        self.speed = speed
        self.target = target
        self.target_distance = target_distance

    def hello(self):
        print("Object "+self.name+" Created!")

    def where(self):
        print(self.name,"is located at",self.lat,self.lon)

    #Function to calculate the distance from this station to another station object
    def distance_calculate(self):
        R = 6373.0

        lat1 = radians(self.target.lat)
        lon1 = radians(self.target.lon)
        lat2 = radians(self.lat)
        lon2 = radians(self.lon)

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        self.target_distance = round(R * c,2)

    #Function to print the current distance from the tracker to the target object
    def distance_report(self):
        print("The",self.name,"is",self.target_distance,"km from the",self.target.name)

class Satellite(Station):
    #Function to get location data from web API for satellite objects
    def location_update(self):
        # Pull ISS data from web source
        # Source is: https://wheretheiss.at/w/developer
        with urllib.request.urlopen("https://api.wheretheiss.at/v1/satellites/"+str(self.id)) as url:
            location_data = json.loads(url.read().decode())

        # Extract needed data from source
        self.lat = location_data['latitude']
        self.lon = location_data['longitude']
        self.alt = location_data['altitude']
        self.speed = location_data['velocity']
        time = location_data['timestamp']

        # Shorten the lat and lon lengths
        self.lat = round(self.lat,2)
        self.lon = round(self.lon,2)

        # Convert the timestamp into a readable time format
        realtime = datetime.datetime.fromtimestamp(time)

class Base(Station):
    #Function to get location information for the tracker from a web API
    def location_update(self):
        with urllib.request.urlopen("http://ipinfo.io/json") as url:
            ipLocationData = json.loads(url.read().decode())

        ipgps = ipLocationData['loc']
        ipgps = ipgps.split(",")

        self.lat = float(ipgps[0])
        self.lon = float(ipgps[1])
