x = 1
a = []
while (x <= 100):
         a.append(x)
         x+=1
#above code just makes a list of 1-100
for i in a:
    if (i%5==0 and i%4==0):
        print('GoFigure')
    elif (i%4==0):
        print('Go')
    elif (i%5==0):
        print('Figure')
    else:
        print(i)