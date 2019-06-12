from django.http import JsonResponse

import requests
import json
import os


def show_pokemon(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    poke_name = body["name"]
    poke_types = body["types"]
    poke_id = body["id"]
    poke_list = []
    for type in poke_types:
        poke_list.append(type['type']['name'])
        
    key = os.environ.get("GIPHY_KEY")
    giphy_url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating=g".format(key, poke_name)
    giphy_res = requests.get(giphy_url)
    giphy_body = json.loads(giphy_res.content)
    giphy_url = giphy_body['data'][0]['url']

    return JsonResponse({"name": poke_name, "id": poke_id, "list": poke_list, "url": giphy_url})
