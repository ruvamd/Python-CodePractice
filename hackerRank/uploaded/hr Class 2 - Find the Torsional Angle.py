'''from math import acos,pi
p = []
for i in range(4):
    p.append(list(map(float,input().split()))) #enter: 0 4 5
                                                     # 1 7 6
                                                     # 0 5 9
                                                     # 1 7 2
def cross(x, y):
    return [x[1]*y[2]-x[2]*y[1],
            x[2]*y[0]-x[0]*y[2],
            x[0]*y[1]-x[1]*y[0]]
def dot(x,y):
    return sum([x[i]*y[i] for i in range(len(x))])
def length(x):
    return sum([a*a for a in x])**0.5
def minus(x, y):
    return [x[i]-y[i] for i in range(len(x))]
X=cross(minus(p[1],p[0]),minus(p[2],p[1]))
Y=cross(minus(p[2],p[1]),minus(p[3],p[2]))
print("%.2f"%(acos(dot(X,Y)/length(X)/length(Y))/pi*180))
#output: 8.19'''

import math

class Points(object):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __sub__(self,no):
        x=self.x-no.x
        y=self.y-no.y
        z=self.z-no.z
        return Points(x,y,z)
    def dot(self,no):
        x=self.x*no.x
        y=self.y*no.y
        z=self.z*no.z
        return x+y+z
    def cross(self,no):
        x=self.y*no.z-self.z*no.y
        y=self.z*no.x-self.x*no.z
        z=self.x*no.y-self.y*no.x
        return Points(x,y,z)
    def absolute_scale(self):
        return pow((self.x**2+self.y**2+self.z**2),.5)
def solve(A,B,C,D):
    A,B,C,D=Points(*A),Points(*B),Points(*C),Points(*D)
    X=(B-A).cross(C-B)
    Y=(C-B).cross(D-C)
    angle=math.acos(X.dot(Y)/(X.absolute_scale()*Y.absolute_scale()))
    print("%.2f"%math.degrees(angle))
points=list()
for i in range(4):
    a = map(float,input().split())
    points.append(a)
solve(*points)