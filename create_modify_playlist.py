import os
import json
import spotipy

spotify_client_id = os.environ['SPOTIPY_CLIENT_ID']
spotify_secret = os.environ['SPOTIPY_CLIENT_SECRET']
spotify_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
# genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

scope = 'playlist-modify-public'
# username = 'ianuriegas'
username = input("Enter a username: ")

token = spotipy.SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager = token)

playlist_name = input("Enter a playlist name: ")
playlist_description = input("Enter a playlist description: ")

# creates actual playlist
spotifyObject.user_playlist_create(user=username,name=playlist_name,public=True,collaborative=False,description=playlist_description)

user_input = input("Enter song and artist: ")
list_of_songs = []

while user_input != 'quit':
    result=spotifyObject.search(q=user_input)
    # print(json.dumps(result,sort_keys=4,indent=4))
    list_of_songs.append(result['tracks']['items'][0]['uri'])
    user_input = input('Enter song and artist: ')

#find new playlist
prePlaylist = spotifyObject.user_playlists(user=username)
playlist = prePlaylist['items'][0]['id']

#add songs
spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=list_of_songs)
