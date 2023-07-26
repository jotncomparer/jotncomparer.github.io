import json
import os
import requests

from ClanExoComparer import URLThree, URLFour, URLFive, URLSix, URLSeven, URLEight, URLNine, URLTen, URLEleven, \
    URLTwelve,URLThirteen, URLFourteen, URLFifteen, URLSixteen, URLSeventeen, URLEighteen, URLNineteen, URLTwenty, \
    URLTwenOne, URLTwenTwo, URLTwenThree, ClanExoCombiner

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
def The_Chrome_Leaf():
    CHAR = 0
    membershipType = 1
    destinyMembershipId = 4611686018444441571
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009265786295
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009283965144
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009569534739
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()
def Piepuns():
    CHAR = 0
    membershipType = 1
    destinyMembershipId = 4611686018434621591
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843010083874501
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009301374530
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009293915719
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()
def TheZefraOracle():
    CHAR = 0
    membershipType = 1
    destinyMembershipId = 4611686018432221111
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009668854600
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009348154555
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009802904121
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()
def HeavyChevy():
    CHAR = 0
    membershipType = 2
    destinyMembershipId = 4611686018469231992
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009268771475
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009891864023
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009890274343
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()
def Lachlan():
    CHAR = 0
    membershipType = 3
    destinyMembershipId = 4611686018476416864
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009359734078
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009359365362
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009756404411
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()
def SlayWarsV():
    CHAR = 0
    membershipType = 3
    destinyMembershipId = 4611686018501646188
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009683284493
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009624174508
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843009683284492
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()
def Gargoyle_Goose():
    CHAR = 0
    membershipType = 1
    destinyMembershipId = 4611686018451886498
    while CHAR < 3:
        if CHAR == 0:
            characterId = 2305843009264637524
            URLZero(membershipType, destinyMembershipId, characterId)
        if CHAR == 1:
            characterId = 2305843009264637527
            URLOne(membershipType, destinyMembershipId, characterId)
        if CHAR == 2:
            characterId = 2305843010322954573
            URLTwo(membershipType, destinyMembershipId, characterId)
        CHAR += 1
    ExoCombiner()


def ALL():
    PLAYER = 0
    while PLAYER < 8:
        # Man in the Moon
        while PLAYER == 0:
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
            PLAYER += 1
        # The Chrome Leaf
        while PLAYER == 1:
            CHAR = 0
            membershipType = 1
            destinyMembershipId = 4611686018444441571
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843009265786295
                    URLThree(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009283965144
                    URLFour(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843009569534739
                    URLFive(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        # Piepuns
        while PLAYER == 2:
            CHAR = 0
            membershipType = 1
            destinyMembershipId = 4611686018434621591
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843010083874501
                    URLSix(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009301374530
                    URLSeven(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843009293915719
                    URLEight(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        # TheZefraOracle
        while PLAYER == 3:
            CHAR = 0
            membershipType = 1
            destinyMembershipId = 4611686018432221111
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843009668854600
                    URLNine(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009348154555
                    URLTen(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843009802904121
                    URLEleven(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        # HeavyChevy
        while PLAYER == 4:
            CHAR = 0
            membershipType = 2
            destinyMembershipId = 4611686018469231992
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843009268771475
                    URLTwelve(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009891864023
                    URLThirteen(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843009890274343
                    URLFourteen(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        # Lachlan
        while PLAYER == 5:
            CHAR = 0
            membershipType = 3
            destinyMembershipId = 4611686018476416864
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843009359734078
                    URLFifteen(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009359365362
                    URLSixteen(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843009756404411
                    URLSeventeen(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        # SlayWarsV
        while PLAYER == 6:
            CHAR = 0
            membershipType = 3
            destinyMembershipId = 4611686018501646188
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843009683284493
                    URLEighteen(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009624174508
                    URLNineteen(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843009683284492
                    URLTwenty(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        # Gargoyle Goose
        while PLAYER == 7:
            CHAR = 0
            membershipType = 1
            destinyMembershipId = 4611686018451886498
            while CHAR < 3:
                if CHAR == 0:
                    characterId = 2305843009264637524
                    URLTwenOne(membershipType, destinyMembershipId, characterId)
                if CHAR == 1:
                    characterId = 2305843009264637527
                    URLTwenTwo(membershipType, destinyMembershipId, characterId)
                if CHAR == 2:
                    characterId = 2305843010322954573
                    URLTwenThree(membershipType, destinyMembershipId, characterId)
                CHAR += 1
            PLAYER += 1
        ClanExoCombiner()


print("Players: Connor, Thomas, Douglas, Hunter, Mark, Jack, Cameron, Kade")
print("Player Name: Man in the Moon, The Chrome Leaf, Piepuns, Lachlan, TheZefraOracle, HeavyChevy, SlayWarsV, "
      "Gargoyle Goose, All")
USER = input("Please type a player or player name to analyse their Exotic Weapon usage: ")

if USER == "Man in the Moon" or USER == "Connor":
    Man_in_the_Moon()
elif USER == "The Chrome Leaf" or USER == "Thomas":
    The_Chrome_Leaf()
elif USER == "Piepuns" or USER == "Douglas":
    Piepuns()
elif USER == "TheZefraOracle" or USER == "Mark":
    TheZefraOracle()
elif USER == "HeavyChevy" or USER == "Jack":
    HeavyChevy()
elif USER == "Lachlan" or USER == "Hunter":
    Lachlan()
elif USER == "SlayWarsV" or USER == "Cameron":
    SlayWarsV()
elif USER == "Gargoyle Goose" or USER == "Kade":
    Gargoyle_Goose()
elif USER == "All":
    ALL()
