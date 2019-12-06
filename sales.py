def main():
    salesPrice=int(input('Enter sales price: '))
    daysOnMarket=int(input('Enter days on market: '))
    daysToClosing=int(input('Enter days to closing: '))
    
    if salesPrice<=400000:
        commissionPct=0.1
    elif salesPrice<=600000:
         commissionPct=0.09
    elif salesPrice<=1000000:
        commissionPct=0.08
    else: 
        commissionPct=0.07

    closingPct=0.0
    if daysOnMarket<=7:
        daysPct=0.0025
        if daysToClosing<=30:
            closingPct=0.0025
    elif daysOnMarket<=30:
        daysPct=0.0
    elif daysOnMarket<=180:
        daysPct=0.0
    else:
        daysPct=-0.001
    
    commision= int(salesPrice*commissionPct)\
              +int(salesPrice*daysPct)      \
              +int(salesPrice*closingPct)
    print('Commission will be $',format(commissionPct, ',.0f'),sep='')
main()

  