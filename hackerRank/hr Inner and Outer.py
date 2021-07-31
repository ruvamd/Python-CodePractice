import numpy as np

# a=np.array(input().split(),int)
# b=np.array(input().split(),int)
a,b=[np.array(input().split(),int) for _ in range(2)] #enter: 0 1
                                                             #2 3  
print(np.inner(a,b),np.outer(a,b),sep='\n')

'''
output: 3
        [[0 0]
        [2 3]]
'''