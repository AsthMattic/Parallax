#ISS Tracker by Matt Hendricks
#Started 4/15/2021

#Updated 4/8/2022
#Restarting this file to use OOP approach, see Paralax_Old for the work history.


#Load needed modules
import datetime
from Stations import Station

#Create Station object that represents the tracker
Tracker = Station("Tracker",0,0,0.0,0.0,0.0,0,0,0)
Tracker.hello()
Tracker.ip_location()

#Create Station object for the ISS
ISS = Station("ISS",1,25544,0.0,0.0,0.0,0,0,0)
ISS.hello()
ISS.location_update()

Tracker.where()

ISS.where()

Tracker.target = ISS

Tracker.distance_calculate()

Tracker.distance_report()