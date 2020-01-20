import datetime,calendar

from datetime import datetime,timedelta

now=datetime.now()

testDate=now+timedelta(days=2)
myFirstLinkedInCourse=now-timedelta(weeks=3)

print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate>myFirstLinkedInCourse:
    print('comparison works')
cal=calendar.month(2000,10)
print(cal)