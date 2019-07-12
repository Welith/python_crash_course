from die import Die 
import pygal

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(10000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_side + die_2.num_side
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(results)
print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling two dies 10000 times"
hist.x_labels = range(2, max_result+1)
hist.x_title = 'Result'
hist.y_title = 'Frequency'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')