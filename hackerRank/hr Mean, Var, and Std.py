import numpy as np

nRow,mCol=map(int,input().split()) #enter: 2 2
arr=np.array([input().split() for _ in range(nRow)],int) #enter:1 2
                                                               #3 4

arrMean=(np.mean(arr,axis=1))
arrVar=(np.var(arr,axis=0))
arrStd=(np.std(arr))
rnd=np.around(arrStd,11)
print(arrMean,arrVar,rnd,sep='\n')

'''
output:
[1.5 3.5]
[1. 1.]
1.11803398875
'''