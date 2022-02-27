from floodsystem.station import consistent_typical_range_stations
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
consistent_stations = consistent_typical_range_stations(stations)
for station in consistent_stations:
    den = station.typical_range[1] - station.typical_range[0] #finds value of the range
    num = station.latest_level - station.typical_range[0] #where latest level lies within range
    ratio = num / den
    print(ratio)
    
