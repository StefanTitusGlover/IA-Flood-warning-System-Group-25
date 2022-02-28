from floodsystem.geo import station_history
from floodsystem.Plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.Analysis import polyfit
from floodsystem.Plot import plot_water_level_with_fit

stationlist = build_station_list()
Days = 2
name = "Hayes Basin"
station_profile,dates,levels = station_history(name,Days)
plot_water_level_with_fit(station_profile,dates,levels,4)
