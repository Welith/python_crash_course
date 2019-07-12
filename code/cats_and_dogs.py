try:
	cat_names = "cats.txt"


	with open(cat_names, 'r') as f_obj:
		contents = f_obj.read()
		



except FileNotFoundError:
	pass

else:
	words = contents.lower().count("the")
	print(words)
	
