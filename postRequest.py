import requests
import json

url = 'http://127.0.0.1:5000/price'
body = {'name': 'Maryja'}
headers = {'X-Api-Key': 'gj353o4jsdfsfj4'}

r = requests.post(url, data=json.dumps(body), headers=headers)

print(r.content)