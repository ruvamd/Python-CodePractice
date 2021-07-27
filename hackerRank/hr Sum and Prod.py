import numpy as np

arr=np.array(map(int,input().split()))
#arr=np.array([[1,2],[3,4]])
print(np.sum(arr,axis=0),np.sum(arr,axis=1),np.sum(arr,axis=None),np.sum(arr))
print(np.prod(arr,))