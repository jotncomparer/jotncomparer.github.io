import json
import os
import requests
from ExoCombiner import ExoCombiner

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://jotncomparer.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token"


def URLZero(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics.json', 'w')
    writeFile.write(exotic_data)


def URLOne(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_1.json', 'w')
    writeFile.write(exotic_data)


def URLTwo(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_2.json', 'w')
    writeFile.write(exotic_data)


def Man_in_the_Moon():
    CHAR = 0
    membershipType = 1
    destinyMembershipId = 4611686018450697084
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009644414176
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009663894341
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009703275457
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()


Man_in_the_Moon()
