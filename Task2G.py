from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import station_history
from floodsystem.Analysis import risk_levels
from floodsystem.station import consistent_typical_range_stations
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    print(len(stations))
    stationlist = stations_highest_rel_level(stations,100)
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
    print("The low risk towns are ", low_risk)
    print("\n")
    print("The medium risk towns are ", medium_risk)
    print("\n")
    print("The high risk towns are ", high_risk)
    print("\n")
    print("The severe risk towns are ", severe_risk)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()