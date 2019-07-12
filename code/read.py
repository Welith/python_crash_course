import json

def get_number():
	filename = 'favnumber.json'
	try:
		with open(filename) as f_obj:
			favnumber = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return favnumber

def store_new_number():
	filename = 'favnumber.json'
	favnumber = input("Enter your favourite number: ")
	with open(filename, 'w') as f_obj:
		json.dump(favnumber, f_obj)
		return favnumber

def tell_number():
	favnumber = get_number()
	if favnumber:
		print("Your number is " + favnumber)
	else:
		favnumber = store_new_number()
		print("We will remember the number: ")

tell_number()
store_new_number()
tell_number()