def print_models(unprinted_design, completed_models):
	"""
	Simulate printing and move models to completed
	"""
	for current_design in unprinted_design:
		current_design = unprinted_design.pop()
		print('Printing the following models: ' + current_design)
		completed_models.append(current_design)

def show_completed(completed_models):
	"""
	Show completed design
	"""
	print('The following models have been printed')
	for complete in completed_models:
		print(complete)






	