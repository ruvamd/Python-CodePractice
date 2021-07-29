import numpy as np

nRow,mCol=map(int,input().split())
arr=np.array([input().split() for _ in range(nRow)],int)
arrSum=(np.sum(arr,axis=0))
arrProd=(np.prod(arrSum))

print(arrProd)