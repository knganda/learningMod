import requests
import sys
import json


# Appending sys.argv to the url enables the user to specify a different band via the terminal

url = "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(url)

#print(json.dumps(response.json(), indent=2))
o = response.json()

for result in o['results']:
    print(result['trackName'])
    

