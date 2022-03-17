import matplotlib.pyplot as plt
from Share import get_last_thirty_days, print_last_thirty_days
from datetime import datetime

'''
from datetime import datetime
import matplotlib.pyplot as plt

a = [['2015-01-08', '174.0'], ['2015-01-09', '172.0'], ['2015-01-11', '170.5']]

dates = [datetime.strptime(d[0], "%Y-%m-%d") for d in a]
values = [float(d[1]) for d in a]

plt.plot(dates, values)

plt.show()

'''

lst = get_last_thirty_days('Source\\MSFT.csv')

x_coordinate = []
y_coordinate = []

for sublist in lst:
    x_coordinate.append(sublist[0])  # datum
    y_coordinate.append(float(sublist[4]))  # close


plt.plot(y_coordinate)

plt.show()

print_last_thirty_days()
