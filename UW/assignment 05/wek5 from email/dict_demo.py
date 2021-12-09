
my_customers = [
    ('01',
     'XYZ abc',
     42.09,
     ),
    ('02',
     'TR deep',
     90.01
     )
]


my_other_customers = [
    {'ID': '01',
     'Name': 'XYZ abc',
     'Credit': 42.09
     },
    {'ID': '02',
     'Name': 'TR deep',
     'Credit': 90.01
     }
]

mydict = {'ID': '01',
     'Name': 'XYZ abc',
     'Credit': 42.09
}

assert mydict['Credit'] == 42.09
