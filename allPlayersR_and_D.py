# Connor Downs
# 7-27-2023
# This program is used with Raid_and_Dungeon to combine all the data of every player in Jötunn Gang.
# The first part of the program is the method of getting the API url call to generate each .json file to then be
# collected, combined, then redivided to get all the necessary values to show all the raid or dungeon info.
# The second part is defining the function allCharsTwoPages, and is split between Raid and Dungeon variables.

import os
import requests
import json
from prettytable import PrettyTable
from Time_Converter import Time_Converter

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
redirect_url = "https://jotncomparer.github.io/"
token_url = "https://www.bungie.net/platform/app/oauth/token"

def URLZero(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_1.json', 'w')
    writeFile.write(char_data)


def URLOne(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_2.json', 'w')
    writeFile.write(char_data)


def URLTwo(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_3.json', 'w')
    writeFile.write(char_data)


def URLThree(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_4.json', 'w')
    writeFile.write(char_data)


def URLFour(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_5.json', 'w')
    writeFile.write(char_data)


def URLFive(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_6.json', 'w')
    writeFile.write(char_data)


def URLSix(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_7.json', 'w')
    writeFile.write(char_data)


def URLSeven(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_8.json', 'w')
    writeFile.write(char_data)


def URLEight(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_9.json', 'w')
    writeFile.write(char_data)


def URLNine(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_10.json', 'w')
    writeFile.write(char_data)


def URLTen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_11.json', 'w')
    writeFile.write(char_data)


def URLEleven(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_12.json', 'w')
    writeFile.write(char_data)


def URLTwelve(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_13.json', 'w')
    writeFile.write(char_data)


def URLThirteen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_14.json', 'w')
    writeFile.write(char_data)


def URLFourteen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_15.json', 'w')
    writeFile.write(char_data)


def URLFifteen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_16.json', 'w')
    writeFile.write(char_data)


def URLSixteen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_17.json', 'w')
    writeFile.write(char_data)


def URLSeventeen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_18.json', 'w')
    writeFile.write(char_data)


def URLEighteen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_19.json', 'w')
    writeFile.write(char_data)


def URLNineteen(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_20.json', 'w')
    writeFile.write(char_data)


def URLTwenty(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_21.json', 'w')
    writeFile.write(char_data)


def URLTwenOne(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_22.json', 'w')
    writeFile.write(char_data)


def URLTwenTwo(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_23.json', 'w')
    writeFile.write(char_data)


def URLTwenThree(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=0"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_24.json', 'w')
    writeFile.write(char_data)


def URLTwenFour(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=1"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_25.json', 'w')
    writeFile.write(char_data)


def URLTwenFive(membershipType, destinyMembershipId, characterId, MODE):
    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=1"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_26.json', 'w')
    writeFile.write(char_data)


def allPlayersR_and_D(MODE):
    if MODE == 4:
        # All Raid Data
        # Totals for all Raids
        Raid_Tot_Start = 0
        Raid_Tot_Comp = 0
        Raid_Tot_Kills = 0
        Raid_Tot_Deaths = 0
        Raid_Tot_Time = 0

        # Total for specific raids
        Levi_Start = 0
        SoS_Start = 0
        EoW_Start = 0
        Crown_Start = 0
        SotP_Start = 0
        LW_Start = 0
        GoS_Start = 0
        DSC_Start = 0
        VoG_Start = 0
        Vow_Start = 0
        KF_Start = 0
        Root_Start = 0

        Levi_Comp = 0
        SotP_Comp = 0
        SoS_Comp = 0
        EoW_Comp = 0
        Crown_Comp = 0
        LW_Comp = 0
        GoS_Comp = 0
        DSC_Comp = 0
        VoG_Comp = 0
        Vow_Comp = 0
        KF_Comp = 0
        Root_Comp = 0

        Levi_Tot_Time = 0
        SoS_Tot_Time = 0
        EoW_Tot_Time = 0
        Crown_Tot_Time = 0
        SotP_Tot_Time = 0
        LW_Tot_Time = 0
        GoS_Tot_Time = 0
        DSC_Tot_Time = 0
        VoG_Tot_Time = 0
        Vow_Tot_Time = 0
        KF_Tot_Time = 0
        Root_Tot_Time = 0

        Levi_Tot_K = 0
        SoS_Tot_K = 0
        EoW_Tot_K = 0
        Crown_Tot_K = 0
        SotP_Tot_K = 0
        LW_Tot_K = 0
        GoS_Tot_K = 0
        DSC_Tot_K = 0
        VoG_Tot_K = 0
        Vow_Tot_K = 0
        KF_Tot_K = 0
        Root_Tot_K = 0

        Levi_Tot_D = 0
        SoS_Tot_D = 0
        EoW_Tot_D = 0
        Crown_Tot_D = 0
        SotP_Tot_D = 0
        LW_Tot_D = 0
        GoS_Tot_D = 0
        DSC_Tot_D = 0
        VoG_Tot_D = 0
        Vow_Tot_D = 0
        KF_Tot_D = 0
        Root_Tot_D = 0

        with open('Char_1.json') as f:
            data1 = json.load(f)
        with open('Char_2.json') as f:
            data2 = json.load(f)
        with open('Char_3.json') as f:
            data3 = json.load(f)
        with open('Char_4.json') as f:
            data4 = json.load(f)
        with open('Char_5.json') as f:
            data5 = json.load(f)
        with open('Char_6.json') as f:
            data6 = json.load(f)
        with open('Char_7.json') as f:
            data7 = json.load(f)
        with open('Char_8.json') as f:
            data8 = json.load(f)
        with open('Char_9.json') as f:
            data9 = json.load(f)
        with open('Char_10.json') as f:
            data10 = json.load(f)
        with open('Char_11.json') as f:
            data11 = json.load(f)
        with open('Char_13.json') as f:
            data13 = json.load(f)
        with open('Char_14.json') as f:
            data14 = json.load(f)
        with open('Char_15.json') as f:
            data15 = json.load(f)
        with open('Char_16.json') as f:
            data16 = json.load(f)
        with open('Char_17.json') as f:
            data17 = json.load(f)
        with open('Char_19.json') as f:
            data19 = json.load(f)
        with open('Char_20.json') as f:
            data20 = json.load(f)
        with open('Char_21.json') as f:
            data21 = json.load(f)
        with open('Char_22.json') as f:
            data22 = json.load(f)
        with open('Char_23.json') as f:
            data23 = json.load(f)
        with open('Char_25.json') as f:
            data25 = json.load(f)
        with open('Char_26.json') as f:
            data26 = json.load(f)

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
        items13 = data13["Response"]
        items14 = data14["Response"]
        items15 = data15["Response"]
        items16 = data16["Response"]
        items17 = data17["Response"]
        items19 = data19["Response"]
        items20 = data20["Response"]
        items21 = data21["Response"]
        items22 = data22["Response"]
        items23 = data23["Response"]
        items25 = data25["Response"]
        items26 = data26["Response"]

        char_json = {"Response": []}

        char_json['Response'].append(items1)
        char_json["Response"].append(items2)
        char_json["Response"].append(items3)
        char_json['Response'].append(items4)
        char_json["Response"].append(items5)
        char_json["Response"].append(items6)
        char_json['Response'].append(items7)
        char_json["Response"].append(items8)
        char_json["Response"].append(items9)
        char_json['Response'].append(items10)
        char_json["Response"].append(items11)
        char_json['Response'].append(items13)
        char_json["Response"].append(items14)
        char_json["Response"].append(items15)
        char_json['Response'].append(items16)
        char_json["Response"].append(items17)
        char_json['Response'].append(items19)
        char_json["Response"].append(items20)
        char_json["Response"].append(items21)
        char_json['Response'].append(items22)
        char_json["Response"].append(items23)
        char_json['Response'].append(items25)
        char_json["Response"].append(items26)

        with open('char.json', "w") as f:
            f.write(json.dumps(char_json, indent=2))

        activities_len_1 = len(char_json["Response"][0]['activities'])
        activities_len_2 = len(char_json["Response"][1]['activities'])
        activities_len_3 = len(char_json["Response"][2]['activities'])
        activities_len_4 = len(char_json["Response"][3]['activities'])
        activities_len_5 = len(char_json["Response"][4]['activities'])
        activities_len_6 = len(char_json["Response"][5]['activities'])
        activities_len_7 = len(char_json["Response"][6]['activities'])
        activities_len_8 = len(char_json["Response"][7]['activities'])
        activities_len_9 = len(char_json["Response"][8]['activities'])
        activities_len_10 = len(char_json["Response"][9]['activities'])
        activities_len_11 = len(char_json["Response"][10]['activities'])
        activities_len_13 = len(char_json["Response"][11]['activities'])
        activities_len_14 = len(char_json["Response"][12]['activities'])
        activities_len_15 = len(char_json["Response"][13]['activities'])
        activities_len_16 = len(char_json["Response"][14]['activities'])
        activities_len_17 = len(char_json["Response"][15]['activities'])
        activities_len_19 = len(char_json["Response"][16]['activities'])
        activities_len_20 = len(char_json["Response"][17]['activities'])
        activities_len_21 = len(char_json["Response"][18]['activities'])
        activities_len_22 = len(char_json["Response"][19]['activities'])
        activities_len_23 = len(char_json["Response"][20]['activities'])
        activities_len_25 = len(char_json["Response"][21]['activities'])
        activities_len_26 = len(char_json["Response"][22]['activities'])

        Raid_Name = {"Raid": []}
        Raid_Kills = {"Kills": []}
        Raid_Deaths = {"Deaths": []}
        Raid_KD = {"K/D": []}
        Raid_KAD = {"KA/D": []}
        Raid_Time = {"Time": []}
        Raid_PlayerCount = {"Player Count": []}
        Raid_Complete = {"Completion": []}

        for number in range(0, activities_len_1):
            Raid_Name_1 = char_json["Response"][0]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_1 = char_json["Response"][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_1 = char_json["Response"][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_1 = \
                char_json["Response"][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_1 = \
                char_json["Response"][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_1 = \
                char_json["Response"][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_1 = \
                char_json["Response"][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_1 = char_json["Response"][0]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_1)
            Raid_Kills['Kills'].append(Raid_Kills_1)
            Raid_Deaths['Deaths'].append(Raid_Deaths_1)
            Raid_KD['K/D'].append(Raid_KD_1)
            Raid_KAD['KA/D'].append(Raid_KAD_1)
            Raid_Time['Time'].append(Raid_Time_1)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_1)
            Raid_Complete['Completion'].append(Raid_Complete_1)
        for number in range(0, activities_len_2):
            Raid_Name_2 = char_json["Response"][1]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_2 = char_json["Response"][1]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_2 = char_json["Response"][1]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_2 = \
                char_json["Response"][1]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_2 = \
                char_json["Response"][1]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_2 = \
                char_json["Response"][1]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_2 = \
                char_json["Response"][1]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_2 = char_json["Response"][1]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_2)
            Raid_Kills['Kills'].append(Raid_Kills_2)
            Raid_Deaths['Deaths'].append(Raid_Deaths_2)
            Raid_KD['K/D'].append(Raid_KD_2)
            Raid_KAD['KA/D'].append(Raid_KAD_2)
            Raid_Time['Time'].append(Raid_Time_2)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_2)
            Raid_Complete['Completion'].append(Raid_Complete_2)
        for number in range(0, activities_len_3):
            Raid_Name_3 = char_json["Response"][2]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_3 = char_json["Response"][2]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_3 = char_json["Response"][2]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_3 = \
                char_json["Response"][2]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_3 = \
                char_json["Response"][2]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_3 = \
                char_json["Response"][2]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_3 = \
                char_json["Response"][2]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_3 = char_json["Response"][2]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_3)
            Raid_Kills['Kills'].append(Raid_Kills_3)
            Raid_Deaths['Deaths'].append(Raid_Deaths_3)
            Raid_KD['K/D'].append(Raid_KD_3)
            Raid_KAD['KA/D'].append(Raid_KAD_3)
            Raid_Time['Time'].append(Raid_Time_3)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_3)
            Raid_Complete['Completion'].append(Raid_Complete_3)
        for number in range(0, activities_len_4):
            Raid_Name_4 = char_json["Response"][3]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_4 = char_json["Response"][3]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_4 = char_json["Response"][3]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_4 = \
                char_json["Response"][3]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_4 = \
                char_json["Response"][3]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_4 = \
                char_json["Response"][3]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_4 = \
                char_json["Response"][3]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_4 = char_json["Response"][3]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_4)
            Raid_Kills['Kills'].append(Raid_Kills_4)
            Raid_Deaths['Deaths'].append(Raid_Deaths_4)
            Raid_KD['K/D'].append(Raid_KD_4)
            Raid_KAD['KA/D'].append(Raid_KAD_4)
            Raid_Time['Time'].append(Raid_Time_4)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_4)
            Raid_Complete['Completion'].append(Raid_Complete_4)
        for number in range(0, activities_len_5):
            Raid_Name_5 = char_json["Response"][4]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_5 = char_json["Response"][4]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_5 = char_json["Response"][4]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_5 = \
                char_json["Response"][4]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_5 = \
                char_json["Response"][4]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_5 = \
                char_json["Response"][4]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_5 = \
                char_json["Response"][4]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_5 = char_json["Response"][4]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_5)
            Raid_Kills['Kills'].append(Raid_Kills_5)
            Raid_Deaths['Deaths'].append(Raid_Deaths_5)
            Raid_KD['K/D'].append(Raid_KD_5)
            Raid_KAD['KA/D'].append(Raid_KAD_5)
            Raid_Time['Time'].append(Raid_Time_5)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_5)
            Raid_Complete['Completion'].append(Raid_Complete_5)
        for number in range(0, activities_len_6):
            Raid_Name_6 = char_json["Response"][5]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_6 = char_json["Response"][5]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_6 = char_json["Response"][5]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_6 = \
                char_json["Response"][5]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_6 = \
                char_json["Response"][5]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_6 = \
                char_json["Response"][5]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_6 = \
                char_json["Response"][5]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_6 = char_json["Response"][5]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_6)
            Raid_Kills['Kills'].append(Raid_Kills_6)
            Raid_Deaths['Deaths'].append(Raid_Deaths_6)
            Raid_KD['K/D'].append(Raid_KD_6)
            Raid_KAD['KA/D'].append(Raid_KAD_6)
            Raid_Time['Time'].append(Raid_Time_6)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_6)
            Raid_Complete['Completion'].append(Raid_Complete_6)
        for number in range(0, activities_len_7):
            Raid_Name_7 = char_json["Response"][6]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_7 = char_json["Response"][6]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_7 = char_json["Response"][6]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_7 = \
                char_json["Response"][6]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_7 = \
                char_json["Response"][6]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_7 = \
                char_json["Response"][6]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_7 = \
                char_json["Response"][6]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_7 = char_json["Response"][6]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_7)
            Raid_Kills['Kills'].append(Raid_Kills_7)
            Raid_Deaths['Deaths'].append(Raid_Deaths_7)
            Raid_KD['K/D'].append(Raid_KD_7)
            Raid_KAD['KA/D'].append(Raid_KAD_7)
            Raid_Time['Time'].append(Raid_Time_7)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_7)
            Raid_Complete['Completion'].append(Raid_Complete_7)
        for number in range(0, activities_len_8):
            Raid_Name_8 = char_json["Response"][7]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_8 = char_json["Response"][7]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_8 = char_json["Response"][7]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_8 = \
                char_json["Response"][7]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_8 = \
                char_json["Response"][7]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_8 = \
                char_json["Response"][7]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_8 = \
                char_json["Response"][7]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_8 = char_json["Response"][7]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_8)
            Raid_Kills['Kills'].append(Raid_Kills_8)
            Raid_Deaths['Deaths'].append(Raid_Deaths_8)
            Raid_KD['K/D'].append(Raid_KD_8)
            Raid_KAD['KA/D'].append(Raid_KAD_8)
            Raid_Time['Time'].append(Raid_Time_8)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_8)
            Raid_Complete['Completion'].append(Raid_Complete_8)
        for number in range(0, activities_len_9):
            Raid_Name_9 = char_json["Response"][8]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_9 = char_json["Response"][8]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_9 = char_json["Response"][8]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_9 = \
                char_json["Response"][8]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_9 = \
                char_json["Response"][8]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_9 = \
                char_json["Response"][8]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_9 = \
                char_json["Response"][8]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_9 = char_json["Response"][8]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_9)
            Raid_Kills['Kills'].append(Raid_Kills_9)
            Raid_Deaths['Deaths'].append(Raid_Deaths_9)
            Raid_KD['K/D'].append(Raid_KD_9)
            Raid_KAD['KA/D'].append(Raid_KAD_9)
            Raid_Time['Time'].append(Raid_Time_9)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_9)
            Raid_Complete['Completion'].append(Raid_Complete_9)
        for number in range(0, activities_len_10):
            Raid_Name_10 = char_json["Response"][9]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_10 = char_json["Response"][9]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_10 = char_json["Response"][9]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_10 = \
                char_json["Response"][9]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_10 = \
                char_json["Response"][9]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_10 = \
                char_json["Response"][9]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_10 = \
                char_json["Response"][9]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_10 = char_json["Response"][9]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_10)
            Raid_Kills['Kills'].append(Raid_Kills_10)
            Raid_Deaths['Deaths'].append(Raid_Deaths_10)
            Raid_KD['K/D'].append(Raid_KD_10)
            Raid_KAD['KA/D'].append(Raid_KAD_10)
            Raid_Time['Time'].append(Raid_Time_10)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_10)
            Raid_Complete['Completion'].append(Raid_Complete_10)
        for number in range(0, activities_len_11):
            Raid_Name_11 = char_json["Response"][10]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_11 = char_json["Response"][10]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_11 = char_json["Response"][10]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_11 = \
                char_json["Response"][10]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_11 = \
                char_json["Response"][10]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_11 = \
                char_json["Response"][10]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_11 = \
                char_json["Response"][10]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_11 = char_json["Response"][10]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_11)
            Raid_Kills['Kills'].append(Raid_Kills_11)
            Raid_Deaths['Deaths'].append(Raid_Deaths_11)
            Raid_KD['K/D'].append(Raid_KD_11)
            Raid_KAD['KA/D'].append(Raid_KAD_11)
            Raid_Time['Time'].append(Raid_Time_11)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_11)
            Raid_Complete['Completion'].append(Raid_Complete_11)
        for number in range(0, activities_len_13):
            Raid_Name_13 = char_json["Response"][11]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_13 = char_json["Response"][11]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_13 = char_json["Response"][11]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_13 = \
                char_json["Response"][11]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_13 = \
                char_json["Response"][11]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_13 = \
                char_json["Response"][11]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_13 = \
                char_json["Response"][11]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_13 = char_json["Response"][11]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_13)
            Raid_Kills['Kills'].append(Raid_Kills_13)
            Raid_Deaths['Deaths'].append(Raid_Deaths_13)
            Raid_KD['K/D'].append(Raid_KD_13)
            Raid_KAD['KA/D'].append(Raid_KAD_13)
            Raid_Time['Time'].append(Raid_Time_13)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_13)
            Raid_Complete['Completion'].append(Raid_Complete_13)
        for number in range(0, activities_len_14):
            Raid_Name_14 = char_json["Response"][12]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_14 = char_json["Response"][12]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_14 = char_json["Response"][12]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_14 = \
                char_json["Response"][12]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_14 = \
                char_json["Response"][12]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_14 = \
                char_json["Response"][12]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_14 = \
                char_json["Response"][12]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_14 = char_json["Response"][12]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_14)
            Raid_Kills['Kills'].append(Raid_Kills_14)
            Raid_Deaths['Deaths'].append(Raid_Deaths_14)
            Raid_KD['K/D'].append(Raid_KD_14)
            Raid_KAD['KA/D'].append(Raid_KAD_14)
            Raid_Time['Time'].append(Raid_Time_14)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_14)
            Raid_Complete['Completion'].append(Raid_Complete_14)
        for number in range(0, activities_len_15):
            Raid_Name_15 = char_json["Response"][13]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_15 = char_json["Response"][13]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_15 = char_json["Response"][13]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_15 = \
                char_json["Response"][13]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_15 = \
                char_json["Response"][13]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_15 = \
                char_json["Response"][13]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_15 = \
                char_json["Response"][13]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_15 = char_json["Response"][13]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_15)
            Raid_Kills['Kills'].append(Raid_Kills_15)
            Raid_Deaths['Deaths'].append(Raid_Deaths_15)
            Raid_KD['K/D'].append(Raid_KD_15)
            Raid_KAD['KA/D'].append(Raid_KAD_15)
            Raid_Time['Time'].append(Raid_Time_15)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_15)
            Raid_Complete['Completion'].append(Raid_Complete_15)
        for number in range(0, activities_len_16):
            Raid_Name_16 = char_json["Response"][14]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_16 = char_json["Response"][14]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_16 = char_json["Response"][14]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_16 = \
                char_json["Response"][14]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_16 = \
                char_json["Response"][14]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_16 = \
                char_json["Response"][14]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_16 = \
                char_json["Response"][14]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_16 = char_json["Response"][14]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_16)
            Raid_Kills['Kills'].append(Raid_Kills_16)
            Raid_Deaths['Deaths'].append(Raid_Deaths_16)
            Raid_KD['K/D'].append(Raid_KD_16)
            Raid_KAD['KA/D'].append(Raid_KAD_16)
            Raid_Time['Time'].append(Raid_Time_16)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_16)
            Raid_Complete['Completion'].append(Raid_Complete_16)
        for number in range(0, activities_len_17):
            Raid_Name_17 = char_json["Response"][15]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_17 = char_json["Response"][15]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_17 = char_json["Response"][15]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_17 = \
                char_json["Response"][15]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_17 = \
                char_json["Response"][15]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_17 = \
                char_json["Response"][15]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_17 = \
                char_json["Response"][15]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_17 = char_json["Response"][15]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_17)
            Raid_Kills['Kills'].append(Raid_Kills_17)
            Raid_Deaths['Deaths'].append(Raid_Deaths_17)
            Raid_KD['K/D'].append(Raid_KD_17)
            Raid_KAD['KA/D'].append(Raid_KAD_17)
            Raid_Time['Time'].append(Raid_Time_17)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_17)
            Raid_Complete['Completion'].append(Raid_Complete_17)
        for number in range(0, activities_len_19):
            Raid_Name_19 = char_json["Response"][16]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_19 = char_json["Response"][16]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_19 = char_json["Response"][16]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_19 = \
                char_json["Response"][16]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_19 = \
                char_json["Response"][16]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_19 = \
                char_json["Response"][16]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_19 = \
                char_json["Response"][16]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_19 = char_json["Response"][16]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_19)
            Raid_Kills['Kills'].append(Raid_Kills_19)
            Raid_Deaths['Deaths'].append(Raid_Deaths_19)
            Raid_KD['K/D'].append(Raid_KD_19)
            Raid_KAD['KA/D'].append(Raid_KAD_19)
            Raid_Time['Time'].append(Raid_Time_19)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_19)
            Raid_Complete['Completion'].append(Raid_Complete_19)
        for number in range(0, activities_len_20):
            Raid_Name_20 = char_json["Response"][17]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_20 = char_json["Response"][17]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_20 = char_json["Response"][17]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_20 = \
                char_json["Response"][17]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_20 = \
                char_json["Response"][17]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_20 = \
                char_json["Response"][17]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_20 = \
                char_json["Response"][17]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_20 = char_json["Response"][17]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_20)
            Raid_Kills['Kills'].append(Raid_Kills_20)
            Raid_Deaths['Deaths'].append(Raid_Deaths_20)
            Raid_KD['K/D'].append(Raid_KD_20)
            Raid_KAD['KA/D'].append(Raid_KAD_20)
            Raid_Time['Time'].append(Raid_Time_20)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_20)
            Raid_Complete['Completion'].append(Raid_Complete_20)
        for number in range(0, activities_len_21):
            Raid_Name_21 = char_json["Response"][18]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_21 = char_json["Response"][18]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_21 = char_json["Response"][18]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_21 = \
                char_json["Response"][18]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_21 = \
                char_json["Response"][18]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_21 = \
                char_json["Response"][18]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_21 = \
                char_json["Response"][18]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_21 = char_json["Response"][18]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_21)
            Raid_Kills['Kills'].append(Raid_Kills_21)
            Raid_Deaths['Deaths'].append(Raid_Deaths_21)
            Raid_KD['K/D'].append(Raid_KD_21)
            Raid_KAD['KA/D'].append(Raid_KAD_21)
            Raid_Time['Time'].append(Raid_Time_21)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_21)
            Raid_Complete['Completion'].append(Raid_Complete_21)
        for number in range(0, activities_len_22):
            Raid_Name_22 = char_json["Response"][19]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_22 = char_json["Response"][19]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_22 = char_json["Response"][19]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_22 = \
                char_json["Response"][19]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_22 = \
                char_json["Response"][19]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_22 = \
                char_json["Response"][19]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_22 = \
                char_json["Response"][19]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_22 = char_json["Response"][19]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_22)
            Raid_Kills['Kills'].append(Raid_Kills_22)
            Raid_Deaths['Deaths'].append(Raid_Deaths_22)
            Raid_KD['K/D'].append(Raid_KD_22)
            Raid_KAD['KA/D'].append(Raid_KAD_22)
            Raid_Time['Time'].append(Raid_Time_22)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_22)
            Raid_Complete['Completion'].append(Raid_Complete_22)
        for number in range(0, activities_len_23):
            Raid_Name_23 = char_json["Response"][20]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_23 = char_json["Response"][20]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_23 = char_json["Response"][20]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_23 = \
                char_json["Response"][20]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_23 = \
                char_json["Response"][20]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_23 = \
                char_json["Response"][20]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_23 = \
                char_json["Response"][20]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_23 = char_json["Response"][20]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_23)
            Raid_Kills['Kills'].append(Raid_Kills_23)
            Raid_Deaths['Deaths'].append(Raid_Deaths_23)
            Raid_KD['K/D'].append(Raid_KD_23)
            Raid_KAD['KA/D'].append(Raid_KAD_23)
            Raid_Time['Time'].append(Raid_Time_23)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_23)
            Raid_Complete['Completion'].append(Raid_Complete_23)
        for number in range(0, activities_len_25):
            Raid_Name_25 = char_json["Response"][21]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_25 = char_json["Response"][21]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_25 = char_json["Response"][21]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_25 = \
                char_json["Response"][21]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_25 = \
                char_json["Response"][21]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_25 = \
                char_json["Response"][21]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_25 = \
                char_json["Response"][21]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_25 = char_json["Response"][21]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_25)
            Raid_Kills['Kills'].append(Raid_Kills_25)
            Raid_Deaths['Deaths'].append(Raid_Deaths_25)
            Raid_KD['K/D'].append(Raid_KD_25)
            Raid_KAD['KA/D'].append(Raid_KAD_25)
            Raid_Time['Time'].append(Raid_Time_25)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_25)
            Raid_Complete['Completion'].append(Raid_Complete_25)
        for number in range(0, activities_len_26):
            Raid_Name_26 = char_json["Response"][22]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_26 = char_json["Response"][22]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_26 = char_json["Response"][22]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_26 = \
                char_json["Response"][22]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Raid_KAD_26 = \
                char_json["Response"][22]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Raid_Time_26 = \
                char_json["Response"][22]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_26 = \
                char_json["Response"][22]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_26 = char_json["Response"][22]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_26)
            Raid_Kills['Kills'].append(Raid_Kills_26)
            Raid_Deaths['Deaths'].append(Raid_Deaths_26)
            Raid_KD['K/D'].append(Raid_KD_26)
            Raid_KAD['KA/D'].append(Raid_KAD_26)
            Raid_Time['Time'].append(Raid_Time_26)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_26)
            Raid_Complete['Completion'].append(Raid_Complete_26)

        Raid_Info = [Raid_Name, Raid_Kills, Raid_Deaths, Raid_KD, Raid_KAD, Raid_Time,
                     Raid_PlayerCount, Raid_Complete]

        length = len(Raid_Info[0]['Raid'])

        for numb in range(0, length):
            Name = Raid_Info[0]['Raid'][numb]
            Kills = Raid_Info[1]['Kills'][numb]
            Deaths = Raid_Info[2]['Deaths'][numb]
            KD = Raid_Info[3]['K/D'][numb]
            KAD = Raid_Info[4]['KA/D'][numb]
            Time = Raid_Info[5]['Time'][numb]
            Players = Raid_Info[6]['Player Count'][numb]
            Completion = Raid_Info[7]['Completion'][numb]

            if Name == 2122313384:
                Name = "Last Wish"
                LW_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    LW_Comp += 1
                    Raid_Tot_Comp += 1
                LW_Tot_Time += Time
                LW_Tot_K += Kills
                LW_Tot_D += Deaths
            elif Name == 3458480158 or Name == 2659723068:
                Name = "Garden of Salvation"
                GoS_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    GoS_Comp += 1
                    Raid_Tot_Comp += 1
                GoS_Tot_Time += Time
                GoS_Tot_K += Kills
                GoS_Tot_D += Deaths
            elif Name == 910380154:
                Name = "Deep Stone Crypt"
                DSC_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    DSC_Comp += 1
                    Raid_Tot_Comp += 1
                DSC_Tot_Time += Time
                DSC_Tot_K += Kills
                DSC_Tot_D += Deaths
            elif Name == 3881495763:
                Name = "Vault of Glass"
                VoG_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    VoG_Comp += 1
                    Raid_Tot_Comp += 1
                VoG_Tot_Time += Time
                VoG_Tot_K += Kills
                VoG_Tot_D += Deaths
            elif Name == 1441982566:
                Name = "Vow of the Disciple"
                Vow_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    Vow_Comp += 1
                    Raid_Tot_Comp += 1
                Vow_Tot_Time += Time
                Vow_Tot_K += Kills
                Vow_Tot_D += Deaths
            elif Name == 1374392663 or Name == 2964135793:
                if Name == 1374392663:
                    Name = "King's Fall"
                elif Name == 2964135793:
                    Name = "King's Fall: Master"
                KF_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    KF_Comp += 1
                    Raid_Tot_Comp += 1
                KF_Tot_Time += Time
                KF_Tot_K += Kills
                KF_Tot_D += Deaths
            elif Name == 2381413764:
                Name = "Root of Nightmares"
                Root_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    Root_Comp += 1
                    Raid_Tot_Comp += 1
                Root_Tot_Time += Time
                Root_Tot_K += Kills
                Root_Tot_D += Deaths
            elif Name == 2693136601 or Name == 2693136604 or Name == 3879860661 or Name == 2693136602 or Name == 2693136603 \
                    or Name == 2693136605 or Name == 2693136600 or Name == 417231112 or \
                    Name == 757116822 or Name == 1685065161:
                if Name == 2693136601 or Name == 2693136604 or Name == 2693136602 or Name == 2693136603 \
                        or Name == 2693136605 or Name == 2693136600:
                    Name = "Leviathan"
                elif Name == 3879860661:
                    Name = "Prestige Leviathan"
                elif Name == 417231112:
                    Name = "Prestige Leviathan"
                elif Name == 757116822:
                    Name = "Prestige Leviathan"
                elif Name == 1685065161:
                    Name = "Prestige Leviathan"
                elif Name == 3446541099:
                    Name = "Prestige Leviathan"
                elif Name == 2449714930:
                    Name = "Prestige Leviathan"
                Levi_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    Levi_Comp += 1
                    Raid_Tot_Comp += 1
                Levi_Tot_Time += Time
                Levi_Tot_K += Kills
                Levi_Tot_D += Deaths
            elif Name == 548750096:
                Name = "Scourge of the Past"
                SotP_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    SotP_Comp += 1
                    Raid_Tot_Comp += 1
                SotP_Tot_Time += Time
                SotP_Tot_K += Kills
                SotP_Tot_D += Deaths
            elif Name == 3333172150:
                Name = "Crown of Sorrow"
                Crown_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    Crown_Comp += 1
                    Raid_Tot_Comp += 1
                Crown_Tot_Time += Time
                Crown_Tot_K += Kills
                Crown_Tot_D += Deaths
            elif Name == 3089205900 or Name == 809170886:
                if Name == 3089205900:
                    Name = "Eater of Worlds"
                elif Name == 809170886:
                    Name = "Prestige Eater of Worlds"
                EoW_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    EoW_Comp += 1
                    Raid_Tot_Comp += 1
                EoW_Tot_Time += Time
                EoW_Tot_K += Kills
                EoW_Tot_D += Deaths
            elif Name == 119944200:
                Name = "Spire of Stars"
                SoS_Start += 1
                Raid_Tot_Start += 1
                if Completion == 1:
                    SoS_Comp += 1
                    Raid_Tot_Comp += 1
                SoS_Tot_Time += Time
                SoS_Tot_K += Kills
                SoS_Tot_D += Deaths

            if Completion == 1:
                Completion = "Activity Complete"
                if Deaths == 0:
                    Completion = "Flawless"
                if Players == 1:
                    Completion = "Solo"
                    if Deaths == 0:
                        Completion = "Solo Flawless"
            else:
                Completion = "Activity Incompolete"

            Raids = (Name, Kills, Deaths, KD, KAD, Time, Players, Completion)
            Raid_Tot_Kills += Kills
            Raid_Tot_Deaths += Deaths
            Raid_Tot_Time += Time

        oneCharRaid = PrettyTable()
        oneCharRaid.field_names = ["Raid", "Starts", "Completions", "Kills", "Deaths", "Total Time"]
        oneCharRaid.add_row(["All Raids", Raid_Tot_Start, Raid_Tot_Comp, Raid_Tot_Kills, Raid_Tot_Deaths,
                             Time_Converter(Raid_Tot_Time)], divider=True)
        oneCharRaid.add_row(["Leviathan", Levi_Start, Levi_Comp, Levi_Tot_K, Levi_Tot_D, Time_Converter(Levi_Tot_Time)])
        oneCharRaid.add_row(["Eater of Worlds", EoW_Start, EoW_Comp, EoW_Tot_K, EoW_Tot_D,
                             Time_Converter(EoW_Tot_Time)])
        oneCharRaid.add_row(["Spire of Stars", SoS_Start, SoS_Comp, SoS_Tot_K, SoS_Tot_D, Time_Converter(SoS_Tot_Time)])
        oneCharRaid.add_row(["Crown of Sorrows", Crown_Start, Crown_Comp, Crown_Tot_K, Crown_Tot_D,
                             Time_Converter(Crown_Tot_Time)])
        oneCharRaid.add_row(["Scourge of the Past", SotP_Start, SotP_Comp, SotP_Tot_K, SotP_Tot_D,
                             Time_Converter(SotP_Tot_Time)],
                            divider=True)
        oneCharRaid.add_row(["Last Wish", LW_Start, LW_Comp, LW_Tot_K, LW_Tot_D, Time_Converter(LW_Tot_Time)])
        oneCharRaid.add_row(["Garden of Salvation", GoS_Start, GoS_Comp, GoS_Tot_K, GoS_Tot_D,
                             Time_Converter(GoS_Tot_Time)])
        oneCharRaid.add_row(["Deep Stone Crypt", DSC_Start, DSC_Comp, DSC_Tot_K, DSC_Tot_D,
                             Time_Converter(DSC_Tot_Time)])
        oneCharRaid.add_row(["Vault of Glass", VoG_Start, VoG_Comp, VoG_Tot_K, VoG_Tot_D, Time_Converter(VoG_Tot_Time)])
        oneCharRaid.add_row(["Vow of the Disciple", Vow_Start, Vow_Comp, Vow_Tot_K, Vow_Tot_D,
                             Time_Converter(Vow_Tot_Time)])
        oneCharRaid.add_row(["King's Fall", KF_Start, KF_Comp, KF_Tot_K, KF_Tot_D, Time_Converter(KF_Tot_Time)])
        oneCharRaid.add_row(["Root of Nightmares", Root_Start, Root_Comp, Root_Tot_K, Root_Tot_D,
                             Time_Converter(Root_Tot_Time)])
        print(oneCharRaid)

    elif MODE == 82:
        # All Dungeon Data
        # Totals for all Dungeons
        Dungeon_Tot_Start = 0
        Dungeon_Tot_Comp = 0
        Dungeon_Tot_Solo = 0
        Dungeon_Tot_Flawless = 0
        Dungeon_Tot_Solo_Flawless = 0
        Dungeon_Tot_Master_Comp = 0
        Dungeon_Tot_Kills = 0
        Dungeon_Tot_Deaths = 0
        Dungeon_Tot_Time = 0

        # Total for specific Dungeons
        Spire_Start = 0
        GotD_Start = 0
        ST_Start = 0
        Pit_Start = 0
        Proph_Start = 0
        Grasp_Start = 0
        Duality_Start = 0

        Spire_Comp = 0
        GotD_Comp = 0
        ST_Comp = 0
        Pit_Comp = 0
        Proph_Comp = 0
        Grasp_Comp = 0
        Duality_Comp = 0

        Spire_Tot_Time = 0
        GotD_Tot_Time = 0
        ST_Tot_Time = 0
        Pit_Tot_Time = 0
        Proph_Tot_Time = 0
        Grasp_Tot_Time = 0
        Duality_Tot_Time = 0

        Spire_Tot_K = 0
        GotD_Tot_K = 0
        ST_Tot_K = 0
        Pit_Tot_K = 0
        Proph_Tot_K = 0
        Grasp_Tot_K = 0
        Duality_Tot_K = 0

        Spire_Tot_D = 0
        GotD_Tot_D = 0
        ST_Tot_D = 0
        Pit_Tot_D = 0
        Proph_Tot_D = 0
        Grasp_Tot_D = 0
        Duality_Tot_D = 0

        ST_Tot_Solo = 0
        ST_Tot_Flawless = 0
        ST_Tot_Solo_Flawless = 0
        Pit_Tot_Solo = 0
        Pit_Tot_Flawless = 0
        Pit_Tot_Solo_Flawless = 0
        Proph_Tot_Solo = 0
        Proph_Tot_Flawless = 0
        Proph_Tot_Solo_Flawless = 0
        Grasp_Tot_Solo = 0
        Grasp_Tot_Flawless = 0
        Grasp_Tot_Solo_Flawless = 0
        Duality_Tot_Solo = 0
        Duality_Tot_Flawless = 0
        Duality_Tot_Solo_Flawless = 0
        Spire_Tot_Solo = 0
        Spire_Tot_Flawless = 0
        Spire_Tot_Solo_Flawless = 0
        GotD_Tot_Solo = 0
        GotD_Tot_Flawless = 0
        GotD_Tot_Solo_Flawless = 0

        with open('Char_1.json') as f:
            data1 = json.load(f)
        with open('Char_2.json') as f:
            data2 = json.load(f)
        with open('Char_4.json') as f:
            data4 = json.load(f)
        with open('Char_5.json') as f:
            data5 = json.load(f)
        with open('Char_6.json') as f:
            data6 = json.load(f)
        with open('Char_7.json') as f:
            data7 = json.load(f)
        with open('Char_8.json') as f:
            data8 = json.load(f)
        with open('Char_9.json') as f:
            data9 = json.load(f)
        with open('Char_10.json') as f:
            data10 = json.load(f)
        with open('Char_11.json') as f:
            data11 = json.load(f)
        with open('Char_12.json') as f:
            data12 = json.load(f)
        with open('Char_13.json') as f:
            data13 = json.load(f)
        with open('Char_14.json') as f:
            data14 = json.load(f)
        with open('Char_15.json') as f:
            data15 = json.load(f)
        with open('Char_16.json') as f:
            data16 = json.load(f)
        with open('Char_17.json') as f:
            data17 = json.load(f)
        with open('Char_19.json') as f:
            data19 = json.load(f)
        with open('Char_20.json') as f:
            data20 = json.load(f)
        with open('Char_21.json') as f:
            data21 = json.load(f)
        with open('Char_22.json') as f:
            data22 = json.load(f)
        with open('Char_24.json') as f:
            data24 = json.load(f)
        with open('Char_25.json') as f:
            data25 = json.load(f)
        with open('Char_26.json') as f:
            data26 = json.load(f)

        items1 = data1["Response"]
        items2 = data2["Response"]
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
        items19 = data19["Response"]
        items20 = data20["Response"]
        items21 = data21["Response"]
        items22 = data22["Response"]
        items24 = data24["Response"]
        items25 = data25["Response"]
        items26 = data26["Response"]

        char_json = {"Response": []}

        char_json['Response'].append(items1)
        char_json["Response"].append(items2)
        char_json['Response'].append(items4)
        char_json["Response"].append(items5)
        char_json["Response"].append(items6)
        char_json['Response'].append(items7)
        char_json["Response"].append(items8)
        char_json["Response"].append(items9)
        char_json['Response'].append(items10)
        char_json["Response"].append(items11)
        char_json["Response"].append(items12)
        char_json['Response'].append(items13)
        char_json["Response"].append(items14)
        char_json["Response"].append(items15)
        char_json['Response'].append(items16)
        char_json["Response"].append(items17)
        char_json['Response'].append(items19)
        char_json["Response"].append(items20)
        char_json["Response"].append(items21)
        char_json['Response'].append(items22)
        char_json["Response"].append(items24)
        char_json['Response'].append(items25)
        char_json["Response"].append(items26)

        with open('char.json', "w") as f:
            f.write(json.dumps(char_json, indent=2))

        activities_len_1 = len(char_json["Response"][0]['activities'])
        activities_len_2 = len(char_json["Response"][1]['activities'])
        activities_len_4 = len(char_json["Response"][2]['activities'])
        activities_len_5 = len(char_json["Response"][3]['activities'])
        activities_len_6 = len(char_json["Response"][4]['activities'])
        activities_len_7 = len(char_json["Response"][5]['activities'])
        activities_len_8 = len(char_json["Response"][6]['activities'])
        activities_len_9 = len(char_json["Response"][7]['activities'])
        activities_len_10 = len(char_json["Response"][8]['activities'])
        activities_len_11 = len(char_json["Response"][9]['activities'])
        activities_len_12 = len(char_json["Response"][10]['activities'])
        activities_len_13 = len(char_json["Response"][11]['activities'])
        activities_len_14 = len(char_json["Response"][12]['activities'])
        activities_len_15 = len(char_json["Response"][13]['activities'])
        activities_len_16 = len(char_json["Response"][14]['activities'])
        activities_len_17 = len(char_json["Response"][15]['activities'])
        activities_len_19 = len(char_json["Response"][16]['activities'])
        activities_len_20 = len(char_json["Response"][17]['activities'])
        activities_len_21 = len(char_json["Response"][18]['activities'])
        activities_len_22 = len(char_json["Response"][19]['activities'])
        activities_len_24 = len(char_json["Response"][20]['activities'])
        activities_len_25 = len(char_json["Response"][21]['activities'])
        activities_len_26 = len(char_json["Response"][22]['activities'])

        Dungeon_Name = {"Dungeon": []}
        Dungeon_Kills = {"Kills": []}
        Dungeon_Deaths = {"Deaths": []}
        Dungeon_KD = {"K/D": []}
        Dungeon_KAD = {"KA/D": []}
        Dungeon_Time = {"Time": []}
        Dungeon_PlayerCount = {"Player Count": []}
        Dungeon_Complete = {"Completion": []}

        for number in range(0, activities_len_1):
            Dungeon_Name_1 = char_json["Response"][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_1 = char_json["Response"][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_1 = char_json["Response"][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_1 = \
                char_json["Response"][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_1 = \
                char_json["Response"][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_1 = \
                char_json["Response"][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_1 = \
                char_json["Response"][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_1 = char_json["Response"][0]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_1)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_1)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_1)
            Dungeon_KD['K/D'].append(Dungeon_KD_1)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_1)
            Dungeon_Time['Time'].append(Dungeon_Time_1)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_1)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_1)
        for number in range(0, activities_len_2):
            Dungeon_Name_2 = char_json["Response"][1]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_2 = char_json["Response"][1]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_2 = char_json["Response"][1]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_2 = \
                char_json["Response"][1]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_2 = \
                char_json["Response"][1]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_2 = \
                char_json["Response"][1]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_2 = \
                char_json["Response"][1]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_2 = char_json["Response"][1]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_2)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_2)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_2)
            Dungeon_KD['K/D'].append(Dungeon_KD_2)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_2)
            Dungeon_Time['Time'].append(Dungeon_Time_2)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_2)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_2)
        for number in range(0, activities_len_4):
            Dungeon_Name_4 = char_json["Response"][2]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_4 = char_json["Response"][2]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_4 = char_json["Response"][2]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_4 = \
                char_json["Response"][2]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_4 = \
                char_json["Response"][2]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_4 = \
                char_json["Response"][2]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_4 = \
                char_json["Response"][2]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_4 = char_json["Response"][2]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_4)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_4)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_4)
            Dungeon_KD['K/D'].append(Dungeon_KD_4)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_4)
            Dungeon_Time['Time'].append(Dungeon_Time_4)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_4)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_4)
        for number in range(0, activities_len_5):
            Dungeon_Name_5 = char_json["Response"][3]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_5 = char_json["Response"][3]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_5 = char_json["Response"][3]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_5 = \
                char_json["Response"][3]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_5 = \
                char_json["Response"][3]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_5 = \
                char_json["Response"][3]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_5 = \
                char_json["Response"][3]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_5 = char_json["Response"][3]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_5)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_5)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_5)
            Dungeon_KD['K/D'].append(Dungeon_KD_5)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_5)
            Dungeon_Time['Time'].append(Dungeon_Time_5)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_5)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_5)
        for number in range(0, activities_len_6):
            Dungeon_Name_6 = char_json["Response"][4]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_6 = char_json["Response"][4]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_6 = char_json["Response"][4]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_6 = \
                char_json["Response"][4]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_6 = \
                char_json["Response"][4]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_6 = \
                char_json["Response"][4]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_6 = \
                char_json["Response"][4]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_6 = char_json["Response"][4]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_6)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_6)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_6)
            Dungeon_KD['K/D'].append(Dungeon_KD_6)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_6)
            Dungeon_Time['Time'].append(Dungeon_Time_6)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_6)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_6)
        for number in range(0, activities_len_7):
            Dungeon_Name_7 = char_json["Response"][5]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_7 = char_json["Response"][5]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_7 = char_json["Response"][5]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_7 = \
                char_json["Response"][5]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_7 = \
                char_json["Response"][5]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_7 = \
                char_json["Response"][5]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_7 = \
                char_json["Response"][5]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_7 = char_json["Response"][5]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_7)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_7)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_7)
            Dungeon_KD['K/D'].append(Dungeon_KD_7)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_7)
            Dungeon_Time['Time'].append(Dungeon_Time_7)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_7)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_7)
        for number in range(0, activities_len_8):
            Dungeon_Name_8 = char_json["Response"][6]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_8 = char_json["Response"][6]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_8 = char_json["Response"][6]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_8 = \
                char_json["Response"][6]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_8 = \
                char_json["Response"][6]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_8 = \
                char_json["Response"][6]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_8 = \
                char_json["Response"][6]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_8 = char_json["Response"][6]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_8)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_8)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_8)
            Dungeon_KD['K/D'].append(Dungeon_KD_8)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_8)
            Dungeon_Time['Time'].append(Dungeon_Time_8)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_8)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_8)
        for number in range(0, activities_len_9):
            Dungeon_Name_9 = char_json["Response"][7]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_9 = char_json["Response"][7]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_9 = char_json["Response"][7]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_9 = \
                char_json["Response"][7]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_9 = \
                char_json["Response"][7]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_9 = \
                char_json["Response"][7]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_9 = \
                char_json["Response"][7]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_9 = char_json["Response"][7]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_9)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_9)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_9)
            Dungeon_KD['K/D'].append(Dungeon_KD_9)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_9)
            Dungeon_Time['Time'].append(Dungeon_Time_9)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_9)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_9)
        for number in range(0, activities_len_10):
            Dungeon_Name_10 = char_json["Response"][8]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_10 = char_json["Response"][8]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_10 = char_json["Response"][8]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_10 = \
                char_json["Response"][8]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_10 = \
                char_json["Response"][8]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_10 = \
                char_json["Response"][8]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_10 = \
                char_json["Response"][8]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_10 = char_json["Response"][8]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_10)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_10)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_10)
            Dungeon_KD['K/D'].append(Dungeon_KD_10)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_10)
            Dungeon_Time['Time'].append(Dungeon_Time_10)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_10)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_10)
        for number in range(0, activities_len_11):
            Dungeon_Name_11 = char_json["Response"][9]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_11 = char_json["Response"][9]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_11 = char_json["Response"][9]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_11 = \
                char_json["Response"][9]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_11 = \
                char_json["Response"][9]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_11 = \
                char_json["Response"][9]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_11 = \
                char_json["Response"][9]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_11 = char_json["Response"][9]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_11)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_11)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_11)
            Dungeon_KD['K/D'].append(Dungeon_KD_11)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_11)
            Dungeon_Time['Time'].append(Dungeon_Time_11)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_11)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_11)
        for number in range(0, activities_len_12):
            Dungeon_Name_12 = char_json["Response"][10]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_12 = char_json["Response"][10]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_12 = char_json["Response"][10]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_12 = \
                char_json["Response"][10]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_12 = \
                char_json["Response"][10]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_12 = \
                char_json["Response"][10]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_12 = \
                char_json["Response"][10]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_12 = char_json["Response"][10]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_12)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_12)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_12)
            Dungeon_KD['K/D'].append(Dungeon_KD_12)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_12)
            Dungeon_Time['Time'].append(Dungeon_Time_12)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_12)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_12)
        for number in range(0, activities_len_13):
            Dungeon_Name_13 = char_json["Response"][11]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_13 = char_json["Response"][11]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_13 = char_json["Response"][11]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_13 = \
                char_json["Response"][11]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_13 = \
                char_json["Response"][11]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_13 = \
                char_json["Response"][11]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_13 = \
                char_json["Response"][11]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_13 = char_json["Response"][11]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_13)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_13)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_13)
            Dungeon_KD['K/D'].append(Dungeon_KD_13)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_13)
            Dungeon_Time['Time'].append(Dungeon_Time_13)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_13)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_13)
        for number in range(0, activities_len_14):
            Dungeon_Name_14 = char_json["Response"][12]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_14 = char_json["Response"][12]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_14 = char_json["Response"][12]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_14 = \
                char_json["Response"][12]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_14 = \
                char_json["Response"][12]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_14 = \
                char_json["Response"][12]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_14 = \
                char_json["Response"][12]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_14 = char_json["Response"][12]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_14)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_14)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_14)
            Dungeon_KD['K/D'].append(Dungeon_KD_14)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_14)
            Dungeon_Time['Time'].append(Dungeon_Time_14)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_14)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_14)
        for number in range(0, activities_len_15):
            Dungeon_Name_15 = char_json["Response"][13]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_15 = char_json["Response"][13]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_15 = char_json["Response"][13]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_15 = \
                char_json["Response"][13]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_15 = \
                char_json["Response"][13]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_15 = \
                char_json["Response"][13]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_15 = \
                char_json["Response"][13]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_15 = char_json["Response"][13]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_15)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_15)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_15)
            Dungeon_KD['K/D'].append(Dungeon_KD_15)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_15)
            Dungeon_Time['Time'].append(Dungeon_Time_15)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_15)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_15)
        for number in range(0, activities_len_16):
            Dungeon_Name_16 = char_json["Response"][14]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_16 = char_json["Response"][14]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_16 = char_json["Response"][14]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_16 = \
                char_json["Response"][14]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_16 = \
                char_json["Response"][14]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_16 = \
                char_json["Response"][14]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_16 = \
                char_json["Response"][14]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_16 = char_json["Response"][14]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_16)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_16)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_16)
            Dungeon_KD['K/D'].append(Dungeon_KD_16)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_16)
            Dungeon_Time['Time'].append(Dungeon_Time_16)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_16)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_16)
        for number in range(0, activities_len_17):
            Dungeon_Name_17 = char_json["Response"][15]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_17 = char_json["Response"][15]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_17 = char_json["Response"][15]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_17 = \
                char_json["Response"][15]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_17 = \
                char_json["Response"][15]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_17 = \
                char_json["Response"][15]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_17 = \
                char_json["Response"][15]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_17 = char_json["Response"][15]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_17)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_17)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_17)
            Dungeon_KD['K/D'].append(Dungeon_KD_17)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_17)
            Dungeon_Time['Time'].append(Dungeon_Time_17)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_17)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_17)
        for number in range(0, activities_len_19):
            Dungeon_Name_19 = char_json["Response"][16]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_19 = char_json["Response"][16]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_19 = char_json["Response"][16]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_19 = \
                char_json["Response"][16]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_19 = \
                char_json["Response"][16]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_19 = \
                char_json["Response"][16]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_19 = \
                char_json["Response"][16]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_19 = char_json["Response"][16]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_19)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_19)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_19)
            Dungeon_KD['K/D'].append(Dungeon_KD_19)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_19)
            Dungeon_Time['Time'].append(Dungeon_Time_19)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_19)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_19)
        for number in range(0, activities_len_20):
            Dungeon_Name_20 = char_json["Response"][17]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_20 = char_json["Response"][17]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_20 = char_json["Response"][17]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_20 = \
                char_json["Response"][17]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_20 = \
                char_json["Response"][17]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_20 = \
                char_json["Response"][17]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_20 = \
                char_json["Response"][17]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_20 = char_json["Response"][17]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_20)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_20)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_20)
            Dungeon_KD['K/D'].append(Dungeon_KD_20)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_20)
            Dungeon_Time['Time'].append(Dungeon_Time_20)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_20)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_20)
        for number in range(0, activities_len_21):
            Dungeon_Name_21 = char_json["Response"][18]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_21 = char_json["Response"][18]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_21 = char_json["Response"][18]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_21 = \
                char_json["Response"][18]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_21 = \
                char_json["Response"][18]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_21 = \
                char_json["Response"][18]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_21 = \
                char_json["Response"][18]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_21 = char_json["Response"][18]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_21)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_21)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_21)
            Dungeon_KD['K/D'].append(Dungeon_KD_21)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_21)
            Dungeon_Time['Time'].append(Dungeon_Time_21)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_21)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_21)
        for number in range(0, activities_len_22):
            Dungeon_Name_22 = char_json["Response"][19]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_22 = char_json["Response"][19]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_22 = char_json["Response"][19]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_22 = \
                char_json["Response"][19]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_22 = \
                char_json["Response"][19]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_22 = \
                char_json["Response"][19]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_22 = \
                char_json["Response"][19]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_22 = char_json["Response"][19]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_22)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_22)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_22)
            Dungeon_KD['K/D'].append(Dungeon_KD_22)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_22)
            Dungeon_Time['Time'].append(Dungeon_Time_22)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_22)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_22)
        for number in range(0, activities_len_24):
            Dungeon_Name_24 = char_json["Response"][20]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_24 = char_json["Response"][20]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_24 = char_json["Response"][20]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_24 = \
                char_json["Response"][20]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_24 = \
                char_json["Response"][20]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_24 = \
                char_json["Response"][20]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_24 = \
                char_json["Response"][20]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_24 = char_json["Response"][20]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_24)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_24)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_24)
            Dungeon_KD['K/D'].append(Dungeon_KD_24)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_24)
            Dungeon_Time['Time'].append(Dungeon_Time_24)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_24)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_24)
        for number in range(0, activities_len_25):
            Dungeon_Name_25 = char_json["Response"][21]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_25 = char_json["Response"][21]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_25 = char_json["Response"][21]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_25 = \
                char_json["Response"][21]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_25 = \
                char_json["Response"][21]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_25 = \
                char_json["Response"][21]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_25 = \
                char_json["Response"][21]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_25 = char_json["Response"][21]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_25)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_25)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_25)
            Dungeon_KD['K/D'].append(Dungeon_KD_25)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_25)
            Dungeon_Time['Time'].append(Dungeon_Time_25)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_25)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_25)
        for number in range(0, activities_len_26):
            Dungeon_Name_26 = char_json["Response"][22]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_26 = char_json["Response"][22]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_26 = char_json["Response"][22]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_26 = \
                char_json["Response"][22]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_26 = \
                char_json["Response"][22]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_26 = \
                char_json["Response"][22]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_26 = \
                char_json["Response"][22]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_26 = char_json["Response"][22]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_26)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_26)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_26)
            Dungeon_KD['K/D'].append(Dungeon_KD_26)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_26)
            Dungeon_Time['Time'].append(Dungeon_Time_26)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_26)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_26)

        Dungeon_Info = [Dungeon_Name, Dungeon_Kills, Dungeon_Deaths, Dungeon_KD, Dungeon_KAD, Dungeon_Time,
                        Dungeon_PlayerCount, Dungeon_Complete]

        length = len(Dungeon_Info[0]['Dungeon'])

        for numb in range(0, length):
            Name = Dungeon_Info[0]['Dungeon'][numb]
            Kills = Dungeon_Info[1]['Kills'][numb]
            Deaths = Dungeon_Info[2]['Deaths'][numb]
            KD = Dungeon_Info[3]['K/D'][numb]
            KAD = Dungeon_Info[4]['KA/D'][numb]
            Time = Dungeon_Info[5]['Time'][numb]
            Players = Dungeon_Info[6]['Player Count'][numb]
            Completion = Dungeon_Info[7]['Completion'][numb]

            if Name == 1262462921 or Name == 1801496203:
                Name = "Spire of the Watcher"
                Spire_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    Spire_Comp += 1
                    Dungeon_Tot_Comp += 1
                Spire_Tot_Time += Time
                Spire_Tot_K += Kills
                Spire_Tot_D += Deaths
            elif Name == 2823159265 or Name == 1668217731:
                Name = "Duality"
                Duality_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    Duality_Comp += 1
                    Dungeon_Tot_Comp += 1
                Duality_Tot_Time += Time
                Duality_Tot_K += Kills
                Duality_Tot_D += Deaths
            elif Name == 4078656646 or Name == 3774021532:
                Name = "Grasp of Avarice"
                Grasp_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    Grasp_Comp += 1
                    Dungeon_Tot_Comp += 1
                Grasp_Tot_Time += Time
                Grasp_Tot_K += Kills
                Grasp_Tot_D += Deaths
            elif Name == 313828469 or Name == 2716998124:
                Name = "Ghosts of the Deep"
                GotD_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    GotD_Comp += 1
                    Dungeon_Tot_Comp += 1
                GotD_Tot_Time += Time
                GotD_Tot_K += Kills
                GotD_Tot_D += Deaths
            elif Name == 2032534090:
                Name = "The Shattered Throne"
                ST_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    ST_Comp += 1
                    Dungeon_Tot_Comp += 1
                ST_Tot_Time += Time
                ST_Tot_K += Kills
                ST_Tot_D += Deaths
            elif Name == 2582501063 or Name == 1375089621:
                Name = "Pit of Heresy"
                Pit_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    Pit_Comp += 1
                    Dungeon_Tot_Comp += 1
                Pit_Tot_Time += Time
                Pit_Tot_K += Kills
                Pit_Tot_D += Deaths
            elif Name == 4148187374 or Name == 1077850348:
                Name = "Prophecy"
                Proph_Start += 1
                Dungeon_Tot_Start += 1
                if Completion == 1:
                    Proph_Comp += 1
                    Dungeon_Tot_Comp += 1
                Proph_Tot_Time += Time
                Proph_Tot_K += Kills
                Proph_Tot_D += Deaths

            if Completion == 1:
                Completion = "Activity Complete"
                if Deaths == 0:
                    Completion = "Flawless"
                    Dungeon_Tot_Flawless += 1
                    if Name == "Shattered Throne":
                        ST_Tot_Flawless += 1
                    if Name == "Pit of Heresy":
                        Pit_Tot_Flawless += 1
                    if Name == "Prophecy":
                        Proph_Tot_Flawless += 1
                    if Name == "Grasp of Avarice":
                        Grasp_Tot_Flawless += 1
                    if Name == "Duality":
                        Duality_Tot_Flawless += 1
                    if Name == "Spire of the Watcher":
                        Spire_Tot_Flawless += 1
                    if Name == "Ghosts of the Deep":
                        GotD_Tot_Flawless += 1
                if Players == 1:
                    Completion = "Solo"
                    Dungeon_Tot_Solo += 1
                    if Name == "Shattered Throne":
                        ST_Tot_Solo += 1
                    if Name == "Pit of Heresy":
                        Pit_Tot_Solo += 1
                    if Name == "Prophecy":
                        Proph_Tot_Solo += 1
                    if Name == "Grasp of Avarice":
                        Grasp_Tot_Solo += 1
                    if Name == "Duality":
                        Duality_Tot_Solo += 1
                    if Name == "Spire of the Watcher":
                        Spire_Tot_Solo += 1
                    if Name == "Ghosts of the Deep":
                        GotD_Tot_Solo += 1
                    if Deaths == 0:
                        Completion = "Solo Flawless"
                        Dungeon_Tot_Solo_Flawless += 1
                        if Name == "Shattered Throne":
                            ST_Tot_Solo_Flawless += 1
                        if Name == "Pit of Heresy":
                            Pit_Tot_Solo_Flawless += 1
                        if Name == "Prophecy":
                            Proph_Tot_Solo_Flawless += 1
                        if Name == "Grasp of Avarice":
                            Grasp_Tot_Solo_Flawless += 1
                        if Name == "Duality":
                            Duality_Tot_Solo_Flawless += 1
                        if Name == "Spire of the Watcher":
                            Spire_Tot_Solo_Flawless += 1
                        if Name == "Ghosts of the Deep":
                            GotD_Tot_Solo_Flawless += 1
            else:
                Completion = "Activity Incompolete"

            Dungeon_Tot_Kills += Kills
            Dungeon_Tot_Deaths += Deaths
            Dungeon_Tot_Time += Time

        oneCharDung = PrettyTable()
        oneCharDung.field_names = ["Dungeon", "Starts", "Completions", "Kills", "Deaths", "Total Time"]
        oneCharDung.add_row(["All Dungeons", Dungeon_Tot_Start, Dungeon_Tot_Comp, round(Dungeon_Tot_Kills),
                             round(Dungeon_Tot_Deaths), Time_Converter(Dungeon_Tot_Time)], divider=True)
        oneCharDung.add_row(["Shattered Throne", ST_Start, ST_Comp, round(ST_Tot_K), round(ST_Tot_D),
                             Time_Converter(ST_Tot_Time)])
        oneCharDung.add_row(["Pit of Heresy", Pit_Start, Pit_Comp, round(Pit_Tot_K), round(Pit_Tot_D),
                             Time_Converter(Pit_Tot_Time)])
        oneCharDung.add_row(["Prophecy", Proph_Start, Proph_Comp, round(Proph_Tot_K), round(Proph_Tot_D),
                             Time_Converter(Proph_Tot_Time)])
        oneCharDung.add_row(["Grasp of Avarice", Grasp_Start, Grasp_Comp, round(Grasp_Tot_K), round(Grasp_Tot_D),
                             Time_Converter(Grasp_Tot_Time)])
        oneCharDung.add_row(["Duality", Duality_Start, Duality_Comp, round(Duality_Tot_K), round(Duality_Tot_D),
                             Time_Converter(Duality_Tot_Time)])
        oneCharDung.add_row(["Spire of the Watcher", Spire_Start, Spire_Comp, round(Spire_Tot_K), round(Spire_Tot_D),
                             Time_Converter(Spire_Tot_Time)])
        oneCharDung.add_row(["Ghosts of the Deep", GotD_Start, GotD_Comp, round(GotD_Tot_K), round(GotD_Tot_D),
                             Time_Converter(GotD_Tot_Time)])
        print(oneCharDung)

        SoloTable = PrettyTable()
        SoloTable.field_names = ["Dungeon", "Solo", "Flawless", "Solo Flawless"]
        SoloTable.add_row(["All Dungeons", Dungeon_Tot_Solo, Dungeon_Tot_Flawless, Dungeon_Tot_Solo_Flawless],
                          divider=True)
        SoloTable.add_row(["Shattered Throne", ST_Tot_Solo, ST_Tot_Flawless, ST_Tot_Solo_Flawless])
        SoloTable.add_row(["Pit of Heresy", Pit_Tot_Solo, Pit_Tot_Flawless, Pit_Tot_Solo_Flawless])
        SoloTable.add_row(["Prophecy", Proph_Tot_Solo, Proph_Tot_Flawless, Proph_Tot_Solo_Flawless])
        SoloTable.add_row(["Grasp of Avarice", Grasp_Tot_Solo, Grasp_Tot_Flawless, Grasp_Tot_Solo_Flawless])
        SoloTable.add_row(["Duality", Duality_Tot_Solo, Duality_Tot_Flawless, Duality_Tot_Solo_Flawless])
        SoloTable.add_row(["Spire of the Watcher", Spire_Tot_Solo, Spire_Tot_Flawless, Spire_Tot_Solo_Flawless])
        SoloTable.add_row(["Ghosts of the Deep", GotD_Tot_Solo, GotD_Tot_Flawless, GotD_Tot_Solo_Flawless])
        print(SoloTable)
