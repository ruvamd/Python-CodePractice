items=[20,6,8,53,56,23,87,41,49,19]

def quickSort(dataset,first,last):
    if first<last:
        pivotIdx=partition(dataset,first,last)
        quickSort(dataset,first,pivotIdx-1)
        quickSort(dataset,pivotIdx+1,last)
def partition(datavalues,first,last):
    pivotvalue=datavalues[first]
    lower=first+1
    upper=last
    done=False
    while not done:
        while lower<=upper and datavalues[lower]<=pivotvalue:
            lower +=1
            while datavalues[upper]>=pivotvalue and upper>=lower:
                upper-=1
            if upper<lower:
                done=True
            else:
                temp=datavalues[lower]
                datavalues[lower]=datavalues[upper]
                datavalues[upper]=temp
    temp=datavalues[first]
    datavalues[first]=datavalues[upper]
    datavalues[upper]=temp
    return upper
print(items)
quickSort(items,0,len(items)-1)
print(items)
