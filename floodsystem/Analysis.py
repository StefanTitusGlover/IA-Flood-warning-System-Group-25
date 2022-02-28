import numpy as np
import matplotlib
from floodsystem.stationdata import update_water_levels
from floodsystem.geo import station_history
from floodsystem.station import consistent_typical_range_stations

def polyfit(dates, levels, p):
    dates_formatted = matplotlib.dates.date2num(dates)
    shift = dates_formatted[0]
    dates_plot = []
    for number in dates_formatted:
        temp = number - shift
        dates_plot.append(temp)
    poly = np.polyfit(dates_plot,levels,p)
    return poly,shift

def gradient_polyfit(dates, levels, p):
    poly,shift = polyfit(dates, levels, p)
    derivative = np.polyder(poly)
    func=np.poly1d(derivative) # makes a function out of the derivative
    dates_formatted = matplotlib.dates.date2num(dates)
    gradient = func(dates_formatted[0] - shift)
    return gradient

def risk_levels(stations): #Parameter is a list of station objects
    update_water_levels(stations)
    stationlist = consistent_typical_range_stations(stations)
    low_risk = [] 
    medium_risk = [] 
    high_risk = []
    severe_risk = []
    check = True
    for station in stationlist:
        try:
            station_profile,dates,levels = station_history(station.name,2)
        except:
            check = False
        if check == True:
            gradient = gradient_polyfit(dates, levels,4)
            relative_level = station.relative_water_level()
            if relative_level <= 1 :    
                low_risk.append(station.town)
            elif (1< relative_level <= 1.25) and (gradient<=0):
                low_risk.append(station.town)
            elif (1< relative_level <= 1.25) and (gradient>0):
                medium_risk.append(station.town)
            elif (1.25< relative_level <= 1.5):
                medium_risk.append(station.town)
            elif (1.5< relative_level <= 1.75) and (gradient<=0):
                medium_risk.append(station.town)
            elif (1.5< relative_level <= 1.75) and (gradient>0):
                high_risk.append(station.town)
            elif (1.75< relative_level <= 2) and (gradient<=0):
                high_risk.append(station.town)
            elif (1.75< relative_level <= 2) and (gradient>0):
                severe_risk.append(station.town)
            else:
                severe_risk.append(station.town)
    return low_risk,medium_risk,high_risk,severe_risk





