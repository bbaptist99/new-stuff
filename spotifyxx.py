import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Authorize the API for the web app
# export SPOTIPY_CLIENT_ID=''
# export SPOTIPY_CLIENT_SECRET=''
# export SPOTIPY_REDIRECT_URI='http://google.com/'

# Get the username
username = sys.argv[1]

 # User ID bbaptist99
 # Erase cache and prompt for user permission
try:
     token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username)

# Create spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']

while True:

    print()
    print(">>> Welcome to Spotipy " + displayName + " !")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Your choice: ")

    # Search for the artist
    if choice == "0":
        print("0")
        searchQuery = input("Ok, what's their name?: ")
        print()

        # Get search results
        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        
           # Artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total'])+ " followers")
        print(artist['genres'][0])
        print()
        webbrowser.open(artist['images'][0]['url'])



    # End the program
    if choice == "1":
        break



# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
