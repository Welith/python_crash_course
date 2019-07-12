magician_name = ["trevor ", "abra kadabra ", 'hui']
def show_magicians(magician_name):
	for magician in magician_name:
		print("Hello " + str(magician))

def make_great(magician_name):
	magician = [current_magician + ' the Great' for current_magician in magician_name]
	magician_name.append(magician)



make_great(magician_name)
show_magicians(magician_name)
