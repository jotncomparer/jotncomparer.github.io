# Connor Downs
# Started: 7-26-2023
# Last Updated: 8-14-2023
# This program creates tables of the most used exotics across all members of Jotunn Gang
# Tables are broken down into top 5 Primary, Special, and Heavy, as well as top 10 of all Exotics

import json
import os
import requests

from prettytable import PrettyTable

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


def URLThree(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_3.json', 'w')
    writeFile.write(exotic_data)


def URLFour(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_4.json', 'w')
    writeFile.write(exotic_data)


def URLFive(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_5.json', 'w')
    writeFile.write(exotic_data)


def URLSix(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_6.json', 'w')
    writeFile.write(exotic_data)


def URLSeven(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_7.json', 'w')
    writeFile.write(exotic_data)


def URLEight(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_8.json', 'w')
    writeFile.write(exotic_data)


def URLNine(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_9.json', 'w')
    writeFile.write(exotic_data)


def URLTen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_10.json', 'w')
    writeFile.write(exotic_data)


def URLEleven(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_11.json', 'w')
    writeFile.write(exotic_data)


def URLTwelve(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_12.json', 'w')
    writeFile.write(exotic_data)


def URLThirteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_13.json', 'w')
    writeFile.write(exotic_data)


def URLFourteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_14.json', 'w')
    writeFile.write(exotic_data)


def URLFifteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_15.json', 'w')
    writeFile.write(exotic_data)


def URLSixteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_16.json', 'w')
    writeFile.write(exotic_data)


def URLSeventeen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_17.json', 'w')
    writeFile.write(exotic_data)


def URLEighteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_18.json', 'w')
    writeFile.write(exotic_data)


def URLNineteen(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_19.json', 'w')
    writeFile.write(exotic_data)


def URLTwenty(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_20.json', 'w')
    writeFile.write(exotic_data)


def URLTwenOne(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_21.json', 'w')
    writeFile.write(exotic_data)


def URLTwenTwo(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_22.json', 'w')
    writeFile.write(exotic_data)


def URLTwenThree(membershipType, destinyMembershipId, characterId):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/UniqueWeapons/"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    exotic_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Exotics_23.json', 'w')
    writeFile.write(exotic_data)


def ClanExoCombiner():
    class Exotic:
        def __init__(self, exotic_id, exotic_name):
            self.id = exotic_id
            self.name = exotic_name
            self.kills = 0
            self.prec = 0

        def weaponData(self, kills, prec):
            self.kills += Kills
            self.prec += Precision

    sweetBusiness = Exotic(1345867570, 'Sweet Business')
    strum = Exotic(2907129556, 'Strum')
    vigilance = Exotic(3628991659, 'Vigilance Wing')
    ratKing = Exotic(2362471601, 'Rat King')
    mida = Exotic(1331482397, 'MIDA Multi-Tool')
    crimson = Exotic(3437746471, 'Crimson')
    rabbit = Exotic(3844694310, 'Jade Rabbit')
    huckle = Exotic(2286143274, 'Huckleberry')
    suros = Exotic(2856683562, 'SUROS Regime')
    cerberus = Exotic(1541131350, 'Cerberus+1')
    wish = Exotic(814876684, 'Wish Ender')
    malfease = Exotic(204878059, 'Malfeasance')
    ace = Exotic(347366834, 'Ace of Spaced')
    chaperone = Exotic(3413860062, 'The Chaperone')
    izan = Exotic(3211806999, "Izanagi's Burden")
    lastword = Exotic(1364093401, 'The Last Word')
    arbalest = Exotic(2130065553, 'Arbalest')
    thorn = Exotic(3973202132, 'Thorn')
    outbreak = Exotic(400096939, 'Outbreak Perfected')
    lumina = Exotic(3512014804, 'Lumina')
    juju = Exotic(2816212794, 'Bad Juju')
    monte = Exotic(4068264807, 'Monte Carlo')
    bastion = Exotic(2415517654, 'Bastion')
    witherhoard = Exotic(2357297366, 'Witherhoard')
    chosen = Exotic(1853180924, "Traveler's Chosen")
    hawkmoon = Exotic(3856705927, 'Hawkmoon')
    notime = Exotic(1594120904, 'No Time to Explain')
    deadmans = Exotic(3654674561, "Dead Man's Tale")
    cryo = Exotic(603721696, 'Cryosthethesia 77K')
    agers = Exotic(1833195496, "Ager's Scepter")
    forerunner = Exotic(2179048386, 'Forerunner')
    osteo = Exotic(46524085, 'Osteo Striga')
    touch = Exotic(1802135586, 'Touch of Malice')
    quicksilver = Exotic(4293613902, 'Quicksilver Storm')
    revision = Exotic(1473821207, 'Revision Zero')
    warning = Exotic(3121540812, 'Final Warning')
    finality = Exotic(3371017761, 'Conditional Finality')
    verglas = Exotic(3659414143, 'Verglas Curve')
    wicked = Exotic(940371471, 'Wicked Implement')
    navigator = Exotic(1441805468, 'The Navigator')
    coldheart = Exotic(1345867571, 'Coldheart')
    merciless = Exotic(4190156464, 'Merciless')
    fighting = Exotic(3549153978, 'Fighting Lion')
    sunshot = Exotic(2907129557, 'Sunshot')
    graviton = Exotic(3628991658, 'Graviton Lance')
    skyburner = Exotic(4255268456, "Skyburner's Oath")
    bore = Exotic(3141979347, 'Borealis')
    riskrunner = Exotic(3089417789, 'Riskrunner')
    hardlight = Exotic(4124984448, 'Hard Light')
    prometheus = Exotic(19024058, 'Prometheus Lens')
    telesto = Exotic(2208405142, 'Telesto')
    polaris = Exotic(3413074534, 'Polaris Lance')
    trinity = Exotic(814876685, 'Trinity Ghoul')
    wavesplit = Exotic(1852863732, 'Wavesplitter')
    lordofwolves = Exotic(3413860063, 'Lord of Wolves')
    lemon = Exotic(3588934839, 'Le Monarque')
    jotunn = Exotic(417164956, 'Jötunn')
    tarrabah = Exotic(3110698812, 'Tarrabah')
    eriana = Exotic(3524313097, "Eriana's Vow")
    divinity = Exotic(4103414242, 'Divinity')
    symmetry = Exotic(4017959782, 'Symmetry')
    devil = Exotic(3824106094, "Devil's Ruin")
    tommys = Exotic(776191470, "Tommy's Matchbook")
    fourthhorse = Exotic(1665952087, "The Fourth Horseman")
    ruinous = Exotic(1363238943, 'Ruinous Effigy')
    duality = Exotic(3460576091, 'Duality')
    cloudstrike = Exotic(2603483885, 'Cloudstrike')
    ticuu = Exotic(3260753130, "Ticuu's Divination")
    mythoclast = Exotic(4289226715, 'Vex Mythoclast')
    driver = Exotic(3761898871, 'Lorentz Driver')
    intent = Exotic(14194600, 'Edge of Intent')
    messenger = Exotic(2812324401, 'Dead Messenger')
    obligation = Exotic(3505113722, 'Collective Obligation')
    delicate = Exotic(374573733, 'Delicate Tomb')
    trespass = Exotic(1234150730, 'The Trespasser')
    manticore = Exotic(219145368, 'The Manticore')
    hierarchy = Exotic(4174431791, 'Hierarchy of Needs')
    vexcal = Exotic(3118061005, 'Vexcalibur')
    centrifuse = Exotic(1912669214, 'Centrifuse')
    wardcliff = Exotic(1508896098, 'Wardcliff Coil')
    tractor = Exotic(358090458, 'Tractor Cannon')
    acrius = Exotic(3580904580, 'Legend of Acrius')
    darci = Exotic(3141979346, 'D.A.R.C.I')
    colony = Exotic(3899270607, 'The Colony')
    worldline = Exotic(1864563948, 'Worldline Zero')
    sleeper = Exotic(4036115577, 'Sleeper Simulant')
    thousand = Exotic(2069224589, 'One Thousand Voices')
    twotailed = Exotic(2694576561, 'Two-Tailed Fox')
    black = Exotic(3766045777, 'Black Talon')
    queenbreak = Exotic(2044500762, 'The Queenbreaker')
    thunderlord = Exotic(3325463374, 'Thunderlord')
    anarchy = Exotic(2376481550, 'Anarchy')
    leviathan = Exotic(2591746970, "Leviathan's Breath")
    xeno = Exotic(1395261499, 'Xenopahge')
    deathbringer = Exotic(2232171099, 'Deathbringer')
    heir = Exotic(2084878005, 'Heir Apparent')
    salvation = Exotic(370712896, "Salvation's Grip")
    eyesof = Exotic(2399110176, 'Eyes of Tomorrow')
    lament = Exotic(3487253372, 'Lament')
    gjallar = Exotic(1363886209, 'Gjallarhorn')
    parasite = Exotic(2812324400, 'Parasite')
    overture = Exotic(1763584999, 'Grand Overture')
    heartshadow = Exotic(3664831848, 'Heartshadow')
    determine = Exotic(449318888, 'Deterministic Chaos')
    winterbite = Exotic(3118061004, 'Winterbite')
    truth = Exotic(1201830623, 'Truth')
    whisper = Exotic(1891561814, 'Whisper of the Worm')

    with open('Exotics.json') as f:
        data1 = json.load(f)
    with open('Exotics_1.json') as f:
        data2 = json.load(f)
    with open('Exotics_2.json') as f:
        data3 = json.load(f)
    with open('Exotics_3.json') as f:
        data4 = json.load(f)
    with open('Exotics_4.json') as f:
        data5 = json.load(f)
    with open('Exotics_5.json') as f:
        data6 = json.load(f)
    with open('Exotics_6.json') as f:
        data7 = json.load(f)
    with open('Exotics_7.json') as f:
        data8 = json.load(f)
    with open('Exotics_8.json') as f:
        data9 = json.load(f)
    with open('Exotics_9.json') as f:
        data10 = json.load(f)
    with open('Exotics_10.json') as f:
        data11 = json.load(f)
    with open('Exotics_11.json') as f:
        data12 = json.load(f)
    with open('Exotics_12.json') as f:
        data13 = json.load(f)
    with open('Exotics_13.json') as f:
        data14 = json.load(f)
    with open('Exotics_14.json') as f:
        data15 = json.load(f)
    with open('Exotics_15.json') as f:
        data16 = json.load(f)
    with open('Exotics_16.json') as f:
        data17 = json.load(f)
    with open('Exotics_17.json') as f:
        data18 = json.load(f)
    with open('Exotics_18.json') as f:
        data19 = json.load(f)
    with open('Exotics_19.json') as f:
        data20 = json.load(f)
    with open('Exotics_20.json') as f:
        data21 = json.load(f)
    with open('Exotics_21.json') as f:
        data22 = json.load(f)
    with open('Exotics_22.json') as f:
        data23 = json.load(f)
    with open('Exotics_23.json') as f:
        data24 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]
    items4 = data4["Response"]
    items5 = data5["Response"]
    items6 = data6["Response"]
    items7 = data7["Response"]
    items8 = data8["Response"]
    items9 = data9["Response"]
    items10 = data10["Response"]
    items11 = data11["Response"]
    items12 = data12["Response"]
    items13 = data13["Response"]
    items14 = data14["Response"]
    items15 = data15["Response"]
    items16 = data16["Response"]
    items17 = data17["Response"]
    items18 = data18["Response"]
    items19 = data19["Response"]
    items20 = data20["Response"]
    items21 = data21["Response"]
    items22 = data22["Response"]
    items23 = data23["Response"]
    items24 = data24["Response"]

    exotic_json = {"Response": []}

    exotic_json['Response'].append(items1)
    exotic_json["Response"].append(items2)
    exotic_json["Response"].append(items3)
    exotic_json['Response'].append(items4)
    exotic_json["Response"].append(items5)
    exotic_json["Response"].append(items6)
    exotic_json['Response'].append(items7)
    exotic_json["Response"].append(items8)
    exotic_json["Response"].append(items9)
    exotic_json['Response'].append(items10)
    exotic_json["Response"].append(items11)
    exotic_json["Response"].append(items12)
    exotic_json['Response'].append(items13)
    exotic_json["Response"].append(items14)
    exotic_json["Response"].append(items15)
    exotic_json['Response'].append(items16)
    exotic_json["Response"].append(items17)
    exotic_json["Response"].append(items18)
    exotic_json['Response'].append(items19)
    exotic_json["Response"].append(items20)
    exotic_json["Response"].append(items21)
    exotic_json['Response'].append(items22)
    exotic_json["Response"].append(items23)
    exotic_json["Response"].append(items24)

    with open('exotic.json', "w") as f:
        f.write(json.dumps(exotic_json, indent=2))

    exotic_len_1 = len(exotic_json["Response"][0]['weapons'])
    exotic_len_2 = len(exotic_json["Response"][1]['weapons'])
    exotic_len_3 = len(exotic_json["Response"][2]['weapons'])
    exotic_len_4 = len(exotic_json["Response"][3]['weapons'])
    exotic_len_5 = len(exotic_json["Response"][4]['weapons'])
    exotic_len_6 = len(exotic_json["Response"][5]['weapons'])
    exotic_len_7 = len(exotic_json["Response"][6]['weapons'])
    exotic_len_8 = len(exotic_json["Response"][7]['weapons'])
    exotic_len_9 = len(exotic_json["Response"][8]['weapons'])
    exotic_len_10 = len(exotic_json["Response"][9]['weapons'])
    exotic_len_11 = len(exotic_json["Response"][10]['weapons'])
    exotic_len_12 = len(exotic_json["Response"][11]['weapons'])
    exotic_len_13 = len(exotic_json["Response"][12]['weapons'])
    exotic_len_14 = len(exotic_json["Response"][13]['weapons'])
    exotic_len_15 = len(exotic_json["Response"][14]['weapons'])
    exotic_len_16 = len(exotic_json["Response"][15]['weapons'])
    exotic_len_17 = len(exotic_json["Response"][16]['weapons'])
    exotic_len_18 = len(exotic_json["Response"][17]['weapons'])
    exotic_len_19 = len(exotic_json["Response"][18]['weapons'])
    exotic_len_20 = len(exotic_json["Response"][19]['weapons'])
    exotic_len_21 = len(exotic_json["Response"][20]['weapons'])
    exotic_len_22 = len(exotic_json["Response"][21]['weapons'])
    exotic_len_23 = len(exotic_json["Response"][22]['weapons'])
    exotic_len_24 = len(exotic_json["Response"][23]['weapons'])

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
    for number in range(0, exotic_len_4):
        Name_4 = exotic_json["Response"][3]["weapons"][number]["referenceId"]
        Kills_4 = exotic_json["Response"][3]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_4 = \
            exotic_json["Response"][3]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_4)
        Kills['Kills'].append(Kills_4)
        Precision['Precision Kills'].append(Precision_4)
    for number in range(0, exotic_len_5):
        Name_5 = exotic_json["Response"][4]["weapons"][number]["referenceId"]
        Kills_5 = exotic_json["Response"][4]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_5 = \
            exotic_json["Response"][4]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_5)
        Kills['Kills'].append(Kills_5)
        Precision['Precision Kills'].append(Precision_5)
    for number in range(0, exotic_len_6):
        Name_6 = exotic_json["Response"][5]["weapons"][number]["referenceId"]
        Kills_6 = exotic_json["Response"][5]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_6 = \
            exotic_json["Response"][5]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_6)
        Kills['Kills'].append(Kills_6)
        Precision['Precision Kills'].append(Precision_6)
    for number in range(0, exotic_len_7):
        Name_7 = exotic_json["Response"][6]["weapons"][number]["referenceId"]
        Kills_7 = exotic_json["Response"][6]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_7 = \
            exotic_json["Response"][6]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_7)
        Kills['Kills'].append(Kills_7)
        Precision['Precision Kills'].append(Precision_7)
    for number in range(0, exotic_len_8):
        Name_8 = exotic_json["Response"][7]["weapons"][number]["referenceId"]
        Kills_8 = exotic_json["Response"][7]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_8 = \
            exotic_json["Response"][7]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_8)
        Kills['Kills'].append(Kills_8)
        Precision['Precision Kills'].append(Precision_8)
    for number in range(0, exotic_len_9):
        Name_9 = exotic_json["Response"][8]["weapons"][number]["referenceId"]
        Kills_9 = exotic_json["Response"][8]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_9 = \
            exotic_json["Response"][8]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_9)
        Kills['Kills'].append(Kills_9)
        Precision['Precision Kills'].append(Precision_9)
    for number in range(0, exotic_len_10):
        Name_10 = exotic_json["Response"][9]["weapons"][number]["referenceId"]
        Kills_10 = exotic_json["Response"][9]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_10 = \
            exotic_json["Response"][9]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_10)
        Kills['Kills'].append(Kills_10)
        Precision['Precision Kills'].append(Precision_10)
    for number in range(0, exotic_len_11):
        Name_11 = exotic_json["Response"][10]["weapons"][number]["referenceId"]
        Kills_11 = exotic_json["Response"][10]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_11 = \
            exotic_json["Response"][10]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_11)
        Kills['Kills'].append(Kills_11)
        Precision['Precision Kills'].append(Precision_11)
    for number in range(0, exotic_len_12):
        Name_12 = exotic_json["Response"][11]["weapons"][number]["referenceId"]
        Kills_12 = exotic_json["Response"][11]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_12 = \
            exotic_json["Response"][11]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_12)
        Kills['Kills'].append(Kills_12)
        Precision['Precision Kills'].append(Precision_12)
    for number in range(0, exotic_len_13):
        Name_13 = exotic_json["Response"][12]["weapons"][number]["referenceId"]
        Kills_13 = exotic_json["Response"][12]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_13 = \
            exotic_json["Response"][12]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_13)
        Kills['Kills'].append(Kills_13)
        Precision['Precision Kills'].append(Precision_13)
    for number in range(0, exotic_len_14):
        Name_14 = exotic_json["Response"][13]["weapons"][number]["referenceId"]
        Kills_14 = exotic_json["Response"][13]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_14 = \
            exotic_json["Response"][13]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_14)
        Kills['Kills'].append(Kills_14)
        Precision['Precision Kills'].append(Precision_14)
    for number in range(0, exotic_len_15):
        Name_15 = exotic_json["Response"][14]["weapons"][number]["referenceId"]
        Kills_15 = exotic_json["Response"][14]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_15 = \
            exotic_json["Response"][14]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_15)
        Kills['Kills'].append(Kills_15)
        Precision['Precision Kills'].append(Precision_15)
    for number in range(0, exotic_len_16):
        Name_16 = exotic_json["Response"][15]["weapons"][number]["referenceId"]
        Kills_16 = exotic_json["Response"][15]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_16 = \
            exotic_json["Response"][15]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_16)
        Kills['Kills'].append(Kills_16)
        Precision['Precision Kills'].append(Precision_16)
    for number in range(0, exotic_len_17):
        Name_17 = exotic_json["Response"][16]["weapons"][number]["referenceId"]
        Kills_17 = exotic_json["Response"][16]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_17 = \
            exotic_json["Response"][16]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_17)
        Kills['Kills'].append(Kills_17)
        Precision['Precision Kills'].append(Precision_17)
    for number in range(0, exotic_len_18):
        Name_18 = exotic_json["Response"][17]["weapons"][number]["referenceId"]
        Kills_18 = exotic_json["Response"][17]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_18 = \
            exotic_json["Response"][17]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_18)
        Kills['Kills'].append(Kills_18)
        Precision['Precision Kills'].append(Precision_18)
    for number in range(0, exotic_len_19):
        Name_19 = exotic_json["Response"][18]["weapons"][number]["referenceId"]
        Kills_19 = exotic_json["Response"][18]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_19 = \
            exotic_json["Response"][18]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_19)
        Kills['Kills'].append(Kills_19)
        Precision['Precision Kills'].append(Precision_19)
    for number in range(0, exotic_len_20):
        Name_20 = exotic_json["Response"][19]["weapons"][number]["referenceId"]
        Kills_20 = exotic_json["Response"][19]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_20 = \
            exotic_json["Response"][19]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_20)
        Kills['Kills'].append(Kills_20)
        Precision['Precision Kills'].append(Precision_20)
    for number in range(0, exotic_len_21):
        Name_21 = exotic_json["Response"][20]["weapons"][number]["referenceId"]
        Kills_21 = exotic_json["Response"][20]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_21 = \
            exotic_json["Response"][20]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_21)
        Kills['Kills'].append(Kills_21)
        Precision['Precision Kills'].append(Precision_21)
    for number in range(0, exotic_len_22):
        Name_22 = exotic_json["Response"][21]["weapons"][number]["referenceId"]
        Kills_22 = exotic_json["Response"][21]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_22 = \
            exotic_json["Response"][21]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_22)
        Kills['Kills'].append(Kills_22)
        Precision['Precision Kills'].append(Precision_22)
    for number in range(0, exotic_len_23):
        Name_23 = exotic_json["Response"][22]["weapons"][number]["referenceId"]
        Kills_23 = exotic_json["Response"][22]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_23 = \
            exotic_json["Response"][22]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_23)
        Kills['Kills'].append(Kills_23)
        Precision['Precision Kills'].append(Precision_23)
    for number in range(0, exotic_len_24):
        Name_24 = exotic_json["Response"][23]["weapons"][number]["referenceId"]
        Kills_24 = exotic_json["Response"][23]["weapons"][number]["values"]["uniqueWeaponKills"]["basic"]["value"]
        Precision_24 = \
            exotic_json["Response"][23]["weapons"][number]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"]
        Exotic['Exotic'].append(Name_24)
        Kills['Kills'].append(Kills_24)
        [''].append(Kills_24)
        Precision['Precision Kills'].append(Precision_24)

    Exotic_Info = [Exotic, Kills, Precision]

    length = len(Exotic_Info[0]['Exotic'])

    for numb in range(0, length):
        ID = Exotic_Info[0]['Exotic'][numb]
        Kills = Exotic_Info[1]['Kills'][numb]
        Precision = Exotic_Info[2]['Precision Kills'][numb]

        if ID == 2208405142:
            telesto.weaponData(Kills, Precision)
        elif ID == 2232171099:
            deathbringer.weaponData(Kills, Precision)
        elif ID == 2357297366:
            witherhoard.weaponData(Kills, Precision)
        elif ID == 2591746970:
            leviathan.weaponData(Kills, Precision)
        elif ID == 2694576561:
            twotailed.weaponData(Kills, Precision)
        elif ID == 2812324400:
            parasite.weaponData(Kills, Precision)
        elif ID == 2812324401:
            messenger.weaponData(Kills, Precision)
        elif ID == 2816212794:
            juju.weaponData(Kills, Precision)
        elif ID == 2856683562:
            suros.weaponData(Kills, Precision)
        elif ID == 2907129557:
            sunshot.weaponData(Kills, Precision)
        elif ID == 3089417789:
            riskrunner.weaponData(Kills, Precision)
        elif ID == 3118061005:
            vexcal.weaponData(Kills, Precision)
        elif ID == 3141979346:
            darci.weaponData(Kills, Precision)
        elif ID == 3260753130:
            ticuu.weaponData(Kills, Precision)
        elif ID == 3325463374:
            thunderlord.weaponData(Kills, Precision)
        elif ID == 3413074534:
            polaris.weaponData(Kills, Precision)
        elif ID == 3413860062:
            chaperone.weaponData(Kills, Precision)
        elif ID == 3413860063:
            lordofwolves.weaponData(Kills, Precision)
        elif ID == 3437746471:
            crimson.weaponData(Kills, Precision)
        elif ID == 3460576091:
            duality.weaponData(Kills, Precision)
        elif ID == 3487253372:
            lament.weaponData(Kills, Precision)
        elif ID == 3524313097:
            eriana.weaponData(Kills, Precision)
        elif ID == 3580904581:
            tractor.weaponData(Kills, Precision)
        elif ID == 3588934839:
            lemon.weaponData(Kills, Precision)
        elif ID == 3628991658:
            graviton.weaponData(Kills, Precision)
        elif ID == 3628991659:
            vigilance.weaponData(Kills, Precision)
        elif ID == 3654674561:
            deadmans.weaponData(Kills, Precision)
        elif ID == 3659414143:
            verglas.weaponData(Kills, Precision)
        elif ID == 3664831848:
            heartshadow.weaponData(Kills, Precision)
        elif ID == 3973202132:
            thorn.weaponData(Kills, Precision)
        elif ID == 4017959782:
            symmetry.weaponData(Kills, Precision)
        elif ID == 4036115577:
            sleeper.weaponData(Kills, Precision)
        elif ID == 4068264807:
            monte.weaponData(Kills, Precision)
        elif ID == 4124984448:
            hardlight.weaponData(Kills, Precision)
        elif ID == 4255268456:
            skyburner.weaponData(Kills, Precision)
        elif ID == 4293613902:
            quicksilver.weaponData(Kills, Precision)
        elif ID == 19024058:
            prometheus.weaponData(Kills, Precision)
        elif ID == 46524085:
            osteo.weaponData(Kills, Precision)
        elif ID == 204878059:
            malfease.weaponData(Kills, Precision)
        elif ID == 370712896:
            salvation.weaponData(Kills, Precision)
        elif ID == 374573733:
            delicate.weaponData(Kills, Precision)
        elif ID == 400096939:
            outbreak.weaponData(Kills, Precision)
        elif ID == 417164956:
            jotunn.weaponData(Kills, Precision)
        elif ID == 449318888:
            determine.weaponData(Kills, Precision)
        elif ID == 776191470:
            tommys.weaponData(Kills, Precision)
        elif ID == 814876684:
            wish.weaponData(Kills, Precision)
        elif ID == 814876685:
            trinity.weaponData(Kills, Precision)
        elif ID == 1345867570:
            sweetBusiness.weaponData(Kills, Precision)
        elif ID == 1345867571:
            coldheart.weaponData(Kills, Precision)
        elif ID == 1363238943:
            ruinous.weaponData(Kills, Precision)
        elif ID == 1363886209:
            gjallar.weaponData(Kills, Precision)
        elif ID == 1395261499:
            xeno.weaponData(Kills, Precision)
        elif ID == 1441805468:
            navigator.weaponData(Kills, Precision)
        elif ID == 1473821207:
            revision.weaponData(Kills, Precision)
        elif ID == 1508896098:
            wardcliff.weaponData(Kills, Precision)
        elif ID == 1594120904:
            notime.weaponData(Kills, Precision)
        elif ID == 1665952087:
            fourthhorse.weaponData(Kills, Precision)
        elif ID == 1763584999:
            overture.weaponData(Kills, Precision)
        elif ID == 1833195496:
            agers.weaponData(Kills, Precision)
        elif ID == 1912669214:
            centrifuse.weaponData(Kills, Precision)
        elif ID == 2044500762:
            queenbreak.weaponData(Kills, Precision)
        elif ID == 2130065553:
            arbalest.weaponData(Kills, Precision)
        elif ID == 2179048386:
            forerunner.weaponData(Kills, Precision)
        elif ID == 2286143274:
            huckle.weaponData(Kills, Precision)
        elif ID == 2362471601:
            ratKing.weaponData(Kills, Precision)
        elif ID == 2376481550:
            anarchy.weaponData(Kills, Precision)
        elif ID == 2399110176:
            eyesof.weaponData(Kills, Precision)
        elif ID == 2415517654:
            bastion.weaponData(Kills, Precision)
        elif ID == 2603483885:
            cloudstrike.weaponData(Kills, Precision)
        elif ID == 2907129556:
            strum.weaponData(Kills, Precision)
        elif ID == 3110698812:
            tarrabah.weaponData(Kills, Precision)
        elif ID == 3118061004:
            winterbite.weaponData(Kills, Precision)
        elif ID == 3121540812:
            warning.weaponData(Kills, Precision)
        elif ID == 3141979347:
            bore.weaponData(Kills, Precision)
        elif ID == 3211806999:
            izan.weaponData(Kills, Precision)
        elif ID == 3371017761:
            finality.weaponData(Kills, Precision)
        elif ID == 3505113722:
            obligation.weaponData(Kills, Precision)
        elif ID == 3512014804:
            lumina.weaponData(Kills, Precision)
        elif ID == 3580904580 or ID == 1744115122:
            acrius.weaponData(Kills, Precision)
        elif ID == 3761898871:
            driver.weaponData(Kills, Precision)
        elif ID == 3766045777:
            black.weaponData(Kills, Precision)
        elif ID == 3824106094:
            devil.weaponData(Kills, Precision)
        elif ID == 3844694310:
            rabbit.weaponData(Kills, Precision)
        elif ID == 3856705927:
            hawkmoon.weaponData(Kills, Precision)
        elif ID == 3899270607:
            colony.weaponData(Kills, Precision)
        elif ID == 4174431791:
            hierarchy.weaponData(Kills, Precision)
        elif ID == 4289226715:
            mythoclast.weaponData(Kills, Precision)
        elif ID == 14194600:
            intent.weaponData(Kills, Precision)
        elif ID == 219145368:
            manticore.weaponData(Kills, Precision)
        elif ID == 347366834:
            ace.weaponData(Kills, Precision)
        elif ID == 940371471:
            wicked.weaponData(Kills, Precision)
        elif ID == 1201830623:
            truth.weaponData(Kills, Precision)
        elif ID == 1234150730:
            trespass.weaponData(Kills, Precision)
        elif ID == 1331482397:
            mida.weaponData(Kills, Precision)
        elif ID == 1364093401:
            lastword.weaponData(Kills, Precision)
        elif ID == 1541131350:
            cerberus.weaponData(Kills, Precision)
        elif ID == 1802135586:
            touch.weaponData(Kills, Precision)
        elif ID == 1852863732:
            wavesplit.weaponData(Kills, Precision)
        elif ID == 1853180924:
            chosen.weaponData(Kills, Precision)
        elif ID == 1864563948:
            worldline.weaponData(Kills, Precision)
        elif ID == 1891561814:
            whisper.weaponData(Kills, Precision)
        elif ID == 2069224589:
            thousand.weaponData(Kills, Precision)
        elif ID == 2084878005:
            heir.weaponData(Kills, Precision)
        elif ID == 4103414242:
            divinity.weaponData(Kills, Precision)
        elif ID == 603721696:
            cryo.weaponData(Kills, Precision)
        elif ID == 4190156464:
            merciless.weaponData(Kills, Precision)
        elif ID == 3549153978:
            fighting.weaponData(Kills, Precision)

    Primary = PrettyTable()
    Primary.add_column("Exotic", ["Sweet Business", "Strum", "Vigilance Wing", "Rat King", "MIDA Multi-Tool", "Crimson",
                                  "The Jade Rabbit", "The Huckleberry", "SUROS Regime", "Cerberus+1", "Wish-Ender",
                                  "Malfeasance", "Ace of Spades", "The Last Word", "Thorn", "Outbreak Perfected",
                                  "Lumina", "Bad Juju", "Monte Carlo", "Traveler's Chosen", "Hawkmoon",
                                  "No Time to Explain",
                                  "Dead Man's Tale", "Cryosthethesia 77K", "Osteo Striga", "Touch of Malice",
                                  "Quicksilver Storm", "Revision Zero", "Final Warning", "Verglas Curve",
                                  "Wicked Implement",
                                  "Fighting Lion", "Sunshot", "Skyburner's Oath", 'Graviton Lance', "Riskrunner",
                                  "Hard Light",
                                  "Polaris Lance",
                                  "Trinity Ghoul", "Le Monarque", "Tarrabah", "Symmetry", "Devil's Ruin",
                                  "Tommy's Matchbook",
                                  "Ticuu's Divination", "Vex Mythoclast", "Collective Obligation", "Trespasser",
                                  "The Manticore", "Hierarchy of Needs", "Centrifuse"])
    Primary.add_column("Element",
                       ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                        "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                        "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis",
                        "Kinetic", "Kinetic", "Kinetic/Strand", "Kinetic", "Strand", "Stasis", "Stasis",
                        "Void", "Solar", "Solar", 'Void', "Arc", "Arc/Void/Solar", "Solar", "Arc", "Void", "Solar",
                        "Arc", "Solar", "Solar", "Solar", "Solar", "Void", "Arc", "Void", "Solar", "Arc"])
    Primary.add_column("Weapon Type", ["Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sidearm", "Scout Rifle",
                                       "Hand Cannon", "Scout Rifle", "Submachine Gun", "Auto Rifle", "Auto Rifle",
                                       "Combat Bow", "Hand Cannon", "Hand Cannon", "Hand Cannon", "Hand Cannon",
                                       "Pulse Rifle", "Hand Cannon", "Pulse Rifle", "Auto Rifle", "Sidearm",
                                       "Hand Cannon", "Pulse Rifle", "Scout Rifle", "Sidearm", "Submachine Gun",
                                       "Scout Rifle", "Auto Rifle", "Pulse Rifle", "Sidearm", "Combat Bow",
                                       "Scout Rifle", "Grenade Launcher", "Hand Cannon", "Scout Rifle", 'Pulse Rifle',
                                       "Submachine Gun", "Auto Rifle", "Scout Rifle", "Combat Bow", "Combat Bow",
                                       "Submachine Gun", "Scout Rifle", "Sidearm", "Auto Rifle", "Combat Bow",
                                       "Fusion Rifle", "Pulse Rifle", "Sidearm", "Submachine Gun", "Combat Bow",
                                       "Auto Rifle"])
    Primary.add_column("Kills",
                       [sweetBusiness.kills, strum.kills, vigilance.kills, ratKing.kills, mida.kills, crimson.kills,
                        rabbit.kills,
                        huckle.kills, suros.kills, cerberus.kills, wish.kills, malfease.kills, ace.kills,
                        lastword.kills, thorn.kills, outbreak.kills, lumina.kills, juju.kills, monte.kills,
                        chosen.kills, hawkmoon.kills, notime.kills, deadmans.kills, cryo.kills, osteo.kills, touch.kills,
                        quicksilver.kills, revision.kills, warning.kills, verglas.kills, wicked.kills, fighting.kills,
                        sunshot.kills, skyburner.kills, graviton.kills, riskrunner.kills, hardlight.kills, polaris.kills,
                        trinity.kills, lemon.kills, tarrabah.kills, symmetry.kills, devil.kills, tommys.kills, ticuu.kills,
                        mythoclast.kills, obligation.kills, trespass.kills, manticore.kills, hierarchy.kills, centrifuse.kills])
    Primary.add_column("Precision Kills",
                       [sweetBusiness.prec, strum.prec, vigilance.prec, ratKing.prec, mida.prec, crimson.prec,
                        rabbit.prec, huckle.prec, suros.prec, cerberus.prec, wish.prec, malfease.prec, ace.prec,
                        lastword.prec, thorn.prec, outbreak.prec, lumina.prec, juju.prec, monte.prec, chosen.prec,
                        hawkmoon.prec, notime.prec, deadmans.prec, cryo.prec, osteo.prec, touch.prec,
                        quicksilver.prec, revision.prec, warning.prec, verglas.prec, wicked.prec, fighting.prec,
                        sunshot.prec, skyburner.prec, graviton.prec, riskrunner.prec, hardlight.prec, polaris.prec,
                        trinity.prec, lemon.prec, tarrabah.prec, symmetry.prec, devil.prec, tommys.prec, ticuu.prec,
                        mythoclast.prec, obligation.prec, trespass.prec, manticore.prec, hierarchy.prec, centrifuse.prec])
    Primary.align["Exotic"] = 'l'
    Primary.align["Element"] = 'l'
    Primary.align["Weapon Type"] = 'l'
    Primary.align["Kills"] = 'r'
    Primary.align["Precision Kills"] = 'r'
    Primary.reversesort = True
    print(Primary.get_string(sortby="Kills", start=0, end=5))

    Special = PrettyTable()
    Special.add_column("Exotic",
                       ["The Chaperone", "Izanagi's Burden", "Arbalest", "Bastion", "Witherhoard", "Ager's Scepter",
                        "Forerunner", "Conditional Finality", "The Navigator", "Coldheart", "Merciless", "Borealis",
                        "Prometheus Lens", "Telesto", "Wavesplitter", "Lord of Wolves", "Jötunn", "Eriana's Vow",
                        "Divinity", "The Fourth Horseman", "Ruinous Effigy", "Duality", "Cloudstrike",
                        "Lorentz Driver", "Edge of Intent",
                        "Dead Messenger", "Delicate Tomb", "Vexcalibur"])
    Special.add_column("Element", ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis", "Kinetic",
                                   "Stasis/Solar", "Strand", "Arc", "Solar", "Arc/Void/Solar", "Solar", "Void", "Void",
                                   "Solar", "Solar", "Solar", "Arc", "Arc", "Void", "Solar", "Arc", "Void", "Solar", "Arc/Void/Solar", "Arc", "Void"])
    Special.add_column("Weapon Type", ["Shotgun", "Sniper Rifle", "Linear Fusion Rifle", "Fusion Rifle",
                                       "Grenade Launcher", "Trace Rifle", "Sidearm", "Shotgun", "Trace Rifle",
                                       "Trace Rifle", "Fusion Rifle", "Sniper Rifle", "Trace Rifle", "Fusion Rifle",
                                       "Trace Rifle", "Shotgun", "Fusion Rifle", "Hand Cannon", "Trace Rifle",
                                       "Shotgun", "Trace Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle",
                                       "Glaive", "Grenade Launcher", "Fusion Rifle", "Glaive"])
    Special.add_column("Kills",
                       [chaperone.kills, izan.kills, arbalest.kills, bastion.kills, witherhoard.kills, agers.kills,
                        forerunner.kills, finality.kills, navigator.kills, coldheart.kills, merciless.kills, bore.kills,
                        prometheus.kills,
                        telesto.kills, wavesplit.kills, lordofwolves.kills, jotunn.kills, eriana.kills, divinity.kills,
                        fourthhorse.kills, ruinous.kills, duality.kills, cloudstrike.kills, driver.kills,
                        intent.kills, messenger.kills, delicate.kills, vexcal.kills])
    Special.add_column("Precision Kills",
                       [chaperone.prec, izan.prec, arbalest.prec, bastion.prec, witherhoard.prec, agers.prec, forerunner.prec,
                        finality.prec, navigator.prec, coldheart.prec, merciless.prec, bore.prec,
                        prometheus.prec, telesto.prec, wavesplit.prec, lordofwolves.prec, jotunn.prec, eriana.prec,
                        divinity.prec, fourthhorse.prec, ruinous.prec, duality.prec, cloudstrike.prec, driver.prec,
                        intent.prec, messenger.prec, delicate.prec, vexcal.prec])
    Special.align["Exotic"] = 'l'
    Special.align["Element"] = 'l'
    Special.align["Weapon Type"] = 'l'
    Special.align["Kills"] = 'r'
    Special.align["Precision Kills"] = 'r'
    Special.reversesort = True
    print(Special.get_string(sortby="Kills", start=0, end=5))

    Heavy = PrettyTable()
    Heavy.add_column("Exotic",
                     ["The Wardcliff Coil", "Tractor Cannon", "Legend of Acrius", "D.A.R.C.I.",
                      "The Colony", "Worldline Zero", "Sleeper Simulant", "One Thousand Voices", "Two-Tailed Fox",
                      "Black Talon", "The Queenbreaker", "Thunderlord", "Anarchy", "Leviathan's Breath",
                      "Xenophage", "Deathbringer", "Heir Apparent", "Salvation's Grip", "Eyes of Tomorrow",
                      "The Lament", "Gjallarhorn", "Parasite", "Grand Overture", "Heartshadow",
                      "Deterministic Chaos", "Winterbite", "Truth", "Whisper of the Worm"])
    Heavy.add_column("Element", ["Arc", "Void", "Arc", "Arc", "Void", "Arc", "Solar", "Solar", "Arc/Void/Solar",
                                 "Void", "Arc", "Arc", "Arc", "Void", "Solar", "Void", "Solar", "Stasis", "Solar",
                                 "Solar", "Solar", "Solar", "Arc", "Void", "Void", "Stasis", "Void", "Void"])
    Heavy.add_column("Weapon Type", ["Rocket Launcher", "Shotgun", "Shotgun", "Sniper Rifle",
                                     "Grenade Launcher", "Sword", "Linear Fusion Rifle", "Fusion Rifle",
                                     "Rocket Launcher", "Sword", "Linear Fusion Rifle", "Machine Gun",
                                     "Grenade Launcher", "Combat Bow", "Machine Gun", "Rocket Launcher", "Machine Gun",
                                     "Grenade Launcher", "Rocket Launcher", "Sword", "Rocket Launcher",
                                     "Grenade Launcher", "Machine Gun", "Sword", "Machine Gun", "Glaive",
                                     "Rocket Launcher", "Sniper Rifle"])
    Heavy.add_column("Kills",
                     [wardcliff.kills, tractor.kills, acrius.kills, darci.kills, colony.kills,
                      worldline.kills, sleeper.kills, thousand.kills, twotailed.kills, black.kills, queenbreak.kills,
                      thunderlord.kills,
                      anarchy.kills, leviathan.kills, xeno.kills, deathbringer.kills, heir.kills, salvation.kills,
                      eyesof.kills, lament.kills, gjallar.kills, parasite.kills, overture.kills, heartshadow.kills,
                      determine.kills,
                      winterbite.kills, truth.kills, whisper.kills])
    Heavy.add_column("Precision Kills",
                     [wardcliff.prec, tractor.prec, acrius.prec, darci.prec, colony.prec, worldline.prec,
                      sleeper.prec, thousand.prec, twotailed.prec, black.prec, queenbreak.prec,
                      thunderlord.prec, anarchy.prec, leviathan.prec, xeno.prec, deathbringer.prec, heir.prec, salvation.prec,
                      eyesof.prec, lament.prec, gjallar.prec, parasite.prec, overture.prec,
                      heartshadow.prec, determine.prec, winterbite.prec, truth.prec, whisper.prec])
    Heavy.align["Exotic"] = 'l'
    Heavy.align["Element"] = 'l'
    Heavy.align["Weapon Type"] = 'l'
    Heavy.align["Kills"] = 'r'
    Heavy.align["Precision Kills"] = 'r'
    Heavy.reversesort = True
    print(Heavy.get_string(sortby="Kills", start=0, end=5))

    Full = PrettyTable()
    Full.add_column("Exotic", ["Sweet Business", "Strum", "Vigilance Wing", "Rat King", "MIDA Multi-Tool", "Crimson",
                               "The Jade Rabbit", "The Huckleberry", "SUROS Regime", "Cerberus+1", "Wish-Ender",
                               "Malfeasance", "Ace of Spades", "The Last Word", "Thorn", "Outbreak Perfected",
                               "Lumina", "Bad Juju", "Monte Carlo", "Traveler's Chosen", "Hawkmoon",
                               "No Time to Explain", "Dead Man's Tale", "Cryosthethesia 77K", "Osteo Striga",
                               "Touch of Malice",
                               "Quicksilver Storm", "Revision Zero", "Final Warning", "Verglas Curve",
                               "Wicked Implement", "Fighting Lion", "Sunshot", "Skyburner's Oath", 'Graviton Lance',
                               "Riskrunner", "Hard Light",
                               "Polaris Lance", "Trinity Ghoul", "Le Monarque", "Tarrabah", "Symmetry", "Devil's Ruin",
                               "Tommy's Matchbook", "Ticuu's Divination", "Vex Mythoclast", "Collective Obligation",
                               "Trespasser",
                               "The Manticore", "Hierarchy of Needs", "Centrifuse", "The Chaperone", "Izanagi's Burden",
                               "Arbalest", "Bastion", "Witherhoard", "Ager's Scepter",
                               "Forerunner", "Conditional Finality", "The Navigator", "Coldheart", "Merciless",
                               "Borealis", "Prometheus Lens", "Telesto", "Wavesplitter", "Lord of Wolves", "Jötunn",
                               "Eriana's Vow",
                               "Divinity", "The Fourth Horseman", "Ruinous Effigy", "Duality", "Cloudstrike",
                               "Lorentz Driver", "Edge of Intent",
                               "Dead Messenger", "Delicate Tomb", "Vexcalibur",
                               "The Wardcliff Coil", "Tractor Cannon", "Legend of Acrius", "D.A.R.C.I.",
                               "The Colony", "Worldline Zero", "Sleeper Simulant", "One Thousand Voices",
                               "Two-Tailed Fox", "Black Talon", "The Queenbreaker", "Thunderlord", "Anarchy",
                               "Leviathan's Breath",
                               "Xenophage", "Deathbringer", "Heir Apparent", "Salvation's Grip", "Eyes of Tomorrow",
                               "The Lament", "Gjallarhorn", "Parasite", "Grand Overture", "Heartshadow",
                               "Deterministic Chaos", "Winterbite", "Truth", "Whisper of the Worm"])
    Full.add_column("Element", ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis",
                                "Kinetic", "Kinetic", "Kinetic/Strand", "Kinetic", "Strand", "Stasis", "Stasis",
                                "Void", "Solar", "Solar", 'Void', "Arc", "Arc/Void/Solar", "Solar", "Arc", "Void",
                                "Solar",
                                "Arc", "Solar", "Solar", "Solar", "Solar", "Void", "Arc", "Void", "Solar", "Arc",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis", "Kinetic",
                                "Stasis/Solar", "Strand", "Arc", "Solar", "Arc/Void/Solar", "Solar", "Void", "Void",
                                "Solar", "Solar", "Solar", "Arc", "Arc", "Void", "Solar", "Arc", "Void", "Solar",
                                "Arc/Void/Solar", "Arc", "Void", "Arc", "Void", "Arc", "Arc",
                                "Void", "Arc", "Solar", "Solar", "Arc/Void/Solar",
                                "Void", "Arc", "Arc", "Arc", "Void", "Solar", "Void", "Solar", "Stasis", "Solar",
                                "Solar", "Solar", "Solar", "Arc", "Void", "Void", "Stasis", "Void", "Void"])
    Full.add_column("Weapon Type", ["Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sidearm", "Scout Rifle",
                                    "Hand Cannon", "Scout Rifle", "Submachine Gun", "Auto Rifle", "Auto Rifle",
                                    "Combat Bow", "Hand Cannon", "Hand Cannon", "Hand Cannon", "Hand Cannon",
                                    "Pulse Rifle", "Hand Cannon", "Pulse Rifle", "Auto Rifle", "Sidearm",
                                    "Hand Cannon", "Pulse Rifle", "Scout Rifle", "Sidearm", "Submachine Gun",
                                    "Scout Rifle", "Auto Rifle", "Pulse Rifle", "Sidearm", "Combat Bow",
                                    "Scout Rifle", "Grenade Launcher", "Hand Cannon", "Scout Rifle", 'Pulse Rifle',
                                    "Submachine Gun", "Auto Rifle", "Scout Rifle", "Combat Bow", "Combat Bow",
                                    "Submachine Gun", "Scout Rifle", "Sidearm", "Auto Rifle", "Combat Bow",
                                    "Fusion Rifle", "Pulse Rifle", "Sidearm", "Submachine Gun", "Combat Bow",
                                    "Auto Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle", "Fusion Rifle",
                                    "Grenade Launcher", "Trace Rifle", "Sidearm", "Shotgun", "Trace Rifle",
                                    "Trace Rifle", "Fusion Rifle", "Sniper Rifle", "Trace Rifle", "Fusion Rifle",
                                    "Trace Rifle", "Shotgun", "Fusion Rifle", "Hand Cannon", "Trace Rifle",
                                    "Shotgun", "Trace Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle",
                                    "Glaive", "Grenade Launcher", "Fusion Rifle", "Glaive",
                                    "Rocket Launcher", "Shotgun", "Shotgun", "Sniper Rifle",
                                    "Grenade Launcher", "Sword", "Linear Fusion Rifle", "Fusion Rifle",
                                    "Rocket Launcher", "Sword", "Linear Fusion Rifle", "Machine Gun",
                                    "Grenade Launcher", "Combat Bow", "Machine Gun", "Rocket Launcher", "Machine Gun",
                                    "Grenade Launcher", "Rocket Launcher", "Sword", "Rocket Launcher",
                                    "Grenade Launcher", "Machine Gun", "Sword", "Machine Gun", "Glaive",
                                    "Rocket Launcher", "Sniper Rifle"])
    Full.add_column("Kills",
                    [sweetBusiness.kills, strum.kills, vigilance.kills, ratKing.kills, mida.kills, crimson.kills,
                     rabbit.kills,
                     huckle.kills, suros.kills, cerberus.kills, wish.kills, malfease.kills, ace.kills,
                     lastword.kills, thorn.kills, outbreak.kills, lumina.kills, juju.kills, monte.kills, chosen.kills,
                     hawkmoon.kills, notime.kills, deadmans.kills, cryo.kills, osteo.kills, touch.kills,
                     quicksilver.kills,
                     revision.kills, warning.kills, verglas.kills, wicked.kills, fighting.kills, sunshot.kills,
                     skyburner.kills, graviton.kills, riskrunner.kills, hardlight.kills, polaris.kills, trinity.kills,
                     lemon.kills,
                     tarrabah.kills, symmetry.kills, devil.kills, tommys.kills, ticuu.kills, mythoclast.kills,
                     obligation.kills, trespass.kills, manticore.kills, hierarchy.kills, centrifuse.kills, chaperone.kills,
                     izan.kills, arbalest.kills, bastion.kills, witherhoard.kills, agers.kills, forerunner.kills,
                     finality.kills, navigator.kills, coldheart.kills, merciless.kills, bore.kills, prometheus.kills,
                     telesto.kills, wavesplit.kills, lordofwolves.kills, jotunn.kills, eriana.kills, divinity.kills,
                     fourthhorse.kills, ruinous.kills, duality.kills, cloudstrike.kills, driver.kills, intent.kills,
                     messenger.kills, delicate.kills, vexcal.kills,
                     wardcliff.kills, tractor.kills, acrius.kills, darci.kills, colony.kills, worldline.kills, sleeper.kills,
                     thousand.kills, twotailed.kills, black.kills, queenbreak.kills, thunderlord.kills, anarchy.kills,
                     leviathan.kills, xeno.kills, deathbringer.kills, heir.kills, salvation.kills, eyesof.kills, lament.kills,
                     gjallar.kills, parasite.kills, overture.kills, heartshadow.kills, determine.kills, winterbite.kills,
                     truth.kills, whisper.kills])
    Full.add_column("Precision Kills",
                    [sweetBusiness.prec, strum.prec, vigilance.prec, ratKing.prec, mida.prec, crimson.prec, rabbit.prec,
                     huckle.prec,
                     suros.prec, cerberus.prec, wish.prec, malfease.prec, ace.prec,
                     lastword.prec, thorn.prec, outbreak.prec, lumina.prec, juju.prec, monte.prec, chosen.prec, hawkmoon.prec,
                     notime.prec, deadmans.prec, cryo.prec, osteo.prec, touch.prec,
                     quicksilver.prec, revision.prec, warning.prec, verglas.prec, wicked.prec, fighting.prec, sunshot.prec,
                     skyburner.prec, graviton.prec, riskrunner.prec, hardlight.prec, polaris.prec, trinity.prec, lemon.prec,
                     tarrabah.prec, symmetry.prec, devil.prec, tommys.prec, ticuu.prec, mythoclast.prec, obligation.prec,
                     trespass.prec, manticore.prec, hierarchy.prec, centrifuse.prec, chaperone.prec, izan.prec,
                     arbalest.prec, bastion.prec, witherhoard.prec, agers.prec, forerunner.prec, finality.prec, navigator.prec,
                     coldheart.prec, merciless.prec, bore.prec, prometheus.prec, telesto.prec, wavesplit.prec,
                     lordofwolves.prec, jotunn.prec, eriana.prec, divinity.prec, fourthhorse.prec, ruinous.prec, duality.prec,
                     cloudstrike.prec, driver.prec, intent.prec, messenger.prec,
                     delicate.prec, vexcal.prec, wardcliff.prec, tractor.prec, acrius.prec, darci.prec,
                     colony.prec, worldline.prec, sleeper.prec, thousand.prec, twotailed.prec, black.prec,
                     queenbreak.prec, thunderlord.prec, anarchy.prec, leviathan.prec, xeno.prec, deathbringer.prec, heir.prec,
                     salvation.prec, eyesof.prec, lament.prec, gjallar.prec, parasite.prec, overture.prec,
                     heartshadow.prec, determine.prec, winterbite.prec, truth.prec, whisper.prec])
    Full.align["Exotic"] = 'l'
    Full.align["Element"] = 'l'
    Full.align["Weapon Type"] = 'l'
    Full.align["Kills"] = 'r'
    Full.align["Precision Kills"] = 'r'
    Full.reversesort = True
    print(Full.get_string(sortby="Kills", start=0, end=10))
