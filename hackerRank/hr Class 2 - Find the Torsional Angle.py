#not finished
# x,y,z=[map(float,input().split())for i in range(4)]
# print(x,y,z)
#
from math import acos, pi
p = []
for i in range(4):
    p.append(list(map(float, input().split())))
def cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2],  x[0] * y[1] - x[1] * y[0]]
def dot(x, y):
    return sum([x[i] * y[i] for i in range(len(x))])
def length(x):
    return sum([a * a for a in x]) ** 0.5
def minus(x, y):
    return [x[i] - y[i] for i in range(len(x))]
X = cross(minus(p[1], p[0]), minus(p[2], p[1]))
Y = cross(minus(p[2], p[1]), minus(p[3], p[2]))
print("%.2f" % (acos(dot(X, Y) / length(X) / length(Y)) / pi * 180))