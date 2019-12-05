import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError


username = sys.argv[1]
scope = 'user-library-read'

try:
     token = util.prompt_for_user_token(username, scope)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

results = spotifyObject.current_user_saved_tracks()

displayName = user['display_name']
followers = user['followers']['total']


while True:

    print()
    print(">>> Welcome to Spotipy " + displayName + " !")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Display saved tracks")
    print("1 - exit")
    choice = input("Your choice: ")

    if choice == "0":
        for item in results['items']:
            track = item['track']
            print(track['name'] + ' - ' + track['artists'][0]['name'])
    if choice == "1":
        break
