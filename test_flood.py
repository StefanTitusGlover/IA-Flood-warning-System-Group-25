from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def test_stations_level_over_threshold():
    stationlist = build_station_list()
    update_water_levels(stationlist)
    flood_stations = stations_level_over_threshold(stationlist, 0)
    for i in range( len(flood_stations) - 1 ):
        assert flood_stations[i][1] >= flood_stations[i+1][1]
    assert type(flood_stations) == list
    for j in range(len(flood_stations)):
        assert type(flood_stations[j]) == tuple

def test_stations_highest_rel_level():
    stationlist = build_station_list()
    update_water_levels(stationlist)
    high_stations = stations_highest_rel_level(stationlist, 10)
    assert len(high_stations) == 10
    assert type(high_stations) == list
    level_list = []
    for station in  high_stations:
        assert type
        level_list.append(station.relative_water_level())
    for i in range(len(level_list)-1):
        assert level_list[i] >= level_list[i+1]


test_stations_level_over_threshold()
test_stations_highest_rel_level()