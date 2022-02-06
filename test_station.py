# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range ():
    stationslist = build_station_list()
    for station in stationslist:
        assert type(station.typical_range_consistent()) == bool # Checks that the typical_range_consistent function returns a boolean
    inconstistent_stations = inconsistent_typical_range_stations(stationslist)
    i = 0
    total = 0
    while i < len(inconstistent_stations):
        for station in stationslist:
            if station == inconstistent_stations[i]:
                assert station.typical_range_consistent() == False # Checks that every station in the inconsistent station list has a value false for whether the typical range is consistent
        i += 1
    for station in stationslist:   
        if station.typical_range_consistent() == False:
            total += 1
    assert total == len(inconstistent_stations) # Checks that the number of stations that have been caught as being inconsistent matches the true number of inconsistent stations

test_create_monitoring_station()
test_typical_range()