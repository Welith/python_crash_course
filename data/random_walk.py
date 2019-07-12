from random import choice

class RandomWalk():
	"""docstring for RandomWalkd"""
	def __init__(self, num_points = 5000):
		self.num_points = num_points

		self.x_values = [0]
		self.y_values = [0]


	def fill_walk(self):

		while len(self.x_values) < self.num_points:

			x = self.get_x()
			y = self.get_y()

			if x == 0 and y == 0:
				continue

			next_x = self.x_values[-1] + x
			next_y = self.y_values[-1] + y

			self.x_values.append(next_x)
			self.y_values.append(next_y)

	def get_x(self):
		x_direction = choice([1, -1])
		x_distance = choice([0, 1, 2, 3, 4])
		x_step = x_direction * x_distance

		return x_step

	def get_y(self):

		y_direction = choice([1, -1])
		y_distance = choice([0, 1, 2, 3, 4])
		y_step = y_direction * y_distance

		return y_step