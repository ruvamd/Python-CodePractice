def main():
    sampleNumber=[7,2,4,1,3]

    print('Original list: ',sampleNumber)
    selectionSort(sampleNumber)
    print('Sorted list: ',sampleNumber)

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
