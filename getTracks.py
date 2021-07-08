import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
from pprint import pprint

# Pull credentials
with open('./token.json') as token:
    data = json.load(token)

CLIENT_ID = data['client']['id']
CLIENT_SECRET = data['client']['secret']
REDIRECT_URI = data['client']['redirect']

# Create a new spotify object with read/modify playback permissions
scope = "user-read-playback-state, user-modify-playback-state, user-top-read"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(
                    client_id=CLIENT_ID, client_secret=CLIENT_SECRET,
                    redirect_uri=REDIRECT_URI, scope=scope))

# Get playlist ids
playlist_id = 'spotify:playlist:6YRk65pQ1fP72KxJcMCoat'
response = sp.playlist_items(playlist_id, fields='items.track.id', additional_types=['track'])

# Convert ids to array
ids = []
for track in response['items']:
    ids.append(track['track']['id'])
print(ids)