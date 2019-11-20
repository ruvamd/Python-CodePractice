from datetime import datetime,timedelta
today=datetime.now()
print('today is: '+str(today))

oneDay=timedelta(days=1) 
yesterday=today-oneDay
print('yesterday was: '+str(yesterday))
