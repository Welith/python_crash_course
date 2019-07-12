def make_album(artist_name, album_title, number_tracks = ''):
	##Returning a neattly formated album
	album = {'artis': artist_name, 'album': album_title}
	if number_tracks:
		album['tracks'] = number_tracks
	return album

while True:
	print('\nEnter your favourite artist and album: ')
	print('Press q if you want to quit')
	artist = input("Artist name: ")
	if artist == 'q':
		break
	a_name = input("Album name: ")
	if a_name == 'q':
		break
	number = input('Specify the number of tracks or press n to cancel or q to quit')
	if number == 'n':
		continue
	if number == 'q':
		break

	specific_album = make_album(artist, a_name, number)
	print(specific_album)


