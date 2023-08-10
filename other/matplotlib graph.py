import matplotlib.pyplot as plt 

years=[1950,1955,1960,1965]
pops=[2,3,4,5]

plt.plot(years,pops,color=(255/255,100/255,100,255))

plt.ylabel('population in billions')
plt.xlabel('population growth by year')

plt.title('populatin growth')
plt.show()