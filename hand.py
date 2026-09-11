import matplotlib.pyplot as plt
import seaborn as sns
from pratice import RandomWalk


sns.set_style('darkgrid')

while True:

        
        rw = RandomWalk(50_000)
        rw.fill_walk()

        #Plot the points in the walks.
        fig, ax = plt.subplots(figsize=(15, 9))
        point_number = range(rw.num_points)
        ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Blues, edgecolors='none', s=15)

        #Emphasize the first and last points.
        ax.scatter(0, 0, c='green', edgecolors='none', s=100)
        ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

        #Remove the axis.
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    
    

        plt.show()

        keep_running = input('make another walk? (y/n): ')
        if keep_running == 'n':
                break
