from .utils import sorted_by_key 

def stations_level_over_threshold(stations, tol):
    flood_list = []
    for station in stations:
        if station.relative_water_level() > tol:
            over_station = (station, station.relative_water_level)
            flood_list.append(over_station)
    return sorted_by_key(flood_list, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    high_stations = stations_level_over_threshold(stations, 0) #tol=0 so stations in typical range are considered for function
    highest_list = []
    for i in range(N):
        highest_list.append(high_stations[i][0]) #returns the list of stations (names) with highest level 
    return highest_list


