# Thomas McGinley
# Started 1/22/2024
# Last Updated 1/23/2024

# Gathers playtime information about each desired player, cleans the data, and generates JSON files with relevant information


import json
import requests
import prettytable

def getCharacterData(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=200"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }
    response = requests.request("GET",url, headers=headers, data=payload)
    characterData = json.loads(response.content)
    return characterData

getCharacterData(1,4611686018444441571)