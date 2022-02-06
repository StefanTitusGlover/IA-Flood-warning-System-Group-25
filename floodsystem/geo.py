# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_within_radius(stations, centre, r):
    #Function that gives a list of all stations within a given radius
    r = input() #takes variable r from user input
    stations_in_r = [] 
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_in_r.append(station)
    return stations_in_r


def rivers_by_station_number(stations, N):
    """Function that creates a list of the rivers with the greatest number of stations"""
    num_stations = []
    rivers = stationstoriver(stations)
    for river in rivers:
        total = []
        for station in stations:
            if river == station.river:
                total += 1
    num_stations.append(river, total)
    ordnum_stations = sorted_by_key(num_stations, 1)
    
    i = 0 #indicates Nth position  note: ask what happens if other positions hace same values
    while i <= N :
        final_rivers = []
        final_rivers.append(ordnum_stations[i])
    
        if ordnum_stations[i][1] == ordnum_stations[i + 1][1]:
            final_rivers.append(ordnum_stations[i + 1][1])
            i += 1
            N += 1
        else:
            i += 1
    return final_rivers 
            

