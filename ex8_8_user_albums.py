def make_album(data, artist_name, album_title):
    """Return an artist album as a dictionary."""
    data['artist'].append(artist_name)
    data['album'].append(album_title)
    return data


album = {'artist': [], 'album': []}

while True:
    print("\nGive me your favorite artist and their album:")
    print("(enter 'q' at any prompt to exit)\n")

    name_artist = input('Artist Name: ')
    if name_artist == 'q':
        break

    name_album = input('Album Title: ')
    if name_album == 'q':
        break

    formatted_album = make_album(album, name_artist, name_album)
    print(formatted_album)
