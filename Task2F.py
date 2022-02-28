from floodsystem.geo import station_history
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.Plot import plot_water_level_with_fit

def run():

    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    stations_to_check = stations_highest_rel_level(stations,20)# Gets the 20 stations with the highest relative waterlevels
    valid_stations =[]
    highest_stations = []
    for station in stations_to_check:
        station_profile,dates,levels = station_history(station.name,2)
        if len(dates) != 0: # station has valid data
            valid_stations.append(station)   
    highest_stations = valid_stations[0:5] # Takes the 5 highest stations
    for station in highest_stations:     
        station_profile,dates,levels = station_history(station.name,2)   
        plot_water_level_with_fit(station_profile,dates,levels,4)

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()