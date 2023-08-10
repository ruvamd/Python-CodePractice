country=input('what country do you live in? ')

if country.lower() == 'canada':
    province=input('what province/state do you live in? ')
    if province in ('alberta',\
         'nunavut','yukon'):
          tax = 0.5
          print(f'the tax is {tax}')
    elif province=='ontario':
          tax = 0.15
          print(f'the tax is {tax}')
    else:
          tax = 0.16
          print(f'other than alberta,nunavut,yukon,ontario provinces tax is {tax}')       
else:
    tax = 0