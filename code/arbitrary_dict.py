def build_profie(first_name, last_name, **user_info):

	"""Saves profile information"""

	profile = {}
	profile['name'] = first_name
	profile['surname'] = last_name
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profie('boris', 'kolev', location = 'princeton', ebanie = 'qko')
print(user_profile)