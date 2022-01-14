def doNum(n):
    print(n)
def catch():
    numList=(1,2,3,4,5)
    for i in range(20):
        try:
           doNum(numList[i])
        except IndexError:#put 0 when no range numbers after 5
           doNum(0)
catch()