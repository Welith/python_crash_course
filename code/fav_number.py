import json

filename = 'favnumber.json'
favnumber = input("Enter your favourite number: ")
with open(filename, 'w') as f_obj:
	json.dump(favnumber, f_obj)
