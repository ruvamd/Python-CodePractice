def totalEmplHours():
    totalEmplHours=0
    emplNum=input('Enter employee # or x to exit: ')
    while emplNum!='x':
        emplHours=float(input('Enter employee hours: '))
        totalEmplHours+=emplHours
        emplNum=input('Enter employee # or x to exit: ')
    print('Total employee hours --> ',totalEmplHours)
totalEmplHours()