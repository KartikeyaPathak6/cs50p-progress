import requests
import json
import sys


def song(track):
    if len(sys.argv) !=2:
        sys.exit()

    response =requests.get("https://itunes.apple.com/search?entity=song&limit=20&term="+ track)

    data= response.json()
    for result in data["results"]:
        print(result["trackName"])