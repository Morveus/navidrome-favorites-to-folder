import navidrome
from bs4 import BeautifulSoup 
import methods


starred_data = BeautifulSoup(navidrome.getStarred(), 'xml')

# Let's process artists first
artists = starred_data.find_all('artist')
for artist in artists:
    artist_id = artist.get('id')
    
    artist_directory = BeautifulSoup(navidrome.getMusicDirectory(artist_id), 'xml')
    artist_albums = artist_directory.find_all('child')

    for album in artist_albums:
        album_id = album.get('id')
        album_name = album.get('name')

        album_directory = BeautifulSoup(navidrome.getMusicDirectory(album_id), 'xml')
        album_tracks = album_directory.find_all('child')

        for track in album_tracks:
            track_id = track.get('id')
            track_title = track.get('title')
            track_path = track.get('path')

            print(track_id + ' ' + track_title + ' -> ' + methods.get_source_track_path(track_path))

# Then individual albums


# Then individual songs