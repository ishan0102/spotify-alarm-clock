import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from pprint import pprint
from time import sleep
import argparse, logging

# Pull credentials
with open('./token.json') as token:
    data = json.load(token)

MAC_ID = data['device']['mac']
IPHONE_ID = data['device']['iphone']
CLIENT_ID = data['client']['id']
CLIENT_SECRET = data['client']['secret']
REDIRECT_URI = data['client']['redirect']

# Create a new spotify object with read/modify playback permissions
scope = "user-read-playback-state, user-modify-playback-state, user-top-read"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(
                    client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                    redirect_uri=REDIRECT_URI, scope=scope))

# Show playing devices with pretty formatting!
device_list = sp.devices()
pprint(device_list)

# Transfer playback to Macbook if no song is playing
sp.transfer_playback(device_id=MAC_ID, force_play=True)

# Play a random song off of my playlist
sp.start_playback(context_uri=data['playlist']['trap'])
