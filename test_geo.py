from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit # imports the haversine function
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number

def test_stations_by_distance_types(): # Testing the stations_by_distance function to ensure that the function returns the correct types
    stationlist = build_station_list() # builds a list of all the stations
    location = (52.2053, 0.1218)
    stations = stations_by_distance(stationlist,location)
    example = stations[0]
    assert type(stations) == list # Function should return a list
    assert type(example) == tuple # each element of the list should be a tuple
    assert type(example[0]) == str # first entry of the tuple should be a string
    assert type(example[1]) == str # second entry of the tuple should be a string
    assert type(example[2]) == float # third entry of the tuple should be a float

def test_stations_by_distance_functionalty(): # tests the functionality to ensure that the stations are ordered in ascending distance
    stationlist = build_station_list() # builds a list of all the stations
    location = (52.2053, 0.1218)
    stations = stations_by_distance(stationlist,location)
    i = 0
    while i < (len(stations) - 1) :
        assert stations[i][2] <= stations[i+1][2] # each entry should have a smaller distance than the subsequent
        i +=1

def test_stations_within_radius_types(): # tests that the function returns the correct types
    stationlist = build_station_list() # builds a list of all the stations
    centre = (52.2053, 0.1218) #coordinates for centre of cambridge
    stations = stations_within_radius(stationlist,centre,10)
    assert type(stations) == list # the function should return a list
    i = 0
    while i < len(stations) :
        assert type(stations[i]) == str # each entry of the list should be a string
        i +=1

def test_stations_within_radius_functionality():
    stationlist = build_station_list() # builds a list of all the stations
    centre = (52.2053, 0.1218) #coordinates for centre of cambridge
    radius = 10
    stations = stations_within_radius(stationlist,centre,radius)
    i = 0
    while i < len(stations) :
        for station in stationlist:
            if station == stations[i] :
                assert haversine(station.coord,centre) <= radius # tests if the distance from the stations to the coordinate is less than the given radius
        i +=1

def test_rivers_with_station():
    stationlist = build_station_list() # builds a list of all the stations
    rivers = rivers_with_station(stationlist)
    assert type(rivers) == list # Checks if the function returns a list
    i = 0 
    while i < len(rivers):
        assert type(rivers[i]) == str # checks if each entry of the function
        i += 1
    riversset = set(rivers) # creates a set, a list which definitely has no duplicates
    assert len(riversset) == len(rivers) # checks if the list that was returned contains no duplicates.

def test_stations_by_river():
    stationlist = build_station_list() # builds a list of all the stations
    rivers = rivers_with_station(stationlist) # generates a list of rivers
    rivers.sort()
    river_dictionary = stations_by_river(stationlist)
    assert type(river_dictionary) == dict # checks that the function outputs a dictionary
    river_keys = list(river_dictionary.keys())
    i = 0
    total = 0
    while i < (len(river_keys)):
        for river in rivers:
            if river_keys[i] == river:
                total += 1
        i +=1
    assert total == len(river_keys) # Checks if all the entries in river_keys are in the list of rivers

def test_rivers_by_station_number():
    stationlist = build_station_list()
    Number = 10
    rivers_with_most_stations = rivers_by_station_number(stationlist,Number)
    assert type(rivers_with_most_stations) == list # function should return a list
    example = rivers_with_most_stations[0]
    assert type(example) == tuple # each member of the list should be a tuple
    assert type(example[0]) == str # first entry of the tuple should be a string
    assert type(example[1]) == int # second entry of the tuple should be an integer
    assert len(rivers_with_most_stations) >= Number # the function should return greater than or equal to the number of stations requested
    i = 0
    while i < (len(rivers_with_most_stations)) - 1:
        assert rivers_with_most_stations[i][1] >= rivers_with_most_stations[i+1][1] # checks that function returns tuples in decreasing order of number of rivers
        i += 1
     


test_stations_by_distance_types()
test_stations_by_distance_functionalty()
test_stations_within_radius_types()
test_stations_within_radius_functionality()
test_rivers_with_station()
test_stations_by_river()
test_rivers_by_station_number()