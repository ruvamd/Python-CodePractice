import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np

# x=[1,2,3,4,5]
x=range(1,5000)
w=[i**3 for i in x]
# print(w)

fig,ax=plt.subplots()
ax.scatter(x,w,c=w,cmap=plt.cm.Blues,s=10)
ax.plot(w)
plt.show()

