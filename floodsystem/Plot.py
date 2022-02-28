import matplotlib
import matplotlib.pyplot as plt
from floodsystem.Analysis import polyfit
import numpy as np

def plot_water_levels(station,dates,levels): # This function needs to be tested
    name = station.name
    if station.typical_range_consistent() == True: # if the station's typical levels meet the consistency check the upper and lower values are taken so that they can be plotted
        lower = station.typical_range[0]
        lower_level = [lower] * len(dates) # Makes an array of the lower value of the correct length for plotting
        upper = station.typical_range[1]
        upper_level = [upper] * len(dates) # Makes an array of the upper value of the correct length for plotting

    if station.typical_range_consistent() == True:
        plt.plot(dates,levels)
        plt.plot(dates,lower_level)
        plt.plot(dates,upper_level)

        plt.xlabel('Date')
        plt.ylabel('Water level /m')
        plt.xticks(rotation=45);
        plt.legend(["Actual Level", "Lower typical boundary", "Upper typical boundary"])
        plt.title("Water level of " + str(station.name))
        plt.show()
    
    else:
        plt.plot(dates,levels)
        plt.xlabel('Date')
        plt.ylabel('Water level /m')
        plt.xticks(rotation=45);
        plt.title("Water level of " + str(station.name))
        plt.show() 

def plot_water_levels_no_show(station,dates,levels): # This function needs to be tested
    name = station.name
    if station.typical_range_consistent() == True: # if the station's typical levels meet the consistency check the upper and lower values are taken so that they can be plotted
        lower = station.typical_range[0]
        lower_level = [lower] * len(dates) # Makes an array of the lower value of the correct length for plotting
        upper = station.typical_range[1]
        upper_level = [upper] * len(dates) # Makes an array of the upper value of the correct length for plotting

    if station.typical_range_consistent() == True:
        plt.plot(dates,levels)
        plt.plot(dates,lower_level)
        plt.plot(dates,upper_level)

        plt.xlabel('Date')
        plt.ylabel('Water level /m')
        plt.xticks(rotation=45);
        plt.legend(["Actual Level", "Lower typical boundary", "Upper typical boundary"])
        plt.title("Water level of " + str(station.name))
        plt.show(block = False)
    
    else:
        plt.plot(dates,levels)
        plt.xlabel('Date')
        plt.ylabel('Water level /m')
        plt.xticks(rotation=45);
        plt.title("Water level of " + str(station.name))
        plt.show() 

def plot_water_level_with_fit(station, dates, levels, p):
    poly,shift = polyfit(dates, levels,p)
    poly_dates = []
    poly_levels = []
    dates_formatted = matplotlib.dates.date2num(dates)
    func=np.poly1d(poly) # makes a function out of the polynomial
    for number in dates_formatted:
        temp = number - shift
        poly_dates.append(temp)
        value = func(temp)
        poly_levels.append(value)
    lower = station.typical_range[0]
    lower_level = [lower] * len(dates)
    upper = station.typical_range[1]
    upper_level = [upper] * len(dates)
    

    plt.plot(dates,poly_levels, label = "Best fit polynomial Data")
    plt.plot(dates,levels, label = "Actual Data")
    plt.plot(dates,lower_level, label = "Lower typical boundary") # plots the lower
    plt.plot(dates,upper_level, label = "Upper typical boundary")

    plt.xlabel('Date')
    plt.ylabel('Water level /m')
    plt.xticks(rotation=45);
    plt.legend()
    plt.title("Water level of " + str(station.name))
    plt.show()

def plot_water_level_with_fit_no_show(station, dates, levels, p):
    poly,shift = polyfit(dates, levels,p)
    poly_dates = []
    poly_levels = []
    dates_formatted = matplotlib.dates.date2num(dates)
    func=np.poly1d(poly) # makes a function out of the polynomial
    for number in dates_formatted:
        temp = number - shift
        poly_dates.append(temp)
        value = func(temp)
        poly_levels.append(value)
    lower = station.typical_range[0]
    lower_level = [lower] * len(dates)
    upper = station.typical_range[1]
    upper_level = [upper] * len(dates)
    

    plt.plot(dates,poly_levels, label = "Best fit polynomial Data")
    plt.plot(dates,levels, label = "Actual Data")
    plt.plot(dates,lower_level, label = "Lower typical boundary") # plots the lower
    plt.plot(dates,upper_level, label = "Upper typical boundary")

    plt.xlabel('Date')
    plt.ylabel('Water level /m')
    plt.xticks(rotation=45);
    plt.legend()
    plt.title("Water level of " + str(station.name))
    plt.show(block = False)