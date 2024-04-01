import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
from pytube import YouTube
from pytube import Search

SAVE_PATH = r"C:\Users\Sonny\Downloads\Spotify_Downloads"
CLIENT_ID = "42f4851156894fd6b25c9118816ad740"
CLIENT_SECRET = "14f28b59723c4eebab2e8fd28cf28533"
REDIRECT_URI = "http://localhost:8888/callback"

spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope='user-library-read'))


def download_audio(yt_url, destination='.'):
    try:
        yt = YouTube(yt_url)
        video = yt.streams.filter(only_audio=True).first()
        if video:
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"{yt.title} has been successfully downloaded.")
        else:
            print(f"No audio streams found for {yt.title}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def get_liked_tracks(limit=5):
    liked_tracks = []
    results = spotify.current_user_saved_tracks(limit=limit)
    while results and len(liked_tracks) < limit:
        liked_tracks.extend(item['track'] for item in results['items'])
        if results['next'] and len(liked_tracks) < limit:
            results = spotify.next(results)
        else:
            break
    return liked_tracks[:limit]  # Ensure that only the top 5 tracks are returned


liked_tracks_url = []
tracks = get_liked_tracks()

for current_track in tracks:
    # ... Your existing code to get the YouTube URL for each track ...
    s = Search(current_track['name'] + '-' + current_track['artists'][0]['name'] + "audio")
    v = s.results[0]
    liked_tracks_url.append(v.watch_url)
    print(f"{v.title}\n{v.watch_url}\n")

# Use the download_audio function for each URL
for url in liked_tracks_url:
    download_audio(url, SAVE_PATH)



