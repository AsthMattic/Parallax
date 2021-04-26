#ISS Tracker by Matt Hendricks
#Started 4/15/2021

#Updated 4/25/2021
#Version is working with the N2YO API and velocity is being calculated with two GPS points.

#Load needed modules
import json, urllib.request, datetime
from math import sin,cos,sqrt,atan2,radians

#Establish required variables to store
apikey = "J6VXQY-TQMWLU-NPE9CY-4OGH"
satid = 25544 #NORAD ID of the satellite to be tracked, default is ISS
satname = "ISS" #Name of the Satellite being tracked
satlat=[] #Latitude position point
satlon=[] #Longitude position point
sataltitude=[] #altitude (km)
satvelocity=[] #Current speed (km/h)
time=[] #Timestamp from source
satcountry=[] #Country the ISS is currently over
devicelat=[] #Latitude of the device
devicelon=[] #Longitude of the device
countrytable=[] #Dictionary of country codes and names

#Main program

#satid = 48209 #input a different NORAD ID if desired

#Get device location based on IP Address
with urllib.request.urlopen("http://ipinfo.io/json") as url:
    data2 = json.loads(url.read().decode())

ipgps = data2['loc']
ipgps = ipgps.split(",")

devicelat = float(ipgps[0])
devicelon = float(ipgps[1])


#Pull ISS data from web source
#Source is: https://wheretheiss.at/w/developer

apiurl = "https://api.n2yo.com/rest/v1/satellite/positions/"+str(satid)+"/"+str(devicelat)+"/"+str(devicelon)+"/0/2&apiKey="+apikey
print(apiurl)
with urllib.request.urlopen(apiurl) as url:
    data = json.loads(url.read().decode())

#Extract needed data from source
satname=data['info']['satname']
satlat=data['positions'][0]['satlatitude']
satlon=data['positions'][0]['satlongitude']
#sataltitude=data['sataltitude']
time=data['positions'][0]['timestamp']

#Calculate velocity based on the two GPS points given
R = 6373.0

lat1 = radians(data['positions'][0]['satlatitude'])
lon1 = radians(data['positions'][0]['satlongitude'])
lat2 = radians(data['positions'][1]['satlatitude'])
lon2 = radians(data['positions'][1]['satlongitude'])

dlon = lon2 - lon1
dlat = lat2 - lat1
a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
satvelocity = R * c


#Convert the timestamp into a readable time format
realtime = datetime.datetime.fromtimestamp(time)

#Send ISS location to API and get the country code data back
issurl = "https://api.wheretheiss.at/v1/coordinates/"+str(satlat)+","+str(satlon)

with urllib.request.urlopen(issurl) as url:
    satground = json.loads(url.read().decode())

satcountry = satground['country_code']

#Change to full country name and handle ocean position
if satcountry == "??":
    satcountry = "None"
else:
    with urllib.request.urlopen("http://country.io/names.json") as url:
        countrytable = json.loads(url.read().decode())
    satcountry = countrytable[satground['country_code']]


#Calculate distance from device to ISS
R = 6373.0

lat1 = radians(satlat)
lon1 = radians(satlon)
lat2 = radians(devicelat)
lon2 = radians(devicelon)

dlon = lon2 - lon1
dlat = lat2 - lat1
a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
distance = R * c


#Print updated variables
print("")
print("Current "+satname+" Position and Velocity Data:")
print("")
print("Latitude:",round(satlat,4))
print("Longitude:",round(satlon,4))
#print("Altitude:",round(sataltitude,2),"km")
print("Velocity:",round((satvelocity*3600),2),"km/h")
print("Timestamp:",realtime)
print("Currently over:",satcountry)
print("")
print("Device Data:")
print("")
print("Latitude:",devicelat)
print("Longitude:",devicelon)
print("Distance from device to "+satname+": ",round(distance,2),"km")
print("")
