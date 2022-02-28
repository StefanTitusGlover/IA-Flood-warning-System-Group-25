import numpy as np
import matplotlib

def polyfit(dates, levels, p):
    dates_formatted = matplotlib.dates.date2num(dates)
    shift = dates_formatted[0]
    dates_plot = []
    for number in dates_formatted:
        temp = number - shift
        dates_plot.append(temp)
    poly = np.polyfit(dates_plot,levels,p)
    return poly,shift


