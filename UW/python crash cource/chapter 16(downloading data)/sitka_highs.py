import csv

file='UW/python crash cource/chapter 16(downloading data)/data/sitka_weather_07-2018_simple.csv'
with open(file) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    # print(header_row)
    # for indx,col_header in enumerate(header_row):
    #     print(indx,col_header)
    # get high tempr
    highs=[]
    for row in reader:
        high=int(row[5])
        highs.append(high)
print(highs)
