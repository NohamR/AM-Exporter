import subprocess
import sys
import time
from datetime import datetime
import json
import requests
from pprint import pprint
import os
from dotenv import load_dotenv
load_dotenv()
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
URL_API = os.getenv("URL_API")

stdout_file = 'logfile.log'
stderr_file = 'error_logfile.log'

sys.stdout = open(stdout_file, 'a')
sys.stderr = open(stderr_file, 'a')

def printout(content):
    print(f"{datetime.now().strftime('%H:%M:%S')} : {content}", file=sys.stdout)
    sys.stdout.flush()

def printerr(content):
    print(f"{datetime.now().strftime('%H:%M:%S')} : An error occurred: {str(content)}", file=sys.stderr)
    sys.stderr.flush()

def get_current_song():
    try:
        output = subprocess.check_output(['osascript', 'export.applescript']).decode('utf-8').strip()
        return output
    except subprocess.CalledProcessError as e:
        printerr(e)
        return e

def get_track_extras(song, artist, album):
    query = f"{song} {artist} {album}"
    params = {"media": "music", "entity": "song", "term": query}
    
    r = requests.get("https://itunes.apple.com/search", params=params)
    json_data =  r.json()
    if json_data["resultCount"] == 1:
        result = json_data["results"][0]
    elif json_data["resultCount"] > 1:
        result = json_data["results"][0]
    else :
        result = ''

    artwork_url = result["artworkUrl100"] if result else None
    itunes_url = result["trackViewUrl"] if result else None
    artist_url = result["artistViewUrl"] if result else None

    return (artwork_url, itunes_url, artist_url)

def post(currentsong):
    currentsong['user'] = USER
    currentsong['password'] = PASSWORD
    data = json.dumps(currentsong)
    try:
        r = requests.post(URL_API+'/music/set', data=data, headers=headers)
        if r.status_code != 200:
            return r.status_code
        else :
            return r.text
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)

headers = {'Content-Type': 'application/json'}

def main():
    persistendId = ''
    prevstatus = ''
    while True:
        # print('getting data..', file=sys.stdout)
        # currentsong = json.loads(str(get_current_song()).replace("'''", '"'))
        currentsong = json.loads(get_current_song())

        if currentsong['status'] == 'playing':
            if currentsong['persistent ID'] != persistendId:
                persistendId = currentsong['persistent ID']
                currentsong['timestamp'] = time.time()
                (currentsong['artwork_url'], currentsong['itunes_url'], currentsong['artist_url']) = get_track_extras(currentsong['name'], currentsong['artist'], currentsong['album'])
                printout(f"{post(currentsong)}")
            timets = float(currentsong['duration'].replace(",", "."))-float(currentsong['pPosition'].replace(",", ".")) + 3
            prevstatus = 'playing'
        elif currentsong['status'] == 'not playing' and prevstatus != 'not playing':
            prevstatus = 'not playing'
            printout(f"{post({'status' : 'not playing'})}")
            timets = 5*60
        elif currentsong['status'] == 'not running' and prevstatus != 'not running':
            prevstatus = 'not running'
            printout(f"{post({'status' : 'not running'})}")
            timets = 5*60
        else:
            timets = 5*60

        time.sleep(timets)

if __name__ == "__main__":
    main()