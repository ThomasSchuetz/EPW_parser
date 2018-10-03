#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Simple reader for *.epw files
# Input data for several thousand, worldwide locations can be downloaded here:
# apps1.eere.energy.gov/buildings/energyplus/weatherdata_about.cfm

def parse_location(values, results):
    """
    """
    val = values.split(",")
    results["location"] = val[1]
    results["latitude"] = float(val[6])
    results["longitude"] = float(val[7])
    results["time zone"] = float(val[8])
    results["elevation"] = float(val[9])


def parse_data(values, results):
    val = values.split(",")
    results["date"].append((float(val[0]),  # Year
                            float(val[1]),  # Month
                            float(val[2]),  # Day
                            float(val[3]),  # Hour
                            float(val[4]))) # Minute
    
    results["temperature"].append(float(val[6])) # Dry bulb temperature in °C

    results["relative humidity"].append(float(val[8])) # In %
    
    results["pressure"].append(float(val[9])) # In Pa
    
    # The sampling time is 1 hour --> all radiation values are the same in W/m2
    # Diffuse horizontal radiation in Wh/m2
    results["diffuse"].append(float(val[15]))
    # Global - diffuse horizontal radiation in Wh/m2    
    results["beam"].append(float(val[13]) - float(val[15]))
    
    results["wind direction"].append(float(val[20])) # In °
    results["wind velocity"].append(float(val[21])) # In m/s
    
    results["cloudiness"].append(float(val[22])) # Total sky cover


filename = "DEU_Dusseldorf.104000_IWEC.epw"

result = {}
key_list = ["date", # (Year, Month, Day, Hour, Minute)
            "time", # Time in hours, beginning with 0
            "temperature", # Ambient temperature in °C
            "relative humidity", # In %
            "pressure", # In Pa
            "beam", # Direct horizontal radiation in Wh/m2 (resp. W/m2)
            "diffuse", # Diffuse horizontal radiation in Wh/m2 (resp. W/m2)
            "wind direction", # In °
            "wind velocity", # In m/s
            "cloudiness"] # 
for key in key_list:
    result[key] = []
    
with open(filename, "rb") as data:
    parse_location(data.readline(), result)
    
    # Skip lines 2-8
    while not ((data.readline()).split(","))[0] == "DATA PERIODS":
        data.readline()
    
    
    for line in data:
        parse_data(line, result)

# Finalize: Transform data to numpy array, if possible
result["time"] = np.linspace(start=0,
                             stop=len(result["temperature"])-1,
                             num=len(result["temperature"]),
                             dtype="int")
for key in key_list:
    result[key] = np.array(result[key])
    