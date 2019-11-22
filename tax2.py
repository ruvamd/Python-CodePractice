country=input('what country do you live in? ')

if country.lower() == 'canada':
    province=input('what province/state do you live in? ')
    if province in ('alberta',\
         'nunavut','yukon'):
          tax = 0.5
    elif province=='ontario':
          tax = 0.15
    else:
          tax = 0.16
       
else:
    tax = 0
    
