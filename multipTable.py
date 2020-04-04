def multTable(maxNum):
    for row in range(1,maxNum+1):
        for col in range(1,maxNum+1):
            print(format(row*col,'5d'),end='')
        print()
multTable(12)
