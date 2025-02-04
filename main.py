import os
import sys
import time
import spotipy
import argparse
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


def getArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument('-s', '--start',
                        help='''Specify song start time in seconds (Default=0).
                        Syntax: [--start <time>], [-s <time>]''',
                        default=0, type=int)
    parser.add_argument('-e', '--end',
                        help='''Specify song end time in seconds.
                        Syntax: [--end <time>], [-e <time>]''',
                        default=None, type=int)

    return parser.parse_args()


def getClient():
    load_dotenv()

    id = os.getenv('SPOTIPY_CLIENT_ID')
    secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    url = 'http://localhost:3000/callback'
    scope = 'user-modify-playback-state user-read-playback-state'

    auth = SpotifyOAuth(client_id=id,
                        client_secret=secret,
                        redirect_uri=url,
                        scope=scope)

    return spotipy.Spotify(auth_manager=auth)


def main():
    args = getArgs()
    sp = getClient()

    playback = sp.current_playback()
    if not playback:
        print("No playback found. Ensure that Spotify is playing music.")
        return

    if len(sys.argv) > 1:
        loop_start = args.start
        loop_end = args.end

        if loop_end is None:
            print("Please specify an end time with the -e or --end argument.")
            exit(0)

        while True:
            playback = sp.current_playback()

            if playback:
                current_position = playback['progress_ms'] / 1000
                print(f"Current position: {current_position}s")

                if current_position >= loop_end:
                    print(f"Reached end time of {loop_end}s, resetting to {loop_start}s.")
                    sp.seek_track(int(loop_start * 1000)) 
            time.sleep(1)
    else:
        print("Run 'python3 main.py -h' for help")


if __name__ == '__main__':
    main()
