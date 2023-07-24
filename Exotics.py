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
def Combiner():
    with open('Exotics.json') as f:
        data1 = json.load(f)
    with open('Exotics_1.json') as f:
        data2 = json.load(f)
    with open('Exotics_2.json') as f:
        data3 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]

    exotic_json = {"Response": []}

    exotic_json['Response'].append(items1)
    exotic_json["Response"].append(items2)
    exotic_json["Response"].append(items3)

    with open('exotic.json', "w") as f:
        f.write(json.dumps(exotic_json, indent=2))

    exotic_len_1 = len(exotic_json["Response"][0]['weapons'])
    exotic_len_2 = len(exotic_json["Response"][1]['weapons'])
    exotic_len_3 = len(exotic_json["Response"][2]['weapons'])

    if exotic_len_1 and exotic_len_2 > 0 and exotic_len_3 > 0:
        Exotic = {"Exotic": []}
        Kills = {"Kills": []}
        Precision = {"Precision Kills": []}

        for number in range(0, exotic_len_1):
            Name_1 = exotic_json["Response"][0]["weapons"][number]["referenceId"]
            Kills_1 = exotic_json["Response"][0]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
            Precision_1 = \
                exotic_json["Response"][0]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
            Exotic['Exotic'].append(Name_1)
            Kills['Kills'].append(Kills_1)
            Precision['Precision Kills'].append(Precision_1)
        for number in range(0, exotic_len_2):
            Name_2 = exotic_json["Response"][1]["weapons"][number]["referenceId"]
            Kills_2 = exotic_json["Response"][1]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
            Precision_2 = \
                exotic_json["Response"][1]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
            Exotic['Exotic'].append(Name_2)
            Kills['Kills'].append(Kills_2)
            Precision['Precision Kills'].append(Precision_2)
        for number in range(0, exotic_len_3):
            Name_3 = exotic_json["Response"][2]["weapons"][number]["referenceId"]
            Kills_3 = exotic_json["Response"][2]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
            Precision_3 = \
                exotic_json["Response"][2]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
            Exotic['Exotic'].append(Name_3)
            Kills['Kills'].append(Kills_3)
            Precision['Precision Kills'].append(Precision_3)

        Exotic_Info = [Exotic, Kills, Precision]

    length = len(Exotic_Info[0]['Exotic'])

    for numb in range(0, length):
        ID = Exotic_Info[0]['Exotic'][numb]
        Kills = Exotic_Info[1]['Kills'][numb]
        Precision = Exotic_Info[2]['Precision Kills'][numb]

        if ID == 2208405142:
            Exotic = "Telesto"
        elif ID == 2232171099:
            Exotic = "Deathbringer"
        elif ID == 2357297366:
            Exotic = "Witherhoard"
        elif ID == 2591746970:
            Exotic = "Leviathan's Breath"
        elif ID == 2694576561:
            Exotic = "Two-Tailed Fox"
        elif ID == 2812324400:
            Exotic = "Parasite"
        elif ID == 2812324401:
            Exotic = "Dead Messenger"
        elif ID == 2816212794:
            Exotic = "Bad Juju"
        elif ID == 2856683562:
            Exotic = "SUROS Regime"
        elif ID == 2907129557:
            Exotic = "Sunshot"
        elif ID == 3089417789:
            Exotic = "Riskrunner"
        elif ID == 3118061005:
            Exotic = "Vexcalibur"
        elif ID == 3141979346:
            Exotic = "D.A.R.C.I."
        elif ID == 3260753130:
            Exotic = "Ticuu's Divination"
        elif ID == 3325463374:
            Exotic = "Thunderlord"
        elif ID == 3413074534:
            Exotic = "Polaris Lance"
        elif ID == 3413860062:
            Exotic = "The Chaperone"
        elif ID == 3413860063:
            Exotic = "Lord of Wolves"
        elif ID == 3437746471:
            Exotic = "Crimson"
        elif ID == 3460576091:
            Exotic = "Duality"
        elif ID == 3487253372:
            Exotic = "The Lament"
        elif ID == 3524313097:
            Exotic = "Eriana's Vow"
        elif ID == 3580904581:
            Exotic = "Tractor Cannon"
        elif ID == 3588934839:
            Exotic = "Le Monarque"
        elif ID == 3628991658:
            Exotic = "Graviton Lance"
        elif ID == 3628991659:
            Exotic = "Vigilance Wing"
        elif ID == 3654674561:
            Exotic = "Dead Man's Tale"
        elif ID == 3659414143:
            Exotic = "Verglas Cure"
        elif ID == 3664831848:
            Exotic = "Heartshadow"
        elif ID == 3973202132:
            Exotic = "Thorn"
        elif ID == 4017959782:
            Exotic = "Symmetry"
        elif ID == 4036115577:
            Exotic = "Sleeper Simulant"
        elif ID == 4068264807:
            Exotic = "Monte Carlo"
        elif ID == 4124984448:
            Exotic = "Hard Light"
        elif ID == 4255268456:
            Exotic = "Skyburner's Oath"
        elif ID == 4293613902:
            Exotic = "Quicksilver Storm"
        elif ID == 19024058:
            Exotic = "Prometheus Lens"
        elif ID == 46524085:
            Exotic = "Osteo Striga"
        elif ID == 204878059:
            Exotic = "Malfeasance"
        elif ID == 370712896:
            Exotic = "Salvation's Grip"
        elif ID == 374573733:
            Exotic = "Delicate Tomb"
        elif ID == 400096939:
            Exotic = "Outbreak Perfected"
        elif ID == 417164956:
            Exotic = "Jötunn"
        elif ID == 449318888:
            Exotic = "Deterministic Chaos"
        elif ID == 776191470:
            Exotic = "Tommy's Matchbook"
        elif ID == 814876684:
            Exotic = "Wish-Ender"
        elif ID == 814876685:
            Exotic = "Trinity Ghoul"
        elif ID == 1345867570:
            Exotic = "Sweet Business"
        elif ID == 1345867571:
            Exotic = "Coldheart"
        elif ID == 1363238943:
            Exotic = "Ruinous Effigy"
        elif ID == 1363886209:
            Exotic = "Gjallarhorn"
        elif ID == 1395261499:
            Exotic = "Xenophage"
        elif ID == 1441805468:
            Exotic = "The Navigator"
        elif ID == 1473821207:
            Exotic = "Revision Zero"
        elif ID == 1508896098:
            Exotic = "The Wardcliff Coil"
        elif ID == 1594120904:
            Exotic = "No Time to Explain"
        elif ID == 1665952087:
            Exotic = "The Fourth Horseman"
        elif ID == 1763584999:
            Exotic = "Grand Overture"
        elif ID == 1833195496:
            Exotic = "Ager's Scepter"
        elif ID == 1912669214:
            Exotic = "Centrifuse"
        elif ID == 2044500762:
            Exotic = "The Queenbreaker"
        elif ID == 2130065553:
            Exotic = "Arbalest"

        Percent_PK = (Precision/Kills) * 100
        Percent_PK = round(Percent_PK, 3)
        Exotics = (f"{Exotic}, {Kills}, {Precision}, {Percent_PK}%")
        print(Exotics)

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
    Combiner()
