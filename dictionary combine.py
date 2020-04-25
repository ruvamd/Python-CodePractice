def main():
    abc={'a':1,'b':2,'c':3}
    printDict(abc)
def printDict(o):
    for x in o:print(f'{x}: {o[x]}')
main()