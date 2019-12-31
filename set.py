def main():
    a=set('qwerty')
    b=set('ytrewq')
    printSet(a&b)
def printSet(o):
    print('{',end='')
    for x in o:print(x,end='')
    print('}')
main()