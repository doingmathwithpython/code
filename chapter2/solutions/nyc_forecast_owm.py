'''
Retrieve three days' forecast of New York City and create a graph
Using https://github.com/csparpa/pyowm
'''
import matplotlib.pyplot as plt
from pyowm import OWM

owm = OWM('54c5451fcc146ce043f4f44153e4ea4b')

def get_forecast(city):
    # https://github.com/csparpa/pyowm/issues/266
    fc = owm.three_hours_forecast(city)
    f = fc.get_forecast()
    
    # three_hours_forecast() returns 5 day forecast at a granularity
    # of three hours
    # we plot them all
    weathers = f.get_weathers()
    
    
    data_points = ['temp', 'temp_max', 'temp_min', 'temp_kf']
    temp = []
    for w in weathers:
        forecast_temp = w.get_temperature('celsius')
        #for point in data_points:
        temp.append(forecast_temp['temp'])
    x = range(1, len(temp)+1)
    plt.plot(x, temp, 'o-')
    #plt.xticks(x, day_intervals)
    plt.show()

if __name__ == '__main__':
    get_forecast('new york, us')
