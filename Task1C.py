from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for  Task C"""

    stations_all = build_station_list()

    centre = (52.2053, 0.1218) #coordinates for centre of cambridge

    stationslist = (stations_within_radius(stations_all, centre, 10))
   

    print("These stations are within 10km of Cambridge City centre:", stationslist)




if __name__ == "__main__":
    print("***Task 1C: CUED Part IA Flood Warning System***")
    run()

#test to see if this uploads correctly