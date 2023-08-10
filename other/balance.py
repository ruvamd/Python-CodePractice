def main():
    custName=inputCustName()
    custBal,balType=inputCustBalance()
    
    print('Customer name = ',str(custName[0]))
    print(f'Customer balance = {custBal}',balType)

def inputCustName():
    name=input('Enter the customer name: ')
    nameParts=name.split()
    return nameParts

def inputCustBalance():
    custBalance=float(input('Enter customer balance: '))
    if custBalance>=0:
        balanceType=' Non-negative'
    else:
        balanceType='Negative'
    return custBalance,balanceType
main()