import os
import requests
import json
import math

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://jotncomparer.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token"

membershipType = 1
destinyMembershipId = 4611686018450697084
# Titan:
characterId = 2305843009644414176

url = f"https://www.bungie.net/Platform/GroupV2/Name/Head Empty, Only Jötunn!/clan/"
payload = {}
headers = {
    'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
}

response = requests.request("GET", url, headers=headers, data=payload)
response.content.decode('utf-8')
pretty_Dungeon_data = json.dumps(json.loads(response.content), indent=2)
writeFile = open('Clan.json', 'w')
writeFile.write(pretty_Dungeon_data)

