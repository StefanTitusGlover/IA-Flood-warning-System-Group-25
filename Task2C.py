from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run(): 
    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    at_risk = stations_highest_rel_level(stations, 10)
    for station in at_risk:
        name = at_risk.name
        level = at_risk.relative_water_level
    print(name, level)


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()