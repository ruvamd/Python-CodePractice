#Basics
#1
mystring='string'
myinteger=5
myfloat=2.4

#2
addNum=2+myinteger
intSum=addNum
assert intSum #checking
print(intSum) 

#3
addFlNum=myfloat+3.2
flSum=addFlNum
assert flSum #checking
print(flSum) 

#4
addStr='yes'+'really'
strSum=addStr
assert strSum
print(strSum)

#5
addIntFl=myinteger+myfloat
intFlSum=addIntFl
assert intFlSum
print(intFlSum)

#6
'''
addNumStr=3+'str'

TypeError: unsupported operand type(s) for +: 'int' and 'str'
the string can't be addet with integer,because it's has different types.
'''
#Functions
#1
print(type(mystring))
print(type(myinteger))
print(type(myfloat))

#2
print(f'{myinteger}{mystring}')
#or
print(str(myinteger)+mystring)

#3
mult=5*7.654321
multSum=round(mult,3)
assert multSum #checking
print(multSum)

#4
myname=input('Enter your name: ')
print(myname)

#5
favorite_number=input('Enter your favorite number: ')
print(favorite_number)
print(type(favorite_number)) #the type of fav num is string

#6
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
addNmbs=num1+num2
print(addNmbs)