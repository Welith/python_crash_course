from random import randint
class Die():
	def __init__(self, sides = 20):
		self.sides = sides

	def roll_die(self):
		rand = randint(1, self.sides)
		print(rand)

my_die = Die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()
my_die.roll_die()

