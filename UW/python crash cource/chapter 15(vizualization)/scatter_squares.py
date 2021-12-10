import matplotlib.pyplot as plt

# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]
x_values=range(1,1001)
y_values=[x**2 for x in x_values]

plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)

# ax.scatter(2,4,s=200)
ax.set_title('square numbers',fontsize=24)
ax.set_xlabel('value',fontsize=14)
ax.set_ylabel('square of value',fontsize=14)

ax.tick_params(axis='both',labelsize=14)
ax.axis([0,1100,0,1100000])

plt.show()
# plt.savefig('squares_plot.png',bbox_inches='tight')