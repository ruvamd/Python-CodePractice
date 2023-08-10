#constants
pie_price=17.99
cake_price=24.99
tax_rate=0.095

def main():
    numPies,numCakes=inputOrderData()
    piePrice,cakePrice,orderSubtotal,orderTax,orderTotal=priceOrder(numPies,numCakes)
    dispSum(numPies,numCakes,piePrice,cakePrice,orderSubtotal,orderTax,orderTotal)

#input
 #inputs order data from the user
def inputOrderData():
    pieCount=int(input('How many pies do you want?'))
    cakeCount=int(input('How many cakes do you want?'))
    return pieCount,cakeCount

#calculation
 #prices the order
def priceOrder(pieCount,cakeCount):
    pieTotal=pricePies(pieCount)
    cakeTotal=priceCakes(cakeCount)
    subTotal=pieTotal+cakeTotal
    tax=calcTax()
    total=tax()
    return pieTotal,cakeTotal,subTotal,tax,total
 #prices the pies in an order
def pricePies(pieCount):
    pieTotal=pieCount*pie_price
    return pieTotal
 #prices the cakes in an order
def priceCakes(cakeCount):
    cakeTotal=cakeCount*cake_price
    return cakeTotal
 #calculates the tax on an order
def calcTax(subTotal):
    tax=round(subTotal*tax_rate,2)
    return tax
 #calculates the total price of an order
def calcTotal(subTotal,tax):
    total=subTotal+tax
    return total

#output
def dispSum(numPies,numCakes,piePrice,cakePrice,subTotal,tax,total):
    print(numPies,numCakes,piePrice,cakePrice,subTotal,tax,total)
main()