from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import typical_range_consistent
def run(): 
    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    stations_over = stations_level_over_threshold(stations, 0.8) #tol = 0.8

    for station in stations:
        if station.typical_range_consistent()  == True:
            name = stations_over[0]
            level = stations_over[1]
            print(name, level)
            
        else:
            print('-')

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()