from floodsystem.geo import station_history
from floodsystem.geo import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():

    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    stations_to_check = stations_highest_rel_level(stations,20)# Gets the 20 stations with the highest relative waterlevels
    valid_stations =[]
    highest_stations = []
    for station in stations_to_check:
        station_profile,dates,levels = station_history(station.name,10)
        if len(dates) != 0: # station has valid data
            valid_stations.append(station)   
    highest_stations = valid_stations[0:5] # Takes the 5 highest stations
    
    for station in highest_stations:
        station_profile,dates,levels = station_history(station.name,10)
        plot_water_levels(station_profile,dates,levels)

    


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

# 2E is not currently finished and required code from 2B and C to be done
