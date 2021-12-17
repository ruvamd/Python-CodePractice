data=[2,3,4,5,7,89,2,3,5,6,45,43,34,6]
target=5

def linearSearch(data,target):
    for i in range(len(data)):
        if data[i]==target:
            return True
    return False

def binarySearchIterative(data,target):
    low=0
    high=len(data)-1
    while low<=high:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            high=mid-1
    return False

def binarySearchRecursive(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target==data[mid]:
            return True
        elif target<data[mid]:
            return binarySearchRecursive(data,target,low,mid-1)
        else:
            return binarySearchRecursive(data,target,low,mid+1,high)

print(binarySearchIterative(data,target))
print(binarySearchRecursive(data,target,0,len(data)-1))

            