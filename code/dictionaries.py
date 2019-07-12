alien_0 = {'color' : 'green' , 'points' : 5}
player_points = alien_0['points']
#print("You just scored " + str(player_points) + "pts")
alien_0['x-position'] = 0
alien_0['y-position'] = 25
#print(alien_0)
alien_0['speed'] = 'medium'
print("Original x-position is: " + str(alien_0['x-position']))
 #We want to move the alien based in speed
if alien_0['speed'] == 'slow':
 	x_increment = 1
elif alien_0['speed'] == 'medium':
 	x_increment = 2
else:
 	x_increment = 3
alien_0['x-position'] = alien_0['x-position'] + x_increment
print("The new x-position is: " + str(alien_0['x-position']))
del alien_0['color']
#print(alien_0)

fav_language = {
	'borko' : 'Python',
	'mimi' : 'English',
	'pepi' : 'Bulgarian'
	}
##
personal_info = {
	'first_name' : 'boris',
	'last_name' : 'kolev',
	'age' : '22',
	'nationality' : 'bulgarian' 
	}
print(personal_info)

##
dictionary = {
	'list' : 'creates a list of information',
	'tuple' : 'creates a list that has constant values',
	'if-loop' : 'creates  a conditional statement'
	}
dictionary['kenef'] = 'mqsto za srane'
dictionary['laino'] = 'ekskremnt'
#print("A list " + str(dictionary['list'])) 
#print("A tuple " + str(dictionary['tuple'])) 
#print("A if-loop " + str(dictionary['if-loop']))

#statements = ['creates a list of information', 'creates a list that has constant values']
for word, meaning in sorted(dictionary.items()):
	print(word.title() + ' ' + meaning.title())
##
rivers = {'bulgaria' : 'dunav', 
	'egypt' : 'nile'
	}
for river in rivers.values():
	print ("The " + river.title() + ' runs through ')

##
aliens = []

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'fast'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color']=='green':
		alien['color']='yellow'
		alien['points']='10'
		alien['speed']='medium'
for alien in aliens[0:5]:
	print(alien)
##

dogs = {'cherno' : 'huski', 'bqlo' : 'labrador'}
cats = { 'siva' : 'britanka', 'sharena' : 'ulichna'}
animals = [dogs, cats]
for animal in animals:
	print(animal)

##
cities = {
	'vraca' : {
			'population' : '35000',
			'fact' : 'krasiv'
			},
	'sofiq' : {
			'population' : '2000000',
			'fact' : 'stolica'
			}
	}
for city, city_info in cities.items():
	print("\nGrad: " + city.title())
	population = city_info['population']
	info = city_info['fact']

	print("\tGradut ima populcaciq: " + str(population))
	print("\tGradut e: " + info)





























	
	