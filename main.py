import os
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

id = os.getenv('SPOTIFY_CLIENT_ID')
secret = os.getenv('SPOTIFY_CLIENT_SECRET')
url = 'http://localhost:3000/callback',
scope = 'user-modify-playback-state user-read-playback-state'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=id,
                                               client_secret=secret,
                                               redirect_uri=url,
                                               scope=scope))

playback = sp.current_playback()
print(playback)

loop_start = 98  # Enter start time in seconds
loop_end = 126  # Enter end time in seconds

while True:
    playback = sp.current_playback()
    if playback:
        current_position = playback['progress_ms'] / 1000
        if current_position >= loop_end:
            sp.seek_track(loop_start * 1000)
    time.sleep(1)
