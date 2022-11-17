import navidrome
from bs4 import BeautifulSoup 
import favstofold
import shutil
import os

def process_artist(artist):
    artist_id = artist.get('id')
    
    artist_directory = BeautifulSoup(navidrome.getMusicDirectory(artist_id), 'xml')
    artist_albums = artist_directory.find_all('child')

    for album in artist_albums:
        process_album(album)

def process_album(album):
    album_id = album.get('id')
    album_name = album.get('name')

    album_directory = BeautifulSoup(navidrome.getMusicDirectory(album_id), 'xml')
    album_tracks = album_directory.find_all('child')

    for track in album_tracks:
        process_track(track)

def process_track(track, single = False):
    track_id = track.get('id')
    track_title = track.get('title')
    track_path = track.get('path')
    track_artist = track.get('artist')
    track_album = track.get('album')

    if(not favstofold.destination_identical(track_path)):
        filename = os.path.split(track_path)[1]
        splitext = os.path.splitext(track_path)
        extension = splitext[1]

        additional_info = "..."
        if(single):
            additional_info = " as a single track..."
            filename = track_artist + " - " + track_album + " - " + track_title + extension

        print("Copying " + track_artist + " - " + track_title + additional_info)
        favstofold.copy_track(track_path, single, filename)

print("Navidrome Favorites to Folder // morveus[at]morveus.com")

print("Connecting to Navidrome and getting Starred <3 content...")
starred_data = BeautifulSoup(navidrome.getStarred(), 'xml')
print("Got the list.")

# Let's process artists first
print("Processing artists...")
artists = starred_data.find_all('artist')
# for artist in artists:
#     process_artist(artist)
print("Done with the artists.")


# Then individual albums
print("Processing albums...")
albums = starred_data.find_all('album')
for album in albums:
    process_album(album)
print("Done with the albums.")

# Then individual songs
print("Processing single tracks...")
tracks = starred_data.find_all('song')
for track in tracks:
    process_track(track, True)
print("Done with the single tracks.")

print("Done with this session.")