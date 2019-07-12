file_name = 'guest.txt'

with open(file_name, 'a') as file_object: #append lets me write without overwriting
	append = True	
	while append:
		user = input("write your name :")
		file_object.write(user)
		if user == 'q':
			break
	
