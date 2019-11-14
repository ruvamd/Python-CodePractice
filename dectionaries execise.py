phonebook={
    'ho':3646473,
    'ha':3644778,
    'hi':7364848
}
phonebook['jake']=3736484
del phonebook['hi']

if 'jake' in phonebook:
    print('jake is listed in phonebook.')
if 'hi' not in phonebook:
    print('hi is not listed in phonebook')