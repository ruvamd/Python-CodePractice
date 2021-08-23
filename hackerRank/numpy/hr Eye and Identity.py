import numpy as np
#np.set_printoptions(legacy='1.13')

nRows,mCol=map(int,input().split()) #enter: 3 3
print(str(np.eye(nRows,mCol))) #result:[[1. 0. 0.]
                                      # [0. 1. 0.]
                                      # [0. 0. 1.]]
