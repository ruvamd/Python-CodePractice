import csv
import matplotlib.pyplot as plt

from datetime import datetime as dt

file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/sitka_weather_2018_simple.csv'
with open(file) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    
    # get high rain
    dates,highs=[],[]
    for row in reader:
        high=float(row[3])
        highs.append(high)

# plot the rain
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(highs,c='red',alpha=1)
ax.plot(c='blue',alpha=1)

# format plot
ax.set_title('title')
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('rain',fontsize=16)

ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()