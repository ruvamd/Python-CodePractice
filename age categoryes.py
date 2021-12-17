ages=[12,9,25,17,35]
for age in ages:
    adult=age>17
    if not adult:
        print('being '+str(age)+' does not makes you an adult')