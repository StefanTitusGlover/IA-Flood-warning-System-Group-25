from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run(): 
    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    stations_over = stations_level_over_threshold(stations, 0.8) #tol = 0.8
    for i in range(len(stations_over)):
        for station in stations:
            if station == stations_over[i][0]:
                print(station.name, station.relative_water_level())





if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()