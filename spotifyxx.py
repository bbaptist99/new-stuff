import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

# Get the username
username = sys.argv[1]

# Authorize the API for the web app
# export SPOTIPY_CLIENT_ID=''
# export SPOTIPY_CLIENT_SECRET=''
# export SPOTIPY_REDIRECT_URI='http://google.com/'

# run in terminal >> python3 spotifyxx.py bbaptist99

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
        artistID = artist['id']

        # Album and track details
        trackURIs = []
        trackArt = []
        z = 0

        #Extract Album data
        albumResults = spotifyObject.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print('ALBUM ' + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

            # Extract track data
            trackResults = spotifyObject.album_tracks(albumID)
            trackResults = trackResults['items']

            for item in trackResults:
                print(str(z) + ": " + item['name'])
                trackURIs.append(item['uri'])
                trackArt.append(albumArt)
                z+=1
            print()

        # See album artist
        while True:
            songSelection = input("Enter a song number to see the album art (x to exit): ")
            if songSelection = "x":
                break
            webbrowser.open(trackArt[int(songSelection)])

            

    # End the program
    if choice == "1":
        break



# print(json.dumps(VARIABLE, sort_keys=True, indent=4))
