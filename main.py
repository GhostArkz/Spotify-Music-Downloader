import spotipy
import pytube
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from pytube import YouTube
from pytube import Search

#SAVE_PATH = "C:\Users\Sonny\Downloads"
CLIENT_ID = "42f4851156894fd6b25c9118816ad740"
CLIENT_SECRET = "14f28b59723c4eebab2e8fd28cf28533"
REDIRECT_URI = "http://localhost:8888/callback"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope='user-library-read'))


def get_liked_tracks():
    liked_tracks = []
    results = spotify.current_user_saved_tracks()
    while results:
        liked_tracks.extend([item['track'] for item in results['items']])
        if results['next']:
            results = spotify.next(results)
        else:
            break
    return liked_tracks


#def search_liked_tracks():






tracks = get_liked_tracks()
for current_track in tracks:
    s = Search(current_track['name'])
    v = s.results[0]
    print(f"{v.title}\n{v.watch_url}\n")

    """try:
        tracks = get_liked_tracks()
        for track in tracks:
            print(track['name'], '-', track['artists'][0]['name'])
    except Exception as e:
        print(f"An error occurred: {e}")"""