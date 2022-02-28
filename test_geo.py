from distutils.command.build import build
import imp
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import station_history
import datetime

def test_stations_by_distance_types(): # Testing the stations_by_distance function
    stationlist = build_station_list() # builds a list of all the stations
    location = (52.2053, 0.1218)
    stations = stations_by_distance(stationlist,location)
    example = stations[0]
    assert type(stations) == list
    assert type(example) == tuple
    assert type(example[0]) == str
    assert type(example[1]) == str
    assert type(example[2]) == float

def test_stations_by_distance_functionality(): #checks function ouputs stations ordered in ascending dist
    stationlist = build_station_list()
    location =  (52.2053, 0.1218)
    stations = stations_by_distance(stationlist, location)
    i = 0
    while i < (len(stations) - 1):
        assert stations[i][2] <= stations[i+1][2] #each station should have smaller dist than the next in the list
        i += 1

def test_stations_within_radius_types(): 
    stationlist = build_station_list()
    centre = (52.305, 0.1218) #coordinates for centre of cambridge
    stations = stations_within_radius(stationlist, centre, 10)
    assert type(stations) == list
    i = 0
    while i < len(stations):
        assert type(stations[i]) == str 
        i += 1
    
def test_stations_within_radius_functionality():
    stationlist = build_station_list()
    centre = (52.305, 0.1218)
    r = 10
    stations = stations_within_radius(stationlist, centre, r)
    i = 0
    while i < len(stations):
        for station in stationlist:
            if station == stations[i]:
                assert haversine(station.coord, centre) <= r 
        i += 1


def test_rivers_with_stations():
    stationlist = build_station_list()
    rivers = rivers_with_station(stationlist)
    assert type(rivers) == list
    i = 0
    while i < len(rivers):
        assert type(rivers[i]) == str
        i += 1
    river_set = set(rivers)  #set assures there are no duplicates
    assert len(river_set) == len(rivers) #checks there are no duplicates

def test_stations_by_river():
    stationlist = build_station_list()
    rivers = rivers_with_station(stationlist) #list of rivers
    rivers.sort()
    river_dict = stations_by_river(stationlist)
    assert type(river_dict) == dict #ensures output of function is a dictionary
    river_keys = list(river_dict.keys())
    i = 0
    total = 0
    while i < (len(river_keys)):
        for river in rivers:
            if river_keys[i] == river: #checks if all entries in river_keys are in list of rivers
                total += 1
        i += 1
    assert total == len(river_keys)

def test_rivers_by_station_number():
    stationlist = build_station_list()
    N = 10
    rivs_most_stations = rivers_by_station_number(stationlist, N)
    assert type(rivs_most_stations) == list
    example = rivs_most_stations[0]
    assert type(example) == tuple
    assert type(example[0]) == str
    assert type(example[1]) == int
    assert (len(rivs_most_stations) >= N) #function should return list with >= N entries. Accounts for the case where multiple rivers have Nth largest no. stations
    i = 0
    while i < (len(rivs_most_stations) - 1):
        assert rivs_most_stations[i][1] >= rivs_most_stations[i+1][1] #should return tuples in decr order
        i += 1

def test_station_history():
    stationlist = build_station_list()
    Days = 2
    name = "Hayes Basin"
    station_profile,dates,levels = station_history(name,Days)
    assert type(dates) == list
    assert type(levels) == list
    assert type(levels[0]) == float # Types are checked
    delta = dates[0].date() - dates[-1].date() # checks that the number of days worth of data is the same as the requested number
    print(delta)
    assert datetime.timedelta(days = Days) == delta
    
    
test_stations_by_distance_types()
test_stations_by_distance_functionality()
test_stations_within_radius_types()
test_stations_within_radius_functionality()
test_rivers_with_stations()
test_stations_by_river()
test_rivers_by_station_number()
test_station_history()


