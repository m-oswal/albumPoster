import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import math
# Set up the client credentials


# Get the album and artist name from user input

def songs(album,artist,sp,results):
    

    # Get the album ID from the search results
    album_id = results['albums']['items'][0]['id']

    # Get the tracks from the album
    tracks = sp.album_tracks(album_id)

    # Print the names of the tracks
    song = [i['name'] for i in tracks['items']]
    for j in range(len(song)):
        for k in range(len(song[j])):
                if song[j][k] == "(" or song[j][k]=="-":
                    song[j]=song[j][:k]
                    break
    return song


def release(album,artist,sp,results):
    
    try:
        # Get the album ID from the search results
        album_id = results['albums']['items'][0]['id']

        info = sp.album(album_id)
        release_date = info['release_date']
        
        
        date = release_date.split("-")
        
        d={'01':' January ','02':' February ','03':' March ','04':' April ','05':' May ','06':' June ','07':' July ','08':' Augutst ','09':' September ','10':' October ','11':' November ','12':' December '}
        release_date = date[2]+d[date[1]]+date[0]
        return release_date
    except:
        print("no album found")

def runtime(album,artist,sp,results):
   
    album_id = results['albums']['items'][0]['id']
    # album_data = sp.album(album_id)

    # Get track metadata for each track in the album
    tracks_data = sp.album_tracks(album_id)

    # Sum up the duration of each track to get the total runtime of the album
    total_runtime_ms = 0
    for track in tracks_data['items']:
        total_runtime_ms += track['duration_ms']

    # Convert milliseconds to seconds
    total_runtime_sec = total_runtime_ms / 1000
    #second to minutes
    total_runtime_minutes = total_runtime_sec/60
    total_runtime_sec = total_runtime_sec % 60

    return f"{math.floor(total_runtime_minutes)}:{math.floor(total_runtime_sec)}"

def cover(album,artist,sp,results):
    
    album_id = results['albums']['items'][0]['id']
    data = sp.album(album_id)
    print(data['label'])
    url = data['images'][0]['url']
    
    response = requests.get(url)
    with open('album_art.jpg', 'wb') as f:
        f.write(response.content)
    return f"BY {data['label']}"
    
def g(album,artist):
    client_id = "your_client_id"
    client_secret = "secret_id"
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q='album:"' + album + '" artist:"' + artist + '"', type='album')
    album_id = results['albums']['items'][0]['id']
    data = sp.album(album_id)
    

    ge =data['uri']
    print(ge)
album = "the eminem show".capitalize()
artist = "eminem"
g(album,artist)