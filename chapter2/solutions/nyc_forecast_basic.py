'''
nyc_forecast_basic.py

Create a graph showing a city's temperature forecast for the day.
'''
import matplotlib.pyplot as plt

def plot_forecast():

    time_of_day = ['4 AM', '7 AM', '10 AM', '1 PM', '4 PM', '7PM', '10 PM']
    forecast_temp = [71, 70, 74, 80, 82, 81, 76]
    time_interval = range(1, len(time_of_day) + 1)

    plt.plot(time_interval, forecast_temp, 'o-')
    plt.xticks(time_interval, time_of_day)
    plt.show()

if __name__ == '__main__':
    plot_forecast()
