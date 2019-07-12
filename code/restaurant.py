class Restaurant():
	"""docstring for ClassName"""
	def __init__(self, restaurant_name, cuisine_type,number_served):
		"""Creating restaurant class"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

		"""Defining a function that
		describes a chosen restaurant
		"""
		print(self.restaurant_name.title() + 
			" offers " + self.cuisine_type.title() +
			" cuisine.")
	
	def open_restaurant(self):

		print(self.restaurant_name.title() + 
			" is open for bussines.")

	def get_number(self):
		print("This restaurant has served: " + 
			str(self.number_served) + " people.")

	def set_number(self, number):
		self.number_served = number

	def increment_number(self, new_number):
		self.number_served += new_number

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, restaurant_name,cuisine_type,number_served):
		
		super().__init__(restaurant_name,cuisine_type,number_served)
		


		




		