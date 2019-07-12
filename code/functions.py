def get_formatted_name(first_name, last_name):
	"""Returns neatly printed name"""
	full_name = first_name.title() + ' ' + last_name.title()
	return full_name

while True:
	print('\nPlease tell me your name: ')
	print("Press 'q'  anytime to quit")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("Hello " + formatted_name)



