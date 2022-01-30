from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

stations = build_station_list()
riverlist = rivers_with_station(stations)

print("There are", len(riverlist), "rivers with at least one water monitoring station")

riverlist.sort()
print("The first 10 rivers are ", riverlist[:10])