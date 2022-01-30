from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list() # generates a list of stations
    riverlist = rivers_with_station(stations) # generates a list of rivers with stations on them

    print("There are", len(riverlist), "rivers with at least one water monitoring station") # prints the number of rivers with stations
    print("The first 10 rivers are ", riverlist[:10]) # prints the first 10 rivers in alphabetical order

    riverdict = stations_by_river(stations)
    print( "The stations on the River Aire are:" , riverdict["River Aire"]) # prints the stations on the River Aire
    print("\n")
    print( "The stations on the River Cam are:" , riverdict["River Cam"]) # prints the stations on the River Cam
    print("\n")
    print( "The stations on the River Thames are:" , riverdict["River Thames"]) # prints the stations on the River Thames

if __name__ == "__main__":
    run()