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

pl_id = 'spotify:playlist:181rappNUEG26jD0aeYIi4'
pl_id2 = 'spotify:playlist:37i9dQZF1ELZqgPLPo7ozJ'
pl_id3 = 'spotify:playlist:0MtdOpFYr3BJtcAsme7gyJ'
pl_id4 = 'spotify:playlist:5XHaTJ7PJWEiyvUcI8UbFZ'
offset = 0

while True:
    response = sp.playlist_items(pl_id4,
                                 offset=offset,
                                 fields='items.track.id, items.track.name, total',
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    pprint(response['items'])
    offset = offset + len(response['items'])