def main():
    custName=inputCustName()
    custBal,balType=inputCustBalance()

    print('Custom name is: ',str(custName))
    print(f'customer balance: {custBal}',balType)

def inputCustName():
    name=input('Enter your name: ')
    return name

def inputCustBalance():
    custBal=float(input('Enter customer balance: '))
    if custBal>=0:
        balType='positive'
    else:
        balType='negative'
    return custBal,balType
main()