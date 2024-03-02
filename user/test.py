import subprocess
import time
import json
import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

def get_current_song():
    return subprocess.check_output(['osascript', 'test.applescript']).decode('utf-8').strip()

def get_track_extras(song, artist, album):
    query = f"{song} {artist} {album}"
    params = {"media": "music", "entity": "song", "term": query}
    
    r = requests.get("https://itunes.apple.com/search", params=params)
    json_data =  r.json()
    if json_data["resultCount"] == 1:
        result = json_data["results"][0]
        pprint(result)
    elif json_data["resultCount"] > 1:
        result = json_data["results"][0]
    else :
        result = ''

    artwork_url = result["artworkUrl100"] if result else None
    itunes_url = result["trackViewUrl"] if result else None
    artist_url = result["artistViewUrl"] if result else None
    # album_url = result["collectionViewUrl"] if result else None

    return (artwork_url, itunes_url, artist_url)

def post(currentsong):
    currentsong['user'] = USER
    currentsong['password'] = PASSWORD
    data = json.dumps(currentsong)
    r = requests.post(url+'/music/set', data=data, headers=headers)
    if r.status_code != 200:
        return r.status_code
    else :
        return r.text

url = "http://192.168.1.58:3005"
headers = {'Content-Type': 'application/json'}

def main():
    persistendId = ''
    prevstatus = ''
    while True:
        print('getting data..')
        currentsong = json.loads(str(get_current_song()).replace("'''", '"'))

        if currentsong['status'] == 'playing':
            if currentsong['persistent ID'] != persistendId:
                persistendId = currentsong['persistent ID']
                currentsong['timestamp'] = time.time()
                (currentsong['artwork_url'], currentsong['itunes_url'], currentsong['artist_url']) = get_track_extras(currentsong['name'], currentsong['artist'], currentsong['album'])
                print(post(currentsong))
            timets = float(currentsong['duration'].replace(",", "."))-float(currentsong['pPosition'].replace(",", ".")) + 3
            prevstatus = 'playing'
        elif currentsong['status'] == 'not playing' and prevstatus != 'not playing':
            prevstatus = 'not playing'
            print('not playing')
            print(post({'status' : 'not playing'}))
            timets = 5*60
        elif currentsong['status'] == 'not running' and prevstatus != 'not running':
            prevstatus = 'not running'
            print('not running')
            print(post({'status' : 'not running'}))
            timets = 5*60
        else:
            timets = 5*60

        time.sleep(timets)

if __name__ == "__main__":
    main()