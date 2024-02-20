import requests
import sys


# Appending sys.argv to the url enables the user to specify a different band via the terminal

url = "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.orig_argv[1]

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(url)

print(response.json())

