import matplotlib.pyplot as plt 
from random_walk import RandomWalk 

while True:
	rw = RandomWalk(50000)
	rw.fill_walk()

	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values)

	plt.plot(0, 0)
	plt.plot(rw.x_values[-1], rw.y_values[-1])

	#plt.axes().get_xaxis().set_visible(False)
	#plt.axes().get_yaxis().set_visible(False)


	plt.show()
	plt.figure(figsize=(10, 6))

	keep_running = input("Do you want another walk? (y/n)")
	if keep_running == "n":
		break