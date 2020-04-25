dietRestrictions=set(['meat','cheese'])

if 'meat' and 'cheese' in dietRestrictions:
    print('Get a vegan pizza.')
elif 'meat' in dietRestrictions:
    print('Get a cheese pizza.')
else:
    print('Get something else.')