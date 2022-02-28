from floodsystem.geo import station_history
from floodsystem.geo import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stationlist = build_station_list()
Days = 2
name = "Hayes Basin"
station_profile,dates,levels = station_history(name,Days)
assert type(dates) == list
assert type(levels) == list
assert type(levels[0]) == float # Types are checked
delta = dates[0].date() - dates[-1].date() # checks that the number of days worth of data is the same as the requested number
print(delta)
print(datetime.timedelta(days = Days))
