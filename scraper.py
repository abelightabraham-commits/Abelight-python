import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


fig, ax = plt.subplots()
#ax.plot(input_values, squares, linewidth=3)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=5)

#set chart title and label axis.
ax.set_title('Square Number', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square Value', fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', labelsize=13)

#set range
ax.axis([0, 1100, 0, 1100000])

plt.show()