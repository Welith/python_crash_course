class Dog():
	"""docstring for Dog"""
	def __init__(self, name, age):
		"""Initialize class"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a sit command"""
		print(self.name.title() + " is now sitting.")

	def roll(self):
		"""Stimulate rolling"""
		print(self.name.title() + " rolled over.")


class Cats(Dog):
	"""Represents cats"""
	def __init__(self,name,age):
		super().__init__(name,age) #makes connection between paren and child
		self.breed = breeds()



	def roll(self):
		print("Cats don't roll.")
		pass

class breeds():
	"""docstring for breeds"""
	def __init__(self, breed = "English"):
		self.breed = breed

	def  describe_breed(self):
		print("The cat is: " + self.breed.title())
		pass


my_cat = Cats('beni',5)
my_cat.roll()
my_cat.breed.describe_breed()

my_dog = Dog("sharo", 6)
your_dog = Dog("Vanio", 12)
my_dog.sit()
my_dog.roll()

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

your_dog.sit()
your_dog.roll()

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
		