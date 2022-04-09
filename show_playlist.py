import sys
import spotipy

username = input('enter a username: ')
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Whoops, need a username!")
#     print("usage: python user_playlists.py [username]")
#     sys.exit()

scope = 'playlist-modify-public'
# username = 'ianuriegas'

token = spotipy.SpotifyOAuth(scope=scope,username=username)
spotifyObject = spotipy.Spotify(auth_manager=token)

playlists = spotifyObject.user_playlists(username)

count=1

#prints 50 playlists
for playlist in playlists['items']:
    print(int(count)," ")
    print(playlist['name'])
    count=count+1
