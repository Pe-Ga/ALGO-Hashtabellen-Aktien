import matplotlib.dates as mdates
from csv_reader import get_last_thirty_days
import Share
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as subplot
from datetime import datetime

lst = get_last_thirty_days('Source\\MSFT.csv')

x_coordinate = []
y_coordinate = []

for sublist in lst:
    x_coordinate.append(sublist[0])  # datum
    y_coordinate.append(float(sublist[4]))  # close

x = [datetime.strptime(d, "%Y-%m-%d") for d in x_coordinate]  # parses strings to datetime
xs = matplotlib.dates.date2num(x)                             #converts datetime
formatter = matplotlib.dates.DateFormatter('%d-%m\n%Y')       #formates datetime to d-m format

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_major_formatter(formatter)
#ax.set_title(object.getName())                                               # title = class Share getName
plt.grid()

ax.plot(xs, y_coordinate)

plt.show()


