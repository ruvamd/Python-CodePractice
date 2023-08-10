from functools import reduce

numbers=[3,4,6,9,34,12]

def customSum(first,second):
    return first+second

result=reduce(customSum,numbers,10)
print(result)
