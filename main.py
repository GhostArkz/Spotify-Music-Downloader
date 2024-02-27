import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID="325bc3e94f254412bd70845484e833bc"
CLIENT_SECRET="2a7f2ec13d6e4722bfef01313f87e705"

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(CLIENT_ID, CLIENT_SECRET))

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])