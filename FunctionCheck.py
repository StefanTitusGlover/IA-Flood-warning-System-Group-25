from floodsystem.geo import station_history
from floodsystem.Plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.Analysis import polyfit, gradient_polyfit
from floodsystem.Plot import plot_water_level_with_fit
from floodsystem.station import consistent_typical_range_stations


station_profile,dates,levels = station_history("Upper Pound",2)
poly = polyfit(dates,levels,4)
grad = gradient_polyfit(dates,levels,4)
print(poly,grad)
