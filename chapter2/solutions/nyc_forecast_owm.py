'''
Retrieve three days' forecast of New York City and create a graph
Using https://github.com/csparpa/pyowm
'''
import matplotlib.pyplot as plt
from pyowm import OWM
import pytz

owm = OWM('<token>')

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
    date_time = []
    for w in weathers:
        forecast_temp = w.get_temperature('celsius')
        utc_dt = datetime.utcfromtimestamp(w.get_reference_time()).replace(tzinfo=pytz.utc)
        tz = pytz.timezone('America/New_York')
        dt = utc_dt.astimezone(tz)

        # print it
        date_time.append(dt.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        temp.append(forecast_temp['temp'])
    x = range(1, len(temp)+1)
    plt.plot(x, temp, 'o-')
    plt.xticks(x, date_time)
    plt.show()

if __name__ == '__main__':
    get_forecast('new york, us')
