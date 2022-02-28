from floodsystem.geo import station_history
from floodsystem.geo import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

station_profile,dates,levels = station_history("Letcombe Bassett",2)
dates, levels = fetch_measure_levels(
        station_profile.measure_id, dt=datetime.timedelta(days=10))
print(dates)

