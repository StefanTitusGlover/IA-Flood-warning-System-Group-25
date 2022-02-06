from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_stations_by_distance(): # Testing the stations_by_distance function
    stationlist = build_station_list() # builds a list of all the stations
    location = (52.2053, 0.1218)
    stations = stations_by_distance(stationlist,location)
    example = stations[0]
    assert type(example) == tuple
    assert type(example[0]) == str
    assert type(example[1]) == str
    assert type(example[2]) == float

test_stations_by_distance()