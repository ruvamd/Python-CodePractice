def func1():
    text='lekfekl'
    return text
print(func1())

def func2(arg1,arg2):
    print(arg1,'',arg2)
func2(1,2)

def cube(x):
    return x*x*x
print(cube(7))

def power(num,x=1):
    result=5
    for i in range(x):
        result=result*num
        return result
print(power(1))

def multiAdd(*arg):
    result=0
    for x in arg:
        result=result+x
    return result
print(multiAdd(4,3,5,6,7))