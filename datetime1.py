from datetime import datetime
from datetime import time
from datetime import date
def main():
    today=date.today()
    print('today date is :',today)
    print('date components: ',today.day,today.month,today.year)
    print('today weekday is :',today.weekday())
    days=['mon','tue','wed','thu','fri','sat','sun']
    print('which is a: ',days[today.weekday()])
    today=datetime.now()
    print('the current date and time is',today)
    t=datetime.time(datetime.now())
main()
