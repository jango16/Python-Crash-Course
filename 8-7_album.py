def make_album(artist_name, album_title, num_of_songs=None):
    """returns a dict of info about an album"""
    album = {'name': artist_name, 'album': album_title}
    if num_of_songs:
        album['Number of Songs'] = num_of_songs
    return album


artist = {
    'The Beatles': 'Abbey Road',
    'Led Zeppelin': 'Led Zeppelin IV',
    'Kendrick Lamar': 'GNX'
}

for artist_name, album_title in artist.items():
    album_made = make_album(artist_name, album_title)
    if artist_name == 'The Beatles':
        album_made = make_album(artist_name, album_title, num_of_songs=14)
    print(album_made)
