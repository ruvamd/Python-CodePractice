import numpy as np
#import re

#if bool(re.match(r'^\b([1-3])\b',inp)): #constrains
inp=tuple(map(int,input().split())) #enter 3 3 3
zero=np.zeros((inp),dtype=int)
one=np.ones((inp),dtype=int)
print(zero,one,sep='\n')

'''
result 
[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''