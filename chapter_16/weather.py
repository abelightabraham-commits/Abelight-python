import csv
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')


filename = 'data/sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Get dates and high, lows temperature from this file.
    dates, highs, highs_2, lows, lows_2 = [], [], [], [], []
    for row in reader:
        current_dates = datetime.strptime(row[0], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        high_2 = int(row[6])
        low_2 = int(row[7])
        dates.append(current_dates)
        highs.append(high)
        highs_2.append(high_2)
        lows.append(low)
        lows_2.append(low_2)


#Plot the highs and lows temperature.
fig, ax = plt.subplots()
ax.plot(dates, highs, c='blue', alpha=0.5)
ax.plot(dates, lows, c='red', alpha=0.5)
ax.plot(dates, highs_2, c='green', alpha=0.5)
ax.plot(dates, lows_2, c='yellow', alpha=0.5)
plt.fill_between(dates, highs, lows, highs_2, lows_2, facecolor='blue', alpha=0.1)

#Format plot.
plt.title('Daily highs and lows temperature, july 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()