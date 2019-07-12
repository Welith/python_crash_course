def make_pizza(size, *toppings): #arbitrary data
	"""Print number of toppings"""
	print("\nMaking a " + str(size) + "-inch pizza with the following:")
	for topping in toppings:
		print('- ' + topping.title())

