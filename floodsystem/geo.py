# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit # Imports the haversine function for calculating distances between coordinates

def stations_by_distance(stations,p):
    """" Function that  orders a list of stations by distance to a given location"""
    stationslist = [] # creates an empty list which will be used to store the required station data
    for station in stations:
        distance = haversine(station.coord,p) # calculates the distance between a station and the coordinate p
        temp = [station.name, station.town, distance] # creates a list of the station name, town and distance to a point
        stationslist.append(temp) # adds the individual list to the station list
    orderedstations = sorted_by_key(stationslist, 2) # generates an ordered list by distance, the third entry
    return orderedstations
  



