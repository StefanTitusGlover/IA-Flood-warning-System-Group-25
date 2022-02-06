from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from floodsystem.utils import sorted_by_key
from floodsystem.station import inconsistent_typical_range_consistent

def run():
    """Requirements for  Task F"""

    stations_all = build_station_list()
    incon_stations = inconsistent_typical_range_consistent(stations_all)
    ordered_incon = sorted_by_key(incon_stations, 0)

    print(ordered_incon)
    


if __name__ == "__main__":
    run()