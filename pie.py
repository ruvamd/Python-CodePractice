import matplotlib.pyplot as plt 

labels='python','c++','java'
sizes=[33,52,12]
separated=(.1,0,0)

plt.pie(sizes,labels=labels,autopct='%1.1%%',explode=separated)
plt.axis('equal')

plt.show()