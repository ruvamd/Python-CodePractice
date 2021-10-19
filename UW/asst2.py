csv = "comma,separated,values"
print(csv.split(','))
psv = ''.join(csv.split(','))
psv == 'comma separated values'
print(psv)

sample = 'A long string of words'
a=sample.upper()
b=sample.lower()
c=sample.swapcase()
d=sample.title()
print(a,b,c,d,sep='\n')

print('this\nstring')

assert "this" "that" == 'thisthat'
print(ord('h'))
print(chr(104))
print(f"One third with 4 digits is: {1/3:.2}")

age=21

if age > 20:
   print("Older than 20")
elif age > 10:
   print("Older than 10")

if age > 20:
   print("Older than 20")
if age > 10:
   print("Older than 10")

import random
i=0
while i < 10:
   i += random.choice(range(4))
   print(i)

def fun(x=1, y=2, z=3):
    print(x, y, z)
print(fun(3))