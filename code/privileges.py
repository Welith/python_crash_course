from Users import *
class Admin(User):
	def __init__(self, first_name, last_name, age, location):
		super().__init__(first_name,last_name,age,location)
		self.privileges = Privileges()

class Privileges():
	def __init__(self, privileges = ['scan ban', 'can modify']):
		self.privileges = privileges

	def show_privileges(self):
		print("The admin can: ")
		for self.privilege in self.privileges:
			print(" -" + self.privilege)