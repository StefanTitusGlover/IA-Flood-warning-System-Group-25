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
    stationslist = []
    for station in stations:
        distance = haversine(station.coord,p)
        temp = [station.name, station.town, distance]
        stationslist.append(temp)
    orderedstations = sorted_by_key(stationslist, 2)
    return orderedstations
  



