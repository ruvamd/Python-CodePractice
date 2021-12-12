import matplotlib.pyplot as plt
from random_walks import Random_walks

while True:
    rw=Random_walks()
    rw=Random_walks(50_00)
    rw.fill_walk()
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,9),dpi=128)
    point_numbers=range(rw.num_points)
    # ax.scatter(0,0,c='green',edgecolors='none',s=100)
    # ax.scatter(rw.x_val[-1],rw.y_val[-1],c='red',edgecolors='none',s=100)
    # ax.scatter(rw.x_val,rw.y_val,c=point_numbers,cmap=plt.cm.Blues,edgecolor='none',s=1)
    ax.plot(rw.x_val,rw.y_val,linewidth=2)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running=('make another walk?(y/n)')
    if keep_running=='n':
        break
