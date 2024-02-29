import subprocess
import time
import json
import requests
from pprint import pprint

def get_current_song():
    return subprocess.check_output(['osascript', 'test.applescript']).decode('utf-8').strip()

def get_track_extras(song, artist, album):
    query = f"{song} {artist} {album}"
    params = {"media": "music", "entity": "song", "term": query}
    
    r = requests.get("https://itunes.apple.com/search", params=params)
    json_data =  r.json()
    # print('json_data: ', json_data)
    if json_data["resultCount"] == 1:
        result = json_data["results"][0]
    elif json_data["resultCount"] > 1:
        pass
    else :
        pass

    artwork_url = result["artworkUrl100"] if result else None
    itunes_url = result["trackViewUrl"] if result else None
    artist_url = result["artistViewUrl"] if result else None

    return (artwork_url, itunes_url, artist_url)

url = "http://127.0.0.1:5000"
headers = {'Content-Type': 'application/json'}

def post(currentsong):
    data = json.dumps(currentsong)
    r = requests.post(url+'/music/set', data=data, headers=headers)

    r = requests.get(url+'/music/display')
    print(r.text)

currentsong = json.loads(str(get_current_song()).replace("'''", '"'))

if currentsong['status'] == 'playing':
    (artwork_url, itunes_url, artist_url) = get_track_extras(currentsong['name'], currentsong['artist'], currentsong['album'])
    currentsong['artwork_url'] = artwork_url
    currentsong['itunes_url'] = itunes_url
    currentsong['artist_url'] = artist_url
    post(currentsong)
elif currentsong['status'] == 'not playing':
    print('not playing')
    post({'status' : 'not playing'})
elif currentsong['status'] == 'not running':
    print('not running')
    post({'status' : 'not running'})
else:
    pass

# def main():
#     while True:
#         current_song = get_current_song()
#         if current_song:
#             print("Currently listening to:", current_song)
#         else:
#             print("No music is playing.")
#         time.sleep(5)  # Check every 5 seconds

# if __name__ == "__main__":
#     main()
