from floodsystem.Plot import plot_water_level_with_fit_no_show,plot_water_levels_no_show
from floodsystem.geo import station_history
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib
import matplotlib.pyplot as plt


def test_plot_water_levels():
    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    station_profile,dates,levels = station_history("Hayes Basin",2)
    
    num_figures_before = 0
    plot_water_levels_no_show(station_profile,dates,levels)
    num_figures_after = plt.gcf().number
    assert num_figures_before < num_figures_after

def test_plot_water_level_with_fit():
    stations = build_station_list()  # Build list of stations
    update_water_levels(stations)
    station_profile,dates,levels = station_history("Hayes Basin",2)
    
    num_figures_before = 0
    plot_water_level_with_fit_no_show(station_profile,dates,levels,4)
    num_figures_after = plt.gcf().number
    assert num_figures_before < num_figures_after

test_plot_water_levels()
test_plot_water_level_with_fit
