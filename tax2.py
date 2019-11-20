country=input('what country do you live in? ')
if country.lower()=='canada':
    province=input('what province/state do you live in? ')
    if province in('alberta',\
        'nunavut','yukon'):
        tax=1
    elif province=='ontario':
        tax=2
    else:
        tax=3
else:
    tax=0
