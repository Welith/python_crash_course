from random import randint
class Die():
	def __init__(self, sides):
		self.sides = sides

	def roll_die(self):
		x = randint(1, self.sides)
		print(x)

dice = Die(10)
dice.roll_die()


