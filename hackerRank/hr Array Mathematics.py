import numpy as np

nRow,mCol=map(int,input().split()) #1 4
a,b=(np.array([input().split()for _ in range(nRow)],dtype=int) for _ in range(2))

print(a+b,a-b,a*b,a//b,a%b,a**b,sep='\n')

'''
output
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
'''