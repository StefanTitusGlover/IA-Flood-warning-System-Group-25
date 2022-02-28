import numpy as np
import matplotlib
from floodsystem.stationdata import update_water_levels
from floodsystem.geo import station_history
from floodsystem.station import consistent_typical_range_stations
from floodsystem.Analysis import polyfit, gradient_polyfit, risk_levels
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level

def test_polyfit():
    station_profile,dates,levels = station_history("Hayes basin",2)
    poly,shift = polyfit(dates,levels,4)
    assert type(poly) == list
    assert len(poly) == 4
    assert type(poly[0]) == float
    assert type(shift) == float

def test_gradient_polyfit():
    station_profile,dates,levels = station_history("Hayes basin",2)
    gradient = gradient_polyfit(dates,levels,4)
    assert type(gradient) == float

def test_risk_levels():
    stations = build_station_list()
    update_water_levels(stations)
    print(len(stations))
    stationlist = stations_highest_rel_level(stations,50)
    valid_stations = []
    low_risk = [] 
    medium_risk = [] 
    high_risk = []
    severe_risk = []
    for station in stationlist:
        station_profile,dates,levels = station_history(station.name,2)
        if len(dates) != 0: # station has valid data
            valid_stations.append(station)

    low_risk, medium_risk, high_risk, severe_risk = risk_levels(valid_stations)
    assert type(low_risk) == list
    assert type(medium_risk) == list
    assert type(high_risk) == list
    assert type(severe_risk) == list

test_gradient_polyfit()
test_polyfit()
test_risk_levels()