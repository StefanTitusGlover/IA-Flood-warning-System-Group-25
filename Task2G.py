from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.Analysis import risk_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    low_risk = [] 
    medium_risk = [] 
    high_risk = []
    severe_risk = []

    low_risk, medium_risk, high_risk, severe_risk = risk_levels(stations)
    print("The low risk towns are ", low_risk)
    print("\n")
    print("The medium risk towns are ", medium_risk)
    print("\n")
    print("The high risk towns are ", high_risk)
    print("\n")
    print("The severe risk towns are ", severe_risk)

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()