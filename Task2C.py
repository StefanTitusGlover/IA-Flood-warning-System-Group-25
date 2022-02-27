from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run(): 
    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    at_risk = stations_highest_rel_level(stations, 10)
    print(type(at_risk[0]))
    for station in at_risk:
        print(station.name, station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()