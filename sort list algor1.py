def main():
    sampleNumbers=[5,4,9,8,2]
    print('The unsorted list ',sampleNumbers)
    selectionSort(sampleNumbers)
    print('Sorted list: ',sampleNumbers)
def selectionSort(aList):
    for passes in range(len(aList)-1):
        smallIndex=passes
        for checkIndex in range(passes+1,len(aList)):
            if aList[checkIndex]<aList[smallIndex]:
                smallIndex=checkIndex
        if passes!=smallIndex:
            temp=aList[passes]
            aList[passes]=aList[smallIndex]
            aList[smallIndex]=temp
main()
