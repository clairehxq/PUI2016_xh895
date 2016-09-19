'''
    file name: show_bus_locations_xh895
    author: Xueqi Huang
    Date create: 09/18/2016
    Date last modified: 15:12 09/18/2016
    python: 2.7
'''


import pandas as pd
import urllib2
import json
import sys


def main():
    key = sys.argv[1]
    BusName = sys.argv[2]
    data = fetchdata(key, BusName)
    result(data, BusName)


def fetchdata(key,BusName):
    base = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
    link = base + key + '&VehicleMonitoringDetailLevel=calls&LineRef=' + BusName
    webpage = urllib2.urlopen(link)
    data = pd.read_json(webpage)
    location = pd.DataFrame(data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"])
    return location

def getLongitude(location,i):
    return location["MonitoredVehicleJourney"][i]["VehicleLocation"]["Longitude"]


def getLatitude(location,i):
    return location["MonitoredVehicleJourney"][i]["VehicleLocation"]["Latitude"]


def result(location,BusName):
    busnumber = len(location)
    print 'Bus Line: %s' %(BusName)
    print 'Number of Active Buses: %i' %(busnumber)
    for i in range(len(location)):
        Lon = getLongitude(location, i)
        Lat = getLatitude(location, i)
        print 'Bus %i is at latitude %s and longtitude %s' %(i , Lat, Lon)




main()

