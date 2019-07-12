class User():
	def __init__(self, first_name, last_name, age, location):
		"""A class represint a user database"""
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.location = location
		self.login_attempt = 0

	def describe_user(self):
		print(self.first_name.title() + " " + self.last_name.title()
			+ " is " + self.age + " and lives in "
			+ self.location.title()
			)

	def greet_user(self):
		print("Hello " + self.last_name.title())

	def increment_login(self):
		self.login_attempt += 1

	def reset_login(self):
		self.login_attempt = 0





