from datetime import datetime

def printTime(taskName):
    print(taskName)
    print(datetime.now())
    print()
firstName='susan'
printTime('first name assigned')

for x in range(0,10):
    print(x)
printTime('loop completed')

