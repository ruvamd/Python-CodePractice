employees=['a','b','c','d']
addEmployee=[]

def main():
    print('\nEmployee menu record\n')
    menu={1:'Search employee',2:'Add employee',3:'Delete employee',0:'Exit'}
    printDict(menu)
  
def printDict(m):
    for d in m:
         print(f'{int(d)}: {m[d]}')

    menuNum=-1
    while menuNum<0 or menuNum>3:
        menuNum = int(input('\nChose the right number: '))
        print('user made the right choice',menuNum)
main()