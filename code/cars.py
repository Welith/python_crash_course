filename = "text.txt"

with open(filename) as f_obj:
	text = f_obj.readlines()
text_string = ''
for line in text:
	text_string += line.rstrip()
	print(text_string)