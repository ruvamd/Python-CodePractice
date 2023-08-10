from functools import reduce

myFloats=[4.35,6.09,3.25,9.77,2.16,8.88,4.59]
myNames=['olumide','akinremi','josiah','temidayo','omoseun']
myNumbers=[4,6,9,23,5]

mapResult=list(map(lambda x: round(x** 2,3), myFloats))
filterResult=list(filter(lambda name:len(name) <=7,myNames))
reduceResult=reduce(lambda num1,num2:num1*num2,myNumbers)

print(mapResult)
print(filterResult)
print(reduceResult)