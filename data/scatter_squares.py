import matplotlib.pyplot as plt 

x_data = list(range(1,10001))
y_data = [x**2 for x in x_data]

plt.scatter(x_data, y_data, c = y_data, cmap = plt.cm.Blues,
 edgecolor = 'none', s=20)

plt.title("Square Numbers", fontsize = 10)
plt.xlabel("Value", fontsize = 10)
plt.ylabel("Square of Value", fontsize = 10)

plt.tick_params(axis = 'both', which = 'major', labelsize = 10)
plt.axis([0, 1100, 0, 1100000])

plt.show()