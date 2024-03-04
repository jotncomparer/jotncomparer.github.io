# Thomas McGinley
# Started 1/22/2024
# Last Updated 3/3/2024

# Gathers playtime information about each desired player, cleans the data, and generates JSON files with relevant information

from APIKEY import API_KEY
import json
import requests
import prettytable

def getCharacterData(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=200"
    payload = {}
    headers = API_KEY
    response = requests.request("GET",url, headers=headers, data=payload)
    characterData = json.loads(response.content)
    return characterData

getCharacterData(1,4611686018444441571)