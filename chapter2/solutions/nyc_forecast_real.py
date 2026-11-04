'''
Retrieve a day's forecast of New York City and create a graph
Using data downloaded from https://doingmathweatherforecast.ai.studio/
'''
import csv
import matplotlib.pyplot as plt


def read_csv(filename):

    time_of_days = []
    forecast_temperature = []

    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            # Extract only the time from date and time
            time_of_day = row[0].split()[1]
            time_of_days.append(time_of_day)
            forecast_temperature.append(float(row[1]))

    return time_of_days, forecast_temperature


def plot_forecast(time_of_day, forecast_temperature):

    # time_of_day = ['4 AM', '7 AM', '10 AM', '1 PM', '4 PM', '7PM', '10 PM']
    # forecast_temp = [71, 70, 74, 80, 82, 81, 76]
    time_interval = range(1, len(time_of_day) + 1)

    plt.plot(time_interval, forecast_temperature, 'o-')
    plt.xticks(time_interval, time_of_day)
    plt.show()
    # Uncomment below and comment the previous line to save the image
    # plt.savefig('nyc_owm_forecast.png')


if __name__ == '__main__':
    time_of_day, forecast_temperature = read_csv("weather_New_York_1d_3h.csv")
    plot_forecast(time_of_day, forecast_temperature)
