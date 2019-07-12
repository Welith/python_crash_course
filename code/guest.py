class Restaurant():
	"""A class representing restaurants"""
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""A function describing a restaurant"""
		print("\nThe " + self.restaurant_name.title() + " has " 
			+ self.cuisine_type.title() + " cuisiune")

	def set_number_served(self, customers):
		self.number_served = customers

	def increment_served(self, customer):
		self.number_served += customer

	def customers_served(self):
		print("This restaurant has served: " + str(self.number_served))

	def restaurant_open(self):
		"""A funciton indicating that a restaurant is open"""
		print(self.restaurant_name.title() + " is open !")

class IceCream(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.flavours = []

	def show_flavour(self):
		print("The ice-cream stand " + self.restaurant_name.title()
		+ " offers: ")
		for self.flavour in self.flavours:
			print("\n - " + self.flavour.title())



