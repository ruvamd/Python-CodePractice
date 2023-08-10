for number in range(1,101):
    if number%4==0 and number%5==0:
        print('GoFigure')
        continue
    elif number%4==0:
        print('Go')
        continue
    elif number%5==0:
        print('Figure')
        continue
    print(number)