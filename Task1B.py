from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()  # Build list of stations
location = (52.2053, 0.1218)
orderedlist = stations_by_distance(stations, location)

print(orderedlist[:10])
print(orderedlist[-10:])
