import datetime as dt
from datetime import datetime as dts, timedelta
from datetime import date,time 

today=date.today()
# today_day=today.day

delta=dt.timedelta(days=3)

limit=today+delta
limit_day=limit.day

# ent='12/09/2021'
ent=input()
ent_s_d=dts.strptime(ent,'%m/%d/%Y')
ent_day=ent_s_d.day

if ent_day<limit_day:
    print('urgent')
else:
    print('not urgent:truck,ocean')

# print(today_day)
# print(limit_day)
# print(ent_day)



