#while and if loops 

a=int(input('enter the number for a: '))
b=int(input('enter the number for b: '))
while a>b:
    b+=1
    print(b)
while a<b:
    a+=1
    print(a)
if a==b:
    print('a and b are equal')