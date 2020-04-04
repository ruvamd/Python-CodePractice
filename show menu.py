def showMenu():
    print('Employee menu record')
    print()
    print('1.Search employee')
    print('2.Add employee')
    print('3.Delete employee')
    print('0.Exit')
    print()
    menuNum=-99
    while menuNum<0 or menuNum>3:
        menuNum = int(input('Chose the right number: '))
    print('user made the right choice',menuNum)
showMenu()