# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_within_radius(stations, centre, r):
    #Function that gives a list of all stations within a given radius
    r = input() #takes variable r from user input
    stations_in_r = [] 
    for station in stations:
        distance = haversine(station.coord, centre)
        if distance < r:
            stations_in_r.append(station)
    return stations_in_r
