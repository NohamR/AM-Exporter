import requests
import json

url = "http://127.0.0.1:5000"

payload = {
    'key1': 'value1',
    'key2': 'value2'
}

json_payload = json.dumps(payload)

headers = {'Content-Type': 'application/json'}

r = requests.post(url+'/set', data=json_payload, headers=headers)
r = requests.get(url+'/get')
print(r.text)