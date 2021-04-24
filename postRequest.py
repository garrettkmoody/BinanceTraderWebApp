import requests
import json

url = 'https://flaskappfortest.wl.r.appspot.com/update'
body = {'newbal': 55}
headers = {'X-Api-Key': 'gj353o4jsdfsfj4'}
r = requests.post(url, json=body, headers=headers)
print(r.content)