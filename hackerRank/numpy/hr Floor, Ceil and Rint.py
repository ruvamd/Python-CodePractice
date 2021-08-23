import numpy as np
np.set_printoptions(legacy='1.13')

arr=np.array(input().split(),float) #enter: 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
print(np.floor(arr),np.ceil(arr),np.rint(arr),sep='\n')

'''
output:
[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''