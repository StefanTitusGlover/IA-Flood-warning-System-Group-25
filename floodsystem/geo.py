# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit # imports the haversine function

def stations_by_distance(stations,p):
    """" Function that  orders a list of stations by distance to a given location"""
    stationslist = [] # creates an empty list which will be used to store the required station data
    for station in stations:
        distance = haversine(station.coord,p) # calculates the distance between a station and the coordinate p
        temp = (station.name, station.town, distance) # creates a list of the station name, town and distance to a point
        stationslist.append(temp) # adds the individual list to the station list
    orderedstations = sorted_by_key(stationslist, 2) # generates an ordered list by distance, the third entry
    return orderedstations

def stations_within_radius(stations, centre, r): #Function that gives a list of all stations within a given radius
    stations_in_r = [] 
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_in_r.append(station.name)
    stations_in_r.sort()
    return stations_in_r

def rivers_with_station(stations):
    """" Function that returns the name of the rivers with monitoring stations"""
    riverlist = [] # creates an empty list which will be used to store the rivers
    for station in stations:
        newriver = station.river # for every station in the list, the river associated with that station is stored
        if newriver in riverlist:
            newriver = 0 # if the river is already in the list of rivers nothing happens
        else:
            riverlist.append(newriver) #if the river is not in the list of rivers it is added to the list
    riverlist.sort() # sorts the rivers alphabetically
    return riverlist

def stations_by_river(stations):
    rivers = rivers_with_station(stations) # generates a list of rivers in alphabetical order
    riverdict = {} # creates the final dictionary
    i = 0
    while i < len(rivers) :
        stationstoriver = [] # creates a temporary list that will be used to store the station on each river
        for station in stations:
            if station.river == rivers[i]:
                stationstoriver.append(station.name) # if the station is on the river the name of the station is added to the temporary list
            else:
                i = i
        stationstoriver.sort() # sorts the temporary list alphabetically
        riverdict[rivers[i]] = stationstoriver # adds the river and the temporary list to the dictionary
        i += 1
    return riverdict


def rivers_by_station_number(stations, N):
    """Function that creates a list of the rivers with the greatest number of stations"""
    num_stations = []
    rivers = rivers_with_station(stations)
    for river in rivers:
        total = 0
        for station in stations:
            if river == station.river:
                total += 1
        temp = (river, total)
        num_stations.append(temp)
    ordnum_stations = sorted_by_key(num_stations, 1, True)
 

    i = 0 
    final_rivers = []
    while i <= N-1 :
        
        if i < N-1:
            final_rivers.append(ordnum_stations[i])  
            i += 1             
        else:
            if ordnum_stations[i][1] > ordnum_stations[i + 1][1]:
                final_rivers.append(ordnum_stations[i])
                i += 1
            elif ordnum_stations[i][1] == ordnum_stations[i + 1][1]:
                final_rivers.append(ordnum_stations[i])
                i += 1
                N += 1
            else:
                i += 1

    return final_rivers 
             


