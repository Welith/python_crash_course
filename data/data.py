import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth = 5)

plt.title('Square Numbers', fontsize = 24)
plt.xlabel('Value', fontsize = 24)
plt.ylabel('Squared value', fontsize = 24)

plt.tick_params(axis = 'single', labelsize = 8)

plt.show()

