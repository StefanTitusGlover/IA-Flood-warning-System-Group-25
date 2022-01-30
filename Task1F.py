from floodsystem.stationdata import build_station_list

stations = build_station_list()
inconsistentstations = []

for station in stations:
    check = station.typical_range_consistent()
    if check == False:
        inconsistentstations.append(station.name)
inconsistentstations.sort()

print("The stations with inconsistent water level ranges are ", inconsistentstations)
print(" The number of stations with inconsistent water level ranges is", len(inconsistentstations))

