'''
input
4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

output
[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''
import numpy as np
# arr1=np.array([[1,2,3],[4,5,6]])
# arr2=np.array([[0,0,0],[7,8,9]])

# a, b, c = map(int,input().split())
# arrA = np.array([input().split() for _ in range(a)],int)
# arrB = np.array([input().split() for _ in range(b)],int)
# print(np.concatenate((arrA, arrB), axis = 0))

nRow,mRow,pCol=map(int,input().split())
arrA = np.array([input().split() for _ in range(nRow)],int)
arrB = np.array([input().split() for _ in range(mRow)],int)

print(np.concatenate((arrA,arrB),axis=0))

'''
n, m, p = map(int, input().strip().split())
arr = np.array(input().strip().split(), int)
for i in range(1, n + m):
    arr = np.vstack((arr, np.array(input().strip().split(), int)))
print(arr)
'''