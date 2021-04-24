import requests
import json

url = 'http://127.0.0.1:5000/update'
body = {'newbal': 5000}
headers = {'X-Api-Key': 'gj353o4jsdfsfj4'}

r = requests.post(url, json=body, headers=headers)

print(r.content)