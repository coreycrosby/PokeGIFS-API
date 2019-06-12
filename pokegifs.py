import json
import requests
import os


res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"])
print(body["types"])
print(body["id"])     


key = os.environ.get("GIPHY_KEY")
url = "https://api.giphy.com/v1/gifs/search?api_key={}&q=pikachu&rating=g".format(key)
body5 = requests.get(url)
body5 = json.loads(body5.content)
url = body5["data"][5]["url"]

print(body5.keys())
print(url)
