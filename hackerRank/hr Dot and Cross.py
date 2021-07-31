import numpy as np

n=int(input()) #enter: 2
#a,b=(np.array([input().split() for i in range(n)],int) for i in range(2)) #short solution
a=np.array([input().split() for _ in range(n)],int) #enter: 1 2
b=np.array([input().split() for _ in range(n)],int)        #3 4
                                                           #1 2
print(np.dot(a,b),sep='\n')                                #3 4
'''
output:
[[ 7 10]
 [15 22]]
'''