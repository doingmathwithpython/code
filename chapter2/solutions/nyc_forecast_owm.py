'''
Retrieve a day's forecast of New York City and create a graph
Using https://github.com/csparpa/pyowm
'''
import matplotlib.pyplot as plt
from pyowm import OWM
import pytz

owm = OWM('<token>')

def get_forecast(city):
    # this used to be daily_forecast
    # https://github.com/csparpa/pyowm/issues/266
    fc = owm.three_hours_forecast(city)
    f = fc.get_forecast()
    
    # three_hours_forecast() returns 5 day forecast at a granularity
    # of three hours
    # We plot the forecast for the next 24 hours (so, first 8 intervals)
    weathers = f.get_weathers()[0:8]
    data_points = ['temp', 'temp_max', 'temp_min', 'temp_kf']
    temp = []
    date_time = []
    for w in weathers:
        forecast_temp = w.get_temperature('celsius')
        utc_dt = datetime.utcfromtimestamp(w.get_reference_time()).replace(tzinfo=pytz.utc)
        tz = pytz.timezone('America/New_York')
        dt = utc_dt.astimezone(tz)
        date_time.append(dt.strftime('%Y-%m-%d %H:%M'))
        temp.append(forecast_temp['temp'])
    x = range(1, len(temp)+1)
    plt.plot(x, temp, 'o-')
    plt.xticks(x, date_time, rotation=45)
    plt.show()
    # Uncomment below and comment the previous line to save the image
    # plt.savefig('nyc_owm_forecast.png')


if __name__ == '__main__':
    get_forecast('new york, us')
