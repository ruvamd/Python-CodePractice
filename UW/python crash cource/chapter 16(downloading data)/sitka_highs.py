import csv
import matplotlib.pyplot as plt

from datetime import datetime as dt

file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/sitka_weather_2018_simple.csv'
with open(file) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    # print(header_row)
    # for indx,col_header in enumerate(header_row):
    #     print(indx,col_header)
    
    # get high tempr
    dates,highs,lows=[],[],[]
    for row in reader:
        current_date=dt.strptime(row[2],'%Y-%m-%d')
        high=int(row[5])
        low=int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# print(highs)

# plot the high temperature
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# format plot
ax.set_title('title')
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('temperature (F)',fontsize=16)


ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()