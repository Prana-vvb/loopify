import os
import spotipy
import time

from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.getenv('SPOTIFY_CLIENT_ID'), 
                                               client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
                                               redirect_uri='http://localhost:3000/callback', 
                                               scope='user-modify-playback-state user-read-playback-state'))

playback = sp.current_playback()
print(playback)

loop_start = 98 # enter start time in seconds
loop_end = 126  # enter end time in seconds

while True:
    playback = sp.current_playback()
    if playback:
        current_position = playback['progress_ms'] / 1000  
        if current_position >= loop_end:
            sp.seek_track(loop_start * 1000)  
    time.sleep(1)  