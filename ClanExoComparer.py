# Connor Downs
# Started: 7-26-2023
# Last Updated: 8-9-2023
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
    sweetKills = 0
    sweetPrec = 0

    strumKills = 0
    strumPrec = 0

    vigilanceKills = 0
    vigilancePrec = 0

    ratkingKills = 0
    ratkingPrec = 0

    midaKills = 0
    midaPrec = 0

    crimsonKills = 0
    crimsonPrec = 0

    rabbitKills = 0
    rabbitPrec = 0

    huckleKills = 0
    hucklePrec = 0

    surosKills = 0
    surosPrec = 0

    cerberusKills = 0
    cerberusPrec = 0

    wishKills = 0
    wishPrec = 0

    malfeaseKills = 0
    malfeasePrec = 0

    aceKills = 0
    acePrec = 0

    chaperonKills = 0
    chaperonePrec = 0

    izanKills = 0
    izanPrec = 0

    lastwordKills = 0
    lastwordPrec = 0

    arbalestKills = 0
    arbalestPrec = 0

    thornKills = 0
    thornPrec = 0

    outbreakKills = 0
    outbreakPrec = 0

    luminaKills = 0
    luminaPrec = 0

    jujuKills = 0
    jujuPrec = 0

    monteKills = 0
    montePrec = 0

    bastionKills = 0
    bastionPrec = 0

    witherhoardKills = 0
    witherhoardPrec = 0

    chosenKills = 0
    chosenPrec = 0

    hawkmoonKills = 0
    hawkmoonPrec = 0

    notimeKills = 0
    notimePrec = 0

    deadmansKills = 0
    deadmansPrec = 0

    cryoKills = 0
    cryoPrec = 0

    agersKills = 0
    agersPrec = 0

    forerunnerKills = 0
    forerunnerPrec = 0

    osteoKills = 0
    osteoPrec = 0

    touchKills = 0
    touchPrec = 0

    quicksilverKills = 0
    quicksilverPrec = 0

    revisionKills = 0
    revisionPrec = 0

    warningKills = 0
    warningPrec = 0

    finalityKills = 0
    finalityPrec = 0

    verglasKills = 0
    verglasPrec = 0

    wickedKills = 0
    wickedPrec = 0

    navigatorKills = 0
    navigatorPrec = 0

    coldheartKills = 0
    coldheartPrec = 0

    mercilessKills = 0
    mercilessPrec = 0

    fightingKills = 0
    fightingPrec = 0

    sunshotKills = 0
    sunshotPrec = 0

    gravitonKills = 0
    gravitonPrec = 0

    skyburnerKills = 0
    skyburnerPrec = 0

    boreKills = 0
    borePrec = 0

    riskrunnerKills = 0
    riskrunnerPrec = 0

    hardlightKills = 0
    hardlightPrec = 0

    prometheusKills = 0
    prometheusPrec = 0

    telestoKills = 0
    telestoPrec = 0

    polarisKills = 0
    polarisPrec = 0

    trinityKills = 0
    trinityPrec = 0

    wavesplitKills = 0
    wavesplitPrec = 0

    lordofwolvesKills = 0
    lordofwolvesPrec = 0

    lemonKills = 0
    lemonPrec = 0

    jotunnKills = 0
    jotunnPrec = 0

    tarrabahKills = 0
    tarrabahPrec = 0

    erianaKills = 0
    erianaPrec = 0

    divinityKills = 0
    divinityPrec = 0

    symmetryKills = 0
    symmetryPrec = 0

    devilKills = 0
    devilPrec = 0

    tommysKills = 0
    tommysPrec = 0

    fourthhorseKills = 0
    fourthhorsePrec = 0

    ruinousKills = 0
    ruinousPrec = 0

    dualityKills = 0
    dualityPrec = 0

    cloudstrikeKills = 0
    cloudstrikePrec = 0

    ticuuKills = 0
    ticuuPrec = 0

    mythoclastKills = 0
    mythoclastPrec = 0

    driverKills = 0
    driverPrec = 0

    concurrenceKills = 0
    concurrencePrec = 0

    actionKills = 0
    actionPrec = 0

    intentKills = 0
    intentPrec = 0

    messengerKills = 0
    messengerPrec = 0

    obligationKills = 0
    obligationPrec = 0

    delicateKills = 0
    delicatePrec = 0

    trespassKills = 0
    trespassPrec = 0

    manticoreKills = 0
    manticorePrec = 0

    hierarchyKills = 0
    hierarchyPrec = 0

    vexcalKills = 0
    vexcalPrec = 0

    centrifuseKills = 0
    centrifusePrec = 0

    prospectorKills = 0
    prospectorPrec = 0

    wardcliffKills = 0
    wardcliffPrec = 0

    tractorKills = 0
    tractorPrec = 0

    acriusKills = 0
    acriusPrec = 0

    darciKills = 0
    darciPrec = 0

    colonyKills = 0
    colonyPrec = 0

    wordllineKills = 0
    wordllinePrec = 0

    sleeperKills = 0
    sleeperPrec = 0

    thousandKills = 0
    thousandPrec = 0

    twotailedKills = 0
    twotailedPrec = 0

    blackKills = 0
    blackPrec = 0

    queenbreakKills = 0
    queenbreakPrec = 0

    thunderlordKills = 0
    thunderlordPrec = 0

    anarchyKills = 0
    anarchyPrec = 0

    leviathanKills = 0
    leviathanPrec = 0

    xenoKills = 0
    xenoPrec = 0

    deathbringerKills = 0
    deathbringerPrec = 0

    heirKills = 0
    heirPrec = 0

    salvationKills = 0
    salvationPrec = 0

    eyesofKills = 0
    eyesofPrec = 0

    lamentKills = 0
    lamentPrec = 0

    gjallarKills = 0
    gjallarPrec = 0

    parasiteKills = 0
    parasitePrec = 0

    overtureKills = 0
    overturePrec = 0

    heartshadowKills = 0
    heartshadowPrec = 0

    determineKills = 0
    determinePrec = 0

    winterbiteKills = 0
    winterbitePrec = 0

    truthKills = 0
    truthPrec = 0

    whisperKills = 0
    whisperPrec = 0

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
            Exotic = "Telesto"
            telestoKills += Kills
            telestoPrec += Precision
        elif ID == 2232171099:
            Exotic = "Deathbringer"
            deathbringerKills += Kills
            deathbringerPrec += Precision
        elif ID == 2357297366:
            Exotic = "Witherhoard"
            witherhoardKills += Kills
            witherhoardPrec += Precision
        elif ID == 2591746970:
            Exotic = "Leviathan's Breath"
            leviathanKills += Kills
            leviathanPrec += Precision
        elif ID == 2694576561:
            Exotic = "Two-Tailed Fox"
            twotailedKills += Kills
            twotailedPrec += Precision
        elif ID == 2812324400:
            Exotic = "Parasite"
            parasiteKills += Kills
            parasitePrec += Precision
        elif ID == 2812324401:
            Exotic = "Dead Messenger"
            messengerKills += Kills
            messengerPrec += Precision
        elif ID == 2816212794:
            Exotic = "Bad Juju"
            jujuKills += Kills
            jujuPrec += Precision
        elif ID == 2856683562:
            Exotic = "SUROS Regime"
            surosKills += Kills
            surosPrec += Precision
        elif ID == 2907129557:
            Exotic = "Sunshot"
            sunshotKills += Kills
            sunshotPrec += Precision
        elif ID == 3089417789:
            Exotic = "Riskrunner"
            riskrunnerKills += Kills
            riskrunnerPrec += Precision
        elif ID == 3118061005:
            Exotic = "Vexcalibur"
            vexcalKills += Kills
            vexcalPrec += Precision
        elif ID == 3141979346:
            Exotic = "D.A.R.C.I."
            darciKills += Kills
            darciPrec += Precision
        elif ID == 3260753130:
            Exotic = "Ticuu's Divination"
            ticuuKills += Kills
            ticuuPrec += Precision
        elif ID == 3325463374:
            Exotic = "Thunderlord"
            thunderlordKills += Kills
            thunderlordPrec += Precision
        elif ID == 3413074534:
            Exotic = "Polaris Lance"
            polarisKills += Kills
            polarisPrec += Precision
        elif ID == 3413860062:
            Exotic = "The Chaperone"
            chaperonKills += Kills
            chaperonePrec += Precision
        elif ID == 3413860063:
            Exotic = "Lord of Wolves"
            lordofwolvesKills += Kills
            lordofwolvesPrec += Precision
        elif ID == 3437746471:
            Exotic = "Crimson"
            crimsonKills += Kills
            crimsonPrec += Precision
        elif ID == 3460576091:
            Exotic = "Duality"
            dualityKills += Kills
            dualityPrec += Precision
        elif ID == 3487253372:
            Exotic = "The Lament"
            lamentKills += Kills
            lamentPrec += Precision
        elif ID == 3524313097:
            Exotic = "Eriana's Vow"
            erianaKills += Kills
            erianaPrec += Precision
        elif ID == 3580904581:
            Exotic = "Tractor Cannon"
            tractorKills += Kills
            tractorPrec += Precision
        elif ID == 3588934839:
            Exotic = "Le Monarque"
            lemonKills += Kills
            lemonPrec += Precision
        elif ID == 3628991658:
            Exotic = "Graviton Lance"
            gravitonKills += Kills
            gravitonPrec += Precision
        elif ID == 3628991659:
            Exotic = "Vigilance Wing"
            vigilanceKills += Kills
            vigilancePrec += Precision
        elif ID == 3654674561:
            Exotic = "Dead Man's Tale"
            deadmansKills += Kills
            deadmansPrec += Precision
        elif ID == 3659414143:
            Exotic = "Verglas Curve"
            verglasKills += Kills
            verglasPrec += Precision
        elif ID == 3664831848:
            Exotic = "Heartshadow"
            heartshadowKills += Kills
            heartshadowPrec += Precision
        elif ID == 3973202132:
            Exotic = "Thorn"
            thornKills += Kills
            thornPrec += Precision
        elif ID == 4017959782:
            Exotic = "Symmetry"
            symmetryKills += Kills
            symmetryPrec += Precision
        elif ID == 4036115577:
            Exotic = "Sleeper Simulant"
            sleeperKills += Kills
            sleeperPrec += Precision
        elif ID == 4068264807:
            Exotic = "Monte Carlo"
            monteKills += Kills
            montePrec += Precision
        elif ID == 4124984448:
            Exotic = "Hard Light"
            hardlightKills += Kills
            hardlightPrec += Precision
        elif ID == 4255268456:
            Exotic = "Skyburner's Oath"
            skyburnerKills += Kills
            skyburnerPrec += Precision
        elif ID == 4293613902:
            Exotic = "Quicksilver Storm"
            quicksilverKills += Kills
            quicksilverPrec += Precision
        elif ID == 19024058:
            Exotic = "Prometheus Lens"
            prometheusKills += Kills
            prometheusPrec += Precision
        elif ID == 46524085:
            Exotic = "Osteo Striga"
            osteoKills += Kills
            osteoPrec += Precision
        elif ID == 204878059:
            Exotic = "Malfeasance"
            malfeaseKills += Kills
            malfeasePrec += Precision
        elif ID == 370712896:
            Exotic = "Salvation's Grip"
            salvationKills += Kills
            salvationPrec += Precision
        elif ID == 374573733:
            Exotic = "Delicate Tomb"
            delicateKills += Kills
            delicatePrec += Precision
        elif ID == 400096939:
            Exotic = "Outbreak Perfected"
            outbreakKills += Kills
            outbreakPrec += Precision
        elif ID == 417164956:
            Exotic = "Jötunn"
            jotunnKills += Kills
            jotunnPrec += Precision
        elif ID == 449318888:
            Exotic = "Deterministic Chaos"
            determineKills += Kills
            determinePrec += Precision
        elif ID == 776191470:
            Exotic = "Tommy's Matchbook"
            tommysKills += Kills
            tommysPrec += Precision
        elif ID == 814876684:
            Exotic = "Wish-Ender"
            wishKills += Kills
            wishPrec += Precision
        elif ID == 814876685:
            Exotic = "Trinity Ghoul"
            trinityKills += Kills
            trinityPrec += Precision
        elif ID == 1345867570:
            Exotic = "Sweet Business"
            sweetKills += Kills
            sweetPrec += Precision
        elif ID == 1345867571:
            Exotic = "Coldheart"
            coldheartKills += Kills
            coldheartPrec += Precision
        elif ID == 1363238943:
            Exotic = "Ruinous Effigy"
            ruinousKills += Kills
            ruinousPrec += Precision
        elif ID == 1363886209:
            Exotic = "Gjallarhorn"
            gjallarKills += Kills
            gjallarPrec += Precision
        elif ID == 1395261499:
            Exotic = "Xenophage"
            xenoKills += Kills

            xenoPrec += Precision
        elif ID == 1441805468:
            Exotic = "The Navigator"
            navigatorKills += Kills
            navigatorPrec += Precision
        elif ID == 1473821207:
            Exotic = "Revision Zero"
            revisionKills += Kills
            revisionPrec += Precision
        elif ID == 1508896098:
            Exotic = "The Wardcliff Coil"
            wardcliffKills += Kills
            wardcliffPrec += Precision
        elif ID == 1594120904:
            Exotic = "No Time to Explain"
            notimeKills += Kills

            notimePrec += Precision
        elif ID == 1665952087:
            Exotic = "The Fourth Horseman"
            fourthhorseKills += Kills
            fourthhorsePrec += Precision
        elif ID == 1763584999:
            Exotic = "Grand Overture"
            overtureKills += Kills
            overturePrec += Precision
        elif ID == 1833195496:
            Exotic = "Ager's Scepter"
            agersKills += Kills
            agersPrec += Precision
        elif ID == 1912669214:
            Exotic = "Centrifuse"
            centrifuseKills += Kills
            centrifusePrec += Precision
        elif ID == 2044500762:
            Exotic = "The Queenbreaker"
            queenbreakKills += Kills
            queenbreakPrec += Precision
        elif ID == 2130065553:
            Exotic = "Arbalest"
            arbalestKills += Kills
            arbalestPrec += Precision
        elif ID == 2179048386:
            Exotic = "Forerunner"
            forerunnerKills += Kills
            forerunnerPrec += Precision
        elif ID == 2286143274:
            Exotic = "Huckleberry"
            huckleKills += Kills
            hucklePrec += Precision
        elif ID == 2362471601:
            Exotic = "Rat King"
            ratkingKills += Kills
            ratkingPrec += Precision
        elif ID == 2376481550:
            Exotic = "Anarchy"
            anarchyKills += Kills

            anarchyPrec += Precision
        elif ID == 2399110176:
            Exotic = "Eyes of Tomorrow"
            eyesofKills += Kills
            eyesofPrec += Precision
        elif ID == 2415517654:
            Exotic = "Bastion"
            bastionKills += Kills
            bastionPrec += Precision
        elif ID == 2603483885:
            Exotic = "Cloudstrike"
            cloudstrikeKills += Kills
            cloudstrikePrec += Precision
        elif ID == 2907129556:
            Exotic = "Strum"
            strumKills += Kills
            strumPrec += Precision
        elif ID == 3110698812:
            Exotic = "Tarrabah"
            tarrabahKills += Kills
            tarrabahPrec += Precision
        elif ID == 3118061004:
            Exotic = "Winterbite"
            winterbiteKills += Kills
            winterbitePrec += Precision
        elif ID == 3121540812:
            Exotic = "Final Warning"
            warningKills += Kills
            warningPrec += Precision
        elif ID == 3141979347:
            Exotic = "Borealis"
            boreKills += Kills
            borePrec += Precision
        elif ID == 3211806999:
            Exotic = "Izanagi's Burden"
            izanKills += Kills
            izanPrec += Precision
        elif ID == 3371017761:
            Exotic = "Conditional Finality"
            finalityKills += Kills
            finalityPrec += Precision
        elif ID == 3505113722:
            Exotic = "Collective Obligation"
            obligationKills += Kills
            obligationPrec += Precision
        elif ID == 3512014804:
            Exotic = "Lumina"
            luminaKills += Kills
            luminaPrec += Precision
        elif ID == 3580904580 or ID == 1744115122:
            Exotic = "Legend of Acrius"
            acriusKills += Kills
            acriusPrec += Precision
        elif ID == 3761898871:
            Exotic = "Lorentz Driver"
            driverKills += Kills
            driverPrec += Precision
        elif ID == 3766045777:
            Exotic = "Black Talon"
            blackKills += Kills
            blackPrec += Precision
        elif ID == 3824106094:
            Exotic = "Devil's Ruin"
            devilKills += Kills
            devilPrec += Precision
        elif ID == 3844694310:
            Exotic = "The Jade Rabbit"
            rabbitKills += Kills
            rabbitPrec += Precision
        elif ID == 3856705927:
            Exotic = "Hawkmoon"
            hawkmoonKills += Kills
            hawkmoonPrec += Precision
        elif ID == 3899270607:
            Exotic = "The Colony"
            colonyKills += Kills
            colonyPrec += Precision
        elif ID == 4174431791:
            Exotic = "Hierarchy of Needs"
            hierarchyKills += Kills
            hierarchyPrec += Precision
        elif ID == 4289226715:
            Exotic = "Vex Mythoclast"
            mythoclastKills += Kills
            mythoclastPrec += Precision
        elif ID == 14194600:
            Exotic = "Edge of Intent"
            intentKills += Kills
            intentPrec += Precision
        elif ID == 219145368:
            Exotic = "The Manticore"
            manticoreKills += Kills
            manticorePrec += Precision
        elif ID == 347366834:
            Exotic = "Ace of Spades"
            aceKills += Kills
            acePrec += Precision
        elif ID == 940371471:
            Exotic = "Wicked Implement"
            wickedKills += Kills
            wickedPrec += Precision
        elif ID == 1201830623:
            Exotic = "Truth"
            truthKills += Kills
            truthPrec += Precision
        elif ID == 1234150730:
            Exotic = "Trespasser"
            trespassKills += Kills
            trespassPrec += Precision
        elif ID == 1331482397:
            Exotic = "MIDA Multi-Tool"
            midaKills += Kills
            midaPrec += Precision
        elif ID == 1364093401:
            Exotic = "The Last Word"
            lastwordKills += Kills
            lastwordPrec += Precision
        elif ID == 1541131350:
            Exotic = "Cerberus+1"
            cerberusKills += Kills
            cerberusPrec += Precision
        elif ID == 1802135586:
            Exotic = "Touch of Malice"
            touchKills += Kills
            touchPrec += Precision
        elif ID == 1852863732:
            Exotic = "Wavesplitter"
            wavesplitKills += Kills
            wavesplitPrec += Precision
        elif ID == 1853180924:
            Exotic = "Traveler's Chosen"
            chosenKills += Kills
            chosenPrec += Precision
        elif ID == 1864563948:
            Exotic = "Worldline Zero"
            wordllineKills += Kills
            wordllinePrec += Precision
        elif ID == 1891561814:
            Exotic = "Whisper of the Worm"
            whisperKills += Kills
            whisperPrec += Precision
        elif ID == 2069224589:
            Exotic = "One Thousand Voices"
            thousandKills += Kills
            thousandPrec += Precision
        elif ID == 2084878005:
            Exotic = "Heir Apparent"
            heirKills += Kills
            heirPrec += Precision
        elif ID == 4103414242:
            Exotic = 'Divinity'
            divinityKills += Kills
            divinityPrec += Precision
        elif ID == 603721696:
            Exotic = 'Cryosthethesia 77K'
            cryoKills += Kills
            cryoPrec += Precision
        elif ID == 4190156464:
            Exotic = "Merciless"
            mercilessKills += Kills
            mercilessPrec += Precision
        elif ID == 3549153978:
            Exotic = 'Fighting Lion'
            fightingKills += Kills
            fightingPrec += Precision

    Primary = PrettyTable()
    Primary.add_column("Exotic", ["Sweet Business", "Strum", "Vigilance Wing", "Rat King", "MIDA Multi-Tool", "Crimson",
                                  "The Jade Rabbit", "The Huckleberry", "SUROS Regime", "Cerberus+1", "Wish-Ender",
                                  "Malfeasance", "Ace of Spades", "The Last Word", "Thorn", "Outbreak Perfected",
                                  "Lumina", "Bad Juju", "Monte Carlo", "Traveler's Chosen", "Hawkmoon",
                                  "No Time to Explain",
                                  "Dead Man's Tale", "Cryosthethesia 77K", "Osteo Striga", "Touch of Malice",
                                  "Quicksilver Storm", "Revision Zero", "Final Warning", "Verglas Curve",
                                  "Wicked Implement",
                                  "Fighting Lion", "Sunshot", "Skyburner's Oath", "Riskrunner", "Hard Light",
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
                        "Void", "Solar", "Solar", "Arc", "Arc/Void/Solar", "Solar", "Arc", "Void", "Solar",
                        "Arc", "Solar", "Solar", "Solar", "Solar", "Void", "Arc", "Void", "Solar", "Arc"])
    Primary.add_column("Weapon Type", ["Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sidearm", "Scout Rifle",
                                       "Hand Cannon", "Scout Rifle", "Submachine Gun", "Auto Rifle", "Auto Rifle",
                                       "Combat Bow", "Hand Cannon", "Hand Cannon", "Hand Cannon", "Hand Cannon",
                                       "Pulse Rifle", "Hand Cannon", "Pulse Rifle", "Auto Rifle", "Sidearm",
                                       "Hand Cannon", "Pulse Rifle", "Scout Rifle", "Sidearm", "Submachine Gun",
                                       "Scout Rifle", "Auto Rifle", "Pulse Rifle", "Sidearm", "Combat Bow",
                                       "Scout Rifle", "Grenade Launcher", "Hand Cannon", "Scout Rifle",
                                       "Submachine Gun", "Auto Rifle", "Scout Rifle", "Combat Bow", "Combat Bow",
                                       "Submachine Gun", "Scout Rifle", "Sidearm", "Auto Rifle", "Combat Bow",
                                       "Fusion Rifle", "Pulse Rifle", "Sidearm", "Submachine Gun", "Combat Bow",
                                       "Auto Rifle"])
    Primary.add_column("Kills",
                       [sweetKills, strumKills, vigilanceKills, ratkingKills, midaKills, crimsonKills, rabbitKills,
                        huckleKills, surosKills, cerberusKills, wishKills, malfeaseKills, aceKills,
                        lastwordKills, thornKills, outbreakKills, luminaKills, jujuKills, monteKills, chosenKills,
                        hawkmoonKills, notimeKills, deadmansKills, cryoKills, osteoKills, touchKills,
                        quicksilverKills, revisionKills, warningKills, verglasKills, wickedKills, fightingKills,
                        sunshotKills, skyburnerKills, riskrunnerKills, hardlightKills, polarisKills, trinityKills,
                        lemonKills,
                        tarrabahKills, symmetryKills, devilKills, tommysKills, ticuuKills, mythoclastKills,
                        obligationKills, trespassKills, manticoreKills, hierarchyKills, centrifuseKills])
    Primary.add_column("Precision Kills",
                       [sweetPrec, strumPrec, vigilancePrec, ratkingPrec, midaPrec, crimsonPrec, rabbitPrec, hucklePrec,
                        surosPrec, cerberusPrec, wishPrec, malfeasePrec, acePrec,
                        lastwordPrec, thornPrec, outbreakPrec, luminaPrec, jujuPrec, montePrec, chosenPrec,
                        hawkmoonPrec, notimePrec, deadmansPrec, cryoPrec, osteoPrec, touchPrec,
                        quicksilverPrec, revisionPrec, warningPrec, verglasPrec, wickedPrec, fightingPrec, sunshotPrec,
                        skyburnerPrec, riskrunnerPrec, hardlightPrec, polarisPrec, trinityPrec, lemonPrec,
                        tarrabahPrec, symmetryPrec, devilPrec, tommysPrec, ticuuPrec, mythoclastPrec, obligationPrec,
                        trespassPrec, manticorePrec, hierarchyPrec, centrifusePrec])
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
                        "Lorentz Driver", "Edge of Concurrence", "Edge of Action", "Edge of Intent",
                        "Dead Messenger", "Delicate Tomb", "Vexcalibur"])
    Special.add_column("Element", ["Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis", "Kinetic",
                                   "Stasis/Solar", "Strand", "Arc", "Solar", "Arc/Void/Solar", "Solar", "Void", "Void",
                                   "Solar", "Solar", "Solar", "Arc", "Arc", "Void", "Solar", "Arc", "Void", "Arc",
                                   "Void", "Solar", "Arc/Void/Solar", "Arc", "Void"])
    Special.add_column("Weapon Type", ["Shotgun", "Sniper Rifle", "Linear Fusion Rifle", "Fusion Rifle",
                                       "Grenade Launcher", "Trace Rifle", "Sidearm", "Shotgun", "Trace Rifle",
                                       "Trace Rifle", "Fusion Rifle", "Sniper Rifle", "Trace Rifle", "Fusion Rifle",
                                       "Trace Rifle", "Shotgun", "Fusion Rifle", "Hand Cannon", "Trace Rifle",
                                       "Shotgun", "Trace Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle",
                                       "Glaive", "Glaive", "Glaive", "Grenade Launcher", "Fusion Rifle", "Glaive"])
    Special.add_column("Kills",
                       [chaperonKills, izanKills, arbalestKills, bastionKills, witherhoardKills, agersKills,
                        forerunnerKills, finalityKills, navigatorKills, coldheartKills, mercilessKills, boreKills,
                        prometheusKills,
                        telestoKills, wavesplitKills, lordofwolvesKills, jotunnKills, erianaKills, divinityKills,
                        fourthhorseKills, ruinousKills, dualityKills, cloudstrikeKills, driverKills, concurrenceKills,
                        actionKills,
                        intentKills, messengerKills, delicateKills, vexcalKills])
    Special.add_column("Precision Kills",
                       [chaperonePrec, izanPrec, arbalestPrec, bastionPrec, witherhoardPrec, agersPrec, forerunnerPrec,
                        finalityPrec, navigatorPrec, coldheartPrec, mercilessPrec, borePrec,
                        prometheusPrec, telestoPrec, wavesplitPrec, lordofwolvesPrec, jotunnPrec, erianaPrec,
                        divinityPrec, fourthhorsePrec, ruinousPrec, dualityPrec, cloudstrikePrec, driverPrec,
                        concurrencePrec, actionPrec, intentPrec, messengerPrec, delicatePrec, vexcalPrec])
    Special.align["Exotic"] = 'l'
    Special.align["Element"] = 'l'
    Special.align["Weapon Type"] = 'l'
    Special.align["Kills"] = 'r'
    Special.align["Precision Kills"] = 'r'
    Special.reversesort = True
    print(Special.get_string(sortby="Kills", start=0, end=5))

    Heavy = PrettyTable()
    Heavy.add_column("Exotic",
                     ["The Prospector", "The Wardcliff Coil", "Tractor Cannon", "Legend of Acrius", "D.A.R.C.I.",
                      "The Colony", "Worldline Zero", "Sleeper Simulant", "One Thousand Voices", "Two-Tailed Fox",
                      "Black Talon", "The Queenbreaker", "Thunderlord", "Anarchy", "Leviathan's Breath",
                      "Xenophage", "Deathbringer", "Heir Apparent", "Salvation's Grip", "Eyes of Tomorrow",
                      "The Lament", "Gjallarhorn", "Parasite", "Grand Overture", "Heartshadow",
                      "Deterministic Chaos", "Winterbite", "Truth", "Whisper of the Worm"])
    Heavy.add_column("Element", ["Arc", "Arc", "Void", "Arc", "Arc", "Void", "Arc", "Solar", "Solar", "Arc/Void/Solar",
                                 "Void", "Arc", "Arc", "Arc", "Void", "Solar", "Void", "Solar", "Stasis", "Solar",
                                 "Solar", "Solar", "Solar", "Arc", "Void", "Void", "Stasis", "Void", "Void"])
    Heavy.add_column("Weapon Type", ["Grenade Launcher", "Rocket Launcher", "Shotgun", "Shotgun", "Sniper Rifle",
                                     "Grenade Launcher", "Sword", "Linear Fusion Rifle", "Fusion Rifle",
                                     "Rocket Launcher", "Sword", "Linear Fusion Rifle", "Machine Gun",
                                     "Grenade Launcher", "Combat Bow", "Machine Gun", "Rocket Launcher", "Machine Gun",
                                     "Grenade Launcher", "Rocket Launcher", "Sword", "Rocket Launcher",
                                     "Grenade Launcher", "Machine Gun", "Sword", "Machine Gun", "Glaive",
                                     "Rocket Launcher", "Sniper Rifle"])
    Heavy.add_column("Kills",
                     [prospectorKills, wardcliffKills, tractorKills, acriusKills, darciKills, colonyKills,
                      wordllineKills, sleeperKills, thousandKills, twotailedKills, blackKills, queenbreakKills,
                      thunderlordKills,
                      anarchyKills, leviathanKills, xenoKills, deathbringerKills, heirKills, salvationKills,
                      eyesofKills, lamentKills, gjallarKills, parasiteKills, overtureKills, heartshadowKills,
                      determineKills,
                      winterbiteKills, truthKills, whisperKills])
    Heavy.add_column("Precision Kills",
                     [prospectorPrec, wardcliffPrec, tractorPrec, acriusPrec, darciPrec, colonyPrec, wordllinePrec,
                      sleeperPrec, thousandPrec, twotailedPrec, blackPrec, queenbreakPrec,
                      thunderlordPrec, anarchyPrec, leviathanPrec, xenoPrec, deathbringerPrec, heirPrec, salvationPrec,
                      eyesofPrec, lamentPrec, gjallarPrec, parasitePrec, overturePrec,
                      heartshadowPrec, determinePrec, winterbitePrec, truthPrec, whisperPrec])
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
                               "Wicked Implement", "Fighting Lion", "Sunshot", "Skyburner's Oath", "Riskrunner",
                               "Hard Light",
                               "Polaris Lance", "Trinity Ghoul", "Le Monarque", "Tarrabah", "Symmetry", "Devil's Ruin",
                               "Tommy's Matchbook", "Ticuu's Divination", "Vex Mythoclast", "Collective Obligation",
                               "Trespasser",
                               "The Manticore", "Hierarchy of Needs", "Centrifuse", "The Chaperone", "Izanagi's Burden",
                               "Arbalest", "Bastion", "Witherhoard", "Ager's Scepter",
                               "Forerunner", "Conditional Finality", "The Navigator", "Coldheart", "Merciless",
                               "Borealis", "Prometheus Lens", "Telesto", "Wavesplitter", "Lord of Wolves", "Jötunn",
                               "Eriana's Vow",
                               "Divinity", "The Fourth Horseman", "Ruinous Effigy", "Duality", "Cloudstrike",
                               "Lorentz Driver", "Edge of Concurrence", "Edge of Action", "Edge of Intent",
                               "Dead Messenger", "Delicate Tomb", "Vexcalibur", "The Prospector",
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
                                "Void", "Solar", "Solar", "Arc", "Arc/Void/Solar", "Solar", "Arc", "Void", "Solar",
                                "Arc", "Solar", "Solar", "Solar", "Solar", "Void", "Arc", "Void", "Solar", "Arc",
                                "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Kinetic", "Stasis", "Kinetic",
                                "Stasis/Solar", "Strand", "Arc", "Solar", "Arc/Void/Solar", "Solar", "Void", "Void",
                                "Solar", "Solar", "Solar", "Arc", "Arc", "Void", "Solar", "Arc", "Void", "Arc",
                                "Void", "Solar", "Arc/Void/Solar", "Arc", "Void", "Arc", "Arc", "Void", "Arc", "Arc",
                                "Void", "Arc", "Solar", "Solar", "Arc/Void/Solar",
                                "Void", "Arc", "Arc", "Arc", "Void", "Solar", "Void", "Solar", "Stasis", "Solar",
                                "Solar", "Solar", "Solar", "Arc", "Void", "Void", "Stasis", "Void", "Void"])
    Full.add_column("Weapon Type", ["Auto Rifle", "Hand Cannon", "Pulse Rifle", "Sidearm", "Scout Rifle",
                                    "Hand Cannon", "Scout Rifle", "Submachine Gun", "Auto Rifle", "Auto Rifle",
                                    "Combat Bow", "Hand Cannon", "Hand Cannon", "Hand Cannon", "Hand Cannon",
                                    "Pulse Rifle", "Hand Cannon", "Pulse Rifle", "Auto Rifle", "Sidearm",
                                    "Hand Cannon", "Pulse Rifle", "Scout Rifle", "Sidearm", "Submachine Gun",
                                    "Scout Rifle", "Auto Rifle", "Pulse Rifle", "Sidearm", "Combat Bow",
                                    "Scout Rifle", "Grenade Launcher", "Hand Cannon", "Scout Rifle",
                                    "Submachine Gun", "Auto Rifle", "Scout Rifle", "Combat Bow", "Combat Bow",
                                    "Submachine Gun", "Scout Rifle", "Sidearm", "Auto Rifle", "Combat Bow",
                                    "Fusion Rifle", "Pulse Rifle", "Sidearm", "Submachine Gun", "Combat Bow",
                                    "Auto Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle", "Fusion Rifle",
                                    "Grenade Launcher", "Trace Rifle", "Sidearm", "Shotgun", "Trace Rifle",
                                    "Trace Rifle", "Fusion Rifle", "Sniper Rifle", "Trace Rifle", "Fusion Rifle",
                                    "Trace Rifle", "Shotgun", "Fusion Rifle", "Hand Cannon", "Trace Rifle",
                                    "Shotgun", "Trace Rifle", "Shotgun", "Sniper Rifle", "Linear Fusion Rifle",
                                    "Glaive", "Glaive", "Glaive", "Grenade Launcher", "Fusion Rifle", "Glaive",
                                    "Grenade Launcher", "Rocket Launcher", "Shotgun", "Shotgun", "Sniper Rifle",
                                    "Grenade Launcher", "Sword", "Linear Fusion Rifle", "Fusion Rifle",
                                    "Rocket Launcher", "Sword", "Linear Fusion Rifle", "Machine Gun",
                                    "Grenade Launcher", "Combat Bow", "Machine Gun", "Rocket Launcher", "Machine Gun",
                                    "Grenade Launcher", "Rocket Launcher", "Sword", "Rocket Launcher",
                                    "Grenade Launcher", "Machine Gun", "Sword", "Machine Gun", "Glaive",
                                    "Rocket Launcher", "Sniper Rifle"])
    Full.add_column("Kills",
                    [sweetKills, strumKills, vigilanceKills, ratkingKills, midaKills, crimsonKills, rabbitKills,
                     huckleKills, surosKills, cerberusKills, wishKills, malfeaseKills, aceKills,
                     lastwordKills, thornKills, outbreakKills, luminaKills, jujuKills, monteKills, chosenKills,
                     hawkmoonKills, notimeKills, deadmansKills, cryoKills, osteoKills, touchKills, quicksilverKills,
                     revisionKills, warningKills, verglasKills, wickedKills, fightingKills, sunshotKills,
                     skyburnerKills, riskrunnerKills, hardlightKills, polarisKills, trinityKills, lemonKills,
                     tarrabahKills, symmetryKills,
                     devilKills, tommysKills, ticuuKills, mythoclastKills, obligationKills, trespassKills,
                     manticoreKills, hierarchyKills, centrifuseKills, chaperonKills, izanKills, arbalestKills,
                     bastionKills, witherhoardKills,
                     agersKills, forerunnerKills, finalityKills, navigatorKills, coldheartKills, mercilessKills,
                     boreKills, prometheusKills, telestoKills, wavesplitKills, lordofwolvesKills, jotunnKills,
                     erianaKills, divinityKills,
                     fourthhorseKills, ruinousKills, dualityKills, cloudstrikeKills, driverKills, concurrenceKills,
                     actionKills, intentKills, messengerKills, delicateKills, vexcalKills, prospectorKills,
                     wardcliffKills,
                     tractorKills, acriusKills, darciKills, colonyKills, wordllineKills, sleeperKills, thousandKills,
                     twotailedKills, blackKills, queenbreakKills, thunderlordKills, anarchyKills, leviathanKills,
                     xenoKills,
                     deathbringerKills, heirKills, salvationKills, eyesofKills, lamentKills, gjallarKills,
                     parasiteKills, overtureKills, heartshadowKills, determineKills, winterbiteKills, truthKills,
                     whisperKills])
    Full.add_column("Precision Kills",
                    [sweetPrec, strumPrec, vigilancePrec, ratkingPrec, midaPrec, crimsonPrec, rabbitPrec, hucklePrec,
                     surosPrec, cerberusPrec, wishPrec, malfeasePrec, acePrec,
                     lastwordPrec, thornPrec, outbreakPrec, luminaPrec, jujuPrec, montePrec, chosenPrec, hawkmoonPrec,
                     notimePrec, deadmansPrec, cryoPrec, osteoPrec, touchPrec,
                     quicksilverPrec, revisionPrec, warningPrec, verglasPrec, wickedPrec, fightingPrec, sunshotPrec,
                     skyburnerPrec, riskrunnerPrec, hardlightPrec, polarisPrec, trinityPrec, lemonPrec,
                     tarrabahPrec, symmetryPrec, devilPrec, tommysPrec, ticuuPrec, mythoclastPrec, obligationPrec,
                     trespassPrec, manticorePrec, hierarchyPrec, centrifusePrec, chaperonePrec, izanPrec,
                     arbalestPrec, bastionPrec, witherhoardPrec, agersPrec, forerunnerPrec, finalityPrec, navigatorPrec,
                     coldheartPrec, mercilessPrec, borePrec, prometheusPrec, telestoPrec, wavesplitPrec,
                     lordofwolvesPrec, jotunnPrec, erianaPrec, divinityPrec, fourthhorsePrec, ruinousPrec, dualityPrec,
                     cloudstrikePrec, driverPrec, concurrencePrec, actionPrec, intentPrec, messengerPrec,
                     delicatePrec, vexcalPrec, prospectorPrec, wardcliffPrec, tractorPrec, acriusPrec, darciPrec,
                     colonyPrec, wordllinePrec, sleeperPrec, thousandPrec, twotailedPrec, blackPrec,
                     queenbreakPrec, thunderlordPrec, anarchyPrec, leviathanPrec, xenoPrec, deathbringerPrec, heirPrec,
                     salvationPrec, eyesofPrec, lamentPrec, gjallarPrec, parasitePrec, overturePrec,
                     heartshadowPrec, determinePrec, winterbitePrec, truthPrec, whisperPrec])
    Full.align["Exotic"] = 'l'
    Full.align["Element"] = 'l'
    Full.align["Weapon Type"] = 'l'
    Full.align["Kills"] = 'r'
    Full.align["Precision Kills"] = 'r'
    Full.reversesort = True
    print(Full.get_string(sortby="Kills", start=0, end=10))
