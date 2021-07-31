import numpy as np

n=int(input())#enter: 2
a=np.array([input().split() for _ in range(n)],float)#enter:# 1.1 1.1
                                                            # 1.1 1.1
                                                        
print(np.linalg.det(a))
# output: 0.0