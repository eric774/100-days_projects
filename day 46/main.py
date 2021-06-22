from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "fc063f63e719421b86047e42fca4662f"
CLIENT_SECRET = "533a251e5cfc43ba9ce05847763296d3"
REDIRECT_URI = "http://example.com"

# year = input("what year you would like to travel to in YYY-MM-DD format: ")
# URL = "https://www.billboard.com/charts/hot-100/2015-03-21" #replace last string with year
# response = requests.get(URL)
# soup = BeautifulSoup(response.text, "html.parser")
# all_songs = soup.find_all(name="span", class_="chart-element__information__song")

# song_titles = [song.getText() for song in all_songs]
# print(song_titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope="playlist-modify-private"))
                                                           

results = sp.current_user_saved_tracks()
print(results)
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])