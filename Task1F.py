from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    stations = build_station_list()
    inconsistentstations = inconsistent_typical_range_stations(stations)
    print("The stations with inconsistent water level ranges are ", inconsistentstations)
    print(" The number of stations with inconsistent water level ranges is", len(inconsistentstations))

if __name__ == "__main__":
    print("***Task 1F: CUED Part IA Flood Warning System***")
    run()
