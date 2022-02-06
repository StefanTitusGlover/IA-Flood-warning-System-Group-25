from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run(): 
    stations = build_station_list()  # Build list of stations
    location = (52.2053, 0.1218) # Chose a location by its latitude and longitude
    orderedlist = stations_by_distance(stations, location) # generates an ordered list of stations by distance to the given

    print(orderedlist[:10]) # print the first 10 items of the list
    print("\n")
    print(orderedlist[-10:]) # print the last 10 items of the list

if __name__ == "__main__":
    print("***Task 1B: CUED Part IA Flood Warning System***")
    run()