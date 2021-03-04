import calendar as c

#---alt code---
# wday = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# year,month,day=list(map(int,input().split()))
# wn=c.weekday(year,month,day)
# print(wday[wn])


n1,n2,n3=map(int,input().split())
print((c.day_name[c.weekday(n3,n1,n2)]).upper())

#---others---
#import calendar

#print(list(calendar.day_name)[calendar.weekday(year=,month=,day=)].upper())


# calr=c.TextCalendar(firstweekday=0).formatyear(2021)
# c.TextCalendar(firstweekday=0).pryear(2021)

#calr=c.TextCalendar().formatmonth(2021,2)
#c.TextCalendar().prmonth(2021,2)

#year,month,day=2021,1,28


# print(calr)

# def weekDayName(weekDay):
#     wn=list(c.day_name)
#     return wn[weekDay]
# print(weekDayName(2))