#ISS Tracker by Matt Hendricks
#Started 4/15/2021

#Updated 4/18/2021
#Added GPS data retrieved via IP address. Code should now work and return a distance based on the systme it's run.


#Load needed modules
import json, urllib.request, datetime
from math import sin,cos,sqrt,atan2,radians

#Establish required variables to store
isslat=[] #Latitude position point
isslon=[] #Longitude position point
issaltitude=[] #altitude (km)
issspeed=[] #Current speed (km/h)
time=[] #Timestamp from source
isscountry=[] #Country the ISS is currently over
devicelat=[] #Latitude of the device
devicelon=[] #Longitude of the device
countrytable=[] #Dictionary of country codes and names

#Main program

#Pull ISS data from web source
#Source is: https://wheretheiss.at/w/developer
with urllib.request.urlopen("https://api.wheretheiss.at/v1/satellites/25544") as url:
    data = json.loads(url.read().decode())

#Extract needed data from source
isslat=data['latitude']
isslon=data['longitude']
issaltitude=data['altitude']
issspeed=data['velocity']
time=data['timestamp']


#Convert the timestamp into a readable time format
realtime = datetime.datetime.fromtimestamp(time)

#Send ISS location to API and get the country code data back
issurl = "https://api.wheretheiss.at/v1/coordinates/"+str(isslat)+","+str(isslon)

with urllib.request.urlopen(issurl) as url:
    issground = json.loads(url.read().decode())

isscountry = issground['country_code']

#Change to full country name and handle ocean position
if isscountry == "??":
    isscountry = "None"
else:
    with urllib.request.urlopen("http://country.io/names.json") as url:
        countrytable = json.loads(url.read().decode())
    isscountry = countrytable[issground['country_code']]


#Get device location based on IP Address
with urllib.request.urlopen("http://ipinfo.io/json") as url:
    data2 = json.loads(url.read().decode())

ipgps = data2['loc']
ipgps = ipgps.split(",")

devicelat = float(ipgps[0])
devicelon = float(ipgps[1])


#Calculate distance from device to ISS
R = 6373.0

lat1 = radians(isslat)
lon1 = radians(isslon)
lat2 = radians(devicelat)
lon2 = radians(devicelon)

dlon = lon2 - lon1
dlat = lat2 - lat1
a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
distance = R * c


#Print updated variables
print("")
print("Current ISS Position and Velocity Data:")
print("")
print("Latitude:",round(isslat,2))
print("Longitude:",round(isslon,2))
print("Altitude:",round(issaltitude,2),"km")
print("Velocity:",round(issspeed,2),"km/h")
print("Timestamp:",realtime)
print("Currently over:",isscountry)
print("")
print("Device Data:")
print("")
print("Latitude:",devicelat)
print("Longitude:",devicelon)
print("ISS Distance from device:",round(distance,2),"km")
print("")
