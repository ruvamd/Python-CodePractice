x=(1,'two',3.0,[4,'four'],5)
y=(1,'two',3.0,[4,'four'],5)

print(f'x is {x}')
print(f'y is {y}')
print(id(x[0]))
print(id(y[0]))

if x is y:
    print('yep')
else:
    print('nope')
