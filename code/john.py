import json


def get_stored_username():
	filename = 'username.json'

	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def get_new_username():
	username = input("What is your username: ")
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username)
		return username


def greet_user():
	username = get_stored_username()
	if username:
		correct = input("Are you " + username + "? (y/n)")
		if correct == 'y':
			print("Welcome back, " + username + '!')
		else:
			username = get_stored_username()
			print("We will remember you next time " + username + "!")


greet_user()