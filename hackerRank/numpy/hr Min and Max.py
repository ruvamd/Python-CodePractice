import numpy as np

nRow,mCol=map(int,input().split()) #enter: 4 2
arr=np.array([input().split() for _ in range(nRow)],int)
# arrMin=(np.min(arr,axis=1))
# arrMax=(np.max(arrMin))
print(np.max(np.min(arr,axis=1)))
#print(arrMax)

'''
output
2 5
3 7
1 3
4 0
'''