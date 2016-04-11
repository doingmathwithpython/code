'''
Retrieve a day's forecast of New York City and create a graph
Using https://github.com/csparpa/pyowm
'''
import matplotlib.pyplot as plt
from pyowm import OWM

owm = OWM()

def get_forecast(city):
    fc = owm.daily_forecast(city, limit=1)
    f = fc.get_forecast()
    w = f.get_weathers()[0]
    forecast_temp = w.get_temperature('celsius')
    day_intervals = ['morn', 'day', 'eve', 'night']
    temp = []
    for timeofday in day_intervals:
        temp.append(forecast_temp[point])
    x = range(1, len(day_intervals)+1)
    plt.plot(x, temp, 'o-')
    plt.xticks(x, day_intervals)
    plt.show()

if __name__ == '__main__':
    get_forecast('new york, us')
