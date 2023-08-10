from collections import namedtuple as nt

point=nt('point',['x','y'])
p=point(11,y=22)
sum=p[0]+p[1]
x,y=p
coordinates=p.x+p.y

print(p)
print(coordinates)
print(x,y)
print(sum)
