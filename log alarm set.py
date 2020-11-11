'''
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, 
and a boolean indicating if we are on vacation, return a string of 
the form "7:00" indicating when the alarm clock should ring. Weekdays, 
the alarm should be "7:00" and on the weekend it should be "10:00". 
Unless we are on vacation -- then on weekdays it should be "10:00" and 
weekends it should be "off".
'''
def alarm_clock(day, vacation):
    pronto = "7:00" if not vacation else "10:00"
    tarde = "10:00" if not vacation else "off"
    return pronto if day not in [6,0] else tarde

#alternative code
    # weekday=day in range(1,6)
    # weekend=day in [6,0]
    # if weekday and not vacation:
    #     return '7:00'
    # elif weekend and not vacation:
    #     return '10:00'
    # elif weekday and vacation:
    #     return '10:00'
    # elif weekend and vacation:
    #     return 'off'

print(alarm_clock(1, False)) #→ '7:00'
print(alarm_clock(5, False)) #→ '7:00'
print(alarm_clock(0, False)) #→ '10:00'