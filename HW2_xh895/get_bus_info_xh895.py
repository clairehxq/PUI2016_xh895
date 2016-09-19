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
import numpy as np
import csv


def main():
    key = sys.argv[1]
    BusName = sys.argv[2]
    filename = sys.argv[3]
    data = fetchdata(key, BusName)
    value = result(data,BusName)
    value.to_csv(filename,index = False)




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

def stopname(location,i):
    stop = location["MonitoredVehicleJourney"][i]["OnwardCalls"]["OnwardCall"][0]["StopPointName"]
    if stop <> "":
        return stop
    else:
        return "N/A"

def DistancefromStop(location,i):
    Distances = location["MonitoredVehicleJourney"][i]["OnwardCalls"]["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
    if  Distances <> "":
        return Distances
    else:
        return "N/A"


def result(location,BusName):
    busnumber = len(location)
    array = {"Latitude":[],"Longitude":[],"Stop Name":[],"Stop Status":[]}
    for i in range(busnumber):
        array["Latitude"].append(getLatitude(location, i))
        array["Longitude"].append(getLongitude(location, i))
        array["Stop Name"].append(stopname(location, i))
        array["Stop Status"].append(DistancefromStop(location, i))
    result = pd.DataFrame(array, columns = ["Latitude","Longitude","Stop Name","Stop Status"])
    return result





main()

