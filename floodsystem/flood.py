from .utils import sorted_by_key 
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.station import consistent_typical_range_stations
from floodsystem.stationdata import update_water_levels

def stations_level_over_threshold(stations, tol):
    flood_list = []
    update_water_levels(stations)
    consistent_stations = consistent_typical_range_stations(stations)
    for station in consistent_stations:
        if station.relative_water_level() > tol:
            over_station = (station.name, station.relative_water_level())
            flood_list.append(over_station)
    flood_list = sorted_by_key(flood_list, 1, reverse=True)
    return flood_list

def stations_highest_rel_level(stations, N):
    high_stations = stations_level_over_threshold(stations, 0) #tol=0 so stations in typical range are considered for function
    highest_list = []
    for i in range(N):
        highest_list.append(high_stations[i][0]) #returns the list of stations (names) with highest level 
    return highest_list


