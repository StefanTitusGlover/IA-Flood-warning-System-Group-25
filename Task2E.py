from floodsystem.geo import station_history
from floodsystem.geo import plot_water_levels

def run():
    station_profile,dates,levels = station_history("Cam",2)
    plot_water_levels(station_profile,dates,levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()

# 2E is not currently finished and required code from 2B and C to be done
