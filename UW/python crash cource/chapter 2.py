a,b,c=0,1,2
print(a,b,c)

print(5+3,9-1,2*4,round(16/2),sep='\n')

f=5
message=f'this is my fav number: {f}'
print(message)

#lists
a=['a','b','c','d']
message='this is '

while True:
    name=input('enter name:')
    if name=='a':
        print(a[0].title())
    elif name=='b':
        print(a[1].title())
    elif name=='c':
        print(a[2].title())
    elif name=='d':
        print(a[3].title())
        break
    else:print('letters from a-d')

# print(f'{message}{a[0]}')
# print(f'{message}{a[1]}')
# print(f'{message}{a[2]}')
# print(f'{message}{a[3]}')