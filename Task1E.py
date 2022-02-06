from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():

    """Requirements for  Task E"""

    stations_all = build_station_list()
    riverstation_list = rivers_by_station_number(stations_all, 9)
    print(riverstation_list)

if __name__ == "__main__":
    print("***Task 1E: CUED Part IA Flood Warning System***")
    run()