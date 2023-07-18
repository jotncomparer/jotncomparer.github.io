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

# membershipType: Designates what machine the player uses. This number comes from the first device the account is set
# on. 1 - Xbox, 2- Playstation, 3 - Steam
# destinyMembershipId: The actual user account
# characterId: The specific character (Titan/Warlock/Hunter) that is used by the membership account
# Man in the Moon - Connor
membershipType = 1
destinyMembershipId = 4611686018450697084
characterId = 2305843009644414176

# The Chrome Leaf - Thomas
# membershipType = 1
# destinyMembershipId = 4611686018444441571
# Warlock:
# characterId = 2305843009265786295
# Titan:
# characterId = 2305843009283965144
# Hunter:
# characterId = 2305843009569534739

# MODE Numbers: 4 = Raids, 82 = Dungeons
# COUNT Limit: 250 per PAGE
# PAGE LIMIT: unknown

MODE = 82
COUNT = 250
PAGE = 0

if MODE == 82 and destinyMembershipId == 4611686018450697084:

    # All Dungeon Data
    # Totals for all Dungeons
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

    # If the first page is longer than the page limit, create five .json files to and combine them to collect all the data
    # Then proceeds to combine all .json files into one "mega"-file.

    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={PAGE}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    pretty_Dungeon_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Dungeon_data_1.json', 'w')
    writeFile.write(pretty_Dungeon_data)
    writeFile.close

    url2 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={1}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response2 = requests.request("GET", url2, headers=headers, data=payload)
    response2.content.decode('utf-8')
    pretty_Dungeon_data2 = json.dumps(json.loads(response2.content), indent=2)
    writeFile = open('Dungeon_data_2.json', 'w')
    writeFile.write(pretty_Dungeon_data2)
    writeFile.close

    url3 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={2}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response3 = requests.request("GET", url3, headers=headers, data=payload)
    response3.content.decode('utf-8')
    pretty_Dungeon_data3 = json.dumps(json.loads(response3.content), indent=2)
    writeFile = open('Dungeon_data_3.json', 'w')
    writeFile.write(pretty_Dungeon_data3)
    writeFile.close

    with open('Dungeon_data_1.json.') as f:
        data1 = json.load(f)
    with open('Dungeon_data_2.json') as f:
        data2 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]

    Dungeon_data_json = {"Response": []}

    Dungeon_data_json['Response'].append(items1)
    Dungeon_data_json["Response"].append(items2)

    with open('Dungeon_data.json', "w") as f:
        f.write(json.dumps(Dungeon_data_json, indent=2))

    activities_len_1 = len(Dungeon_data_json["Response"][0]['activities'])
    activities_len_2 = len(Dungeon_data_json["Response"][1]['activities'])

    if activities_len_1 and activities_len_2 > 0:
        Dungeon_Name = {"Dungeon": []}
        Dungeon_Kills = {"Kills": []}
        Dungeon_Deaths = {"Deaths": []}
        Dungeon_KD = {"K/D": []}
        Dungeon_KAD = {"KA/D": []}
        Dungeon_Time = {"Time": []}
        Dungeon_PlayerCount = {"Player Count": []}
        Dungeon_Complete = {"Completion": []}
        for number in range(0, activities_len_1):
            Dungeon_Name_1 = Dungeon_data_json["Response"][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_1 = Dungeon_data_json["Response"][0]["activities"][number]["values"]["kills"]["basic"]["value"]
            Dungeon_Deaths_1 = Dungeon_data_json["Response"][0]["activities"][number]["values"]["deaths"]["basic"]["value"]
            Dungeon_KD_1 = Dungeon_data_json["Response"][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                "value"]
            Dungeon_KAD_1 = Dungeon_data_json["Response"][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                "value"]
            Dungeon_Time_1 = \
            Dungeon_data_json["Response"][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"]["value"]
            Dungeon_PlayerCount_1 = \
            Dungeon_data_json["Response"][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_1 = Dungeon_data_json["Response"][0]["activities"][number]["values"]["completed"]["basic"][
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
            Dungeon_Name_2 = Dungeon_data_json["Response"][1]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_2 = Dungeon_data_json["Response"][1]["activities"][number]["values"]["kills"]["basic"]["value"]
            Dungeon_Deaths_2 = Dungeon_data_json["Response"][1]["activities"][number]["values"]["deaths"]["basic"]["value"]
            Dungeon_KD_2 = Dungeon_data_json["Response"][1]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                "value"]
            Dungeon_KAD_2 = Dungeon_data_json["Response"][1]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                "value"]
            Dungeon_Time_2 = \
            Dungeon_data_json["Response"][1]["activities"][number]["values"]["activityDurationSeconds"]["basic"]["value"]
            Dungeon_PlayerCount_2 = \
            Dungeon_data_json["Response"][1]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_2 = Dungeon_data_json["Response"][1]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_2)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_2)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_2)
            Dungeon_KD['K/D'].append(Dungeon_KD_2)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_2)
            Dungeon_Time['Time'].append(Dungeon_Time_2)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_2)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_2)
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
            Spire_Tot_Time += Time
            Spire_Tot_K += Kills
            Spire_Tot_D += Deaths
        elif Name == 2823159265 or Name == 1668217731:
            Name = "Duality"
            Duality_Tot_Time += Time
            Duality_Tot_K += Kills
            Duality_Tot_D += Deaths
        elif Name == 4078656646 or Name == 3774021532:
            Name = "Grasp of Avarice"
            Grasp_Tot_Time += Time
            Grasp_Tot_K += Kills
            Grasp_Tot_D += Deaths
        elif Name == 313828469 or Name == 2716998124:
            Name = "Ghosts of the Deep"
            GotD_Tot_Time += Time
            GotD_Tot_K += Kills
            GotD_Tot_D += Deaths
        elif Name == 2032534090:
            Name = "The Shattered Throne"
            ST_Tot_Time += Time
            ST_Tot_K += Kills
            ST_Tot_D += Deaths
        elif Name == 2582501063 or Name == 1375089621:
            Name = "Pit of Heresy"
            Pit_Tot_Time += Time
            Pit_Tot_K += Kills
            Pit_Tot_D += Deaths
        elif Name == 4148187374 or Name == 1077850348:
            Name = "Prophecy"
            Proph_Tot_Time += Time
            Proph_Tot_K += Kills
            Proph_Tot_D += Deaths

        if Completion == 1:
            Completion = "Activity Complete"
            if Deaths == 0:
                Completion = "Flawless"
            if Players == 1:
                Completion = "Solo"
                if Deaths == 0:
                    Completion = "Solo FLawless"
        else:
            Completion = "Activity Incompolete"


        Dungeon_Tot_Kills += Kills
        Dungeon_Tot_Deaths += Deaths
        Dungeon_Tot_Time += Time

        Dungeons = (Name, Kills, Deaths, KD, KAD, Time, Players, Completion)

        print(Dungeons)

    Seconds = Dungeon_Tot_Time % 60
    Minutes = Dungeon_Tot_Time / 60
    Minutes = math.trunc(Minutes)
    Hours = Minutes / 60
    Hours = math.trunc(Hours)
    Minutes = Minutes % 60
    Days = Hours / 24
    Days = math.trunc(Days)
    Hours = Hours % 24
    Weeks = Days / 7
    Weeks = math.trunc(Weeks)
    Days = Days % 7

    Dungeon_Tot_Time = (f'{Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}')

    print(Dungeon_Tot_Time, Dungeon_Tot_Kills, Dungeon_Tot_Deaths)

elif MODE == 4 and destinyMembershipId == 4611686018450697084:

    # All Raid Data
    # Totals for all Raids
    Raid_Tot_Kills = 0
    Raid_Tot_Deaths = 0
    Raid_Tot_Time = 0

    # Total for specific raids
    Levi_Start = 0
    SotP_Start = 0
    LW_Start = 0
    GoS_Start = 0
    DSC_Start = 0
    VoG_Start = 0
    Vow_Start = 0
    KF_Start = 0
    Root_Start = 0

    Levi_Tot_Time = 0
    SotP_Tot_Time = 0
    LW_Tot_Time = 0
    GoS_Tot_Time = 0
    DSC_Tot_Time = 0
    VoG_Tot_Time = 0
    Vow_Tot_Time = 0
    KF_Tot_Time = 0
    Root_Tot_Time = 0

    Levi_Tot_K = 0
    SotP_Tot_K = 0
    LW_Tot_K = 0
    GoS_Tot_K = 0
    DSC_Tot_K = 0
    VoG_Tot_K = 0
    Vow_Tot_K = 0
    KF_Tot_K = 0
    Root_Tot_K = 0

    Levi_Tot_D = 0
    SotP_Tot_D = 0
    LW_Tot_D = 0
    GoS_Tot_D = 0
    DSC_Tot_D = 0
    VoG_Tot_D = 0
    Vow_Tot_D = 0
    KF_Tot_D = 0
    Root_Tot_D = 0

    url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
          f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={PAGE}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    pretty_Raid_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Raid_data_1.json', 'w')
    writeFile.write(pretty_Raid_data)
    writeFile.close

    url2 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={1}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response2 = requests.request("GET", url2, headers=headers, data=payload)
    response2.content.decode('utf-8')
    pretty_Raid_data2 = json.dumps(json.loads(response2.content), indent=2)
    writeFile = open('Raid_data_2.json', 'w')
    writeFile.write(pretty_Raid_data2)
    writeFile.close

    url3 = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/" \
           f"{characterId}/Stats/Activities/?mode={MODE}&count={COUNT}&page={2}"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response3 = requests.request("GET", url3, headers=headers, data=payload)
    response3.content.decode('utf-8')
    pretty_Raid_data3 = json.dumps(json.loads(response3.content), indent=2)
    writeFile = open('Raid_data_3.json', 'w')
    writeFile.write(pretty_Raid_data3)
    writeFile.close

    with open('Raid_data_1.json.') as f:
        data1 = json.load(f)
    with open('Raid_data_2.json') as f:
        data2 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]

    Raid_data_json = {"Response": []}

    Raid_data_json['Response'].append(items1)
    Raid_data_json["Response"].append(items2)

    with open('Raid_data.json', "w") as f:
        f.write(json.dumps(Raid_data_json, indent=2))

    activities_len_1 = len(Raid_data_json["Response"][0]['activities'])

    if activities_len_1 > 0:
        Raid_Name = {"Raid": []}
        Raid_Kills = {"Kills": []}
        Raid_Deaths = {"Deaths": []}
        Raid_KD = {"K/D": []}
        Raid_KAD = {"KA/D": []}
        Raid_Time = {"Time": []}
        Raid_PlayerCount = {"Player Count": []}
        Raid_Complete = {"Completion": []}
        for number in range(0, activities_len_1):
            Raid_Name_1 = Raid_data_json["Response"][0]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_1 = Raid_data_json["Response"][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_1 = Raid_data_json["Response"][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_1 = \
            Raid_data_json["Response"][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                "value"]
            Raid_KAD_1 = \
            Raid_data_json["Response"][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                "value"]
            Raid_Time_1 = \
                Raid_data_json["Response"][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_1 = \
                Raid_data_json["Response"][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_1 = Raid_data_json["Response"][0]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_1)
            Raid_Kills['Kills'].append(Raid_Kills_1)
            Raid_Deaths['Deaths'].append(Raid_Deaths_1)
            Raid_KD['K/D'].append(Raid_KD_1)
            Raid_KAD['KA/D'].append(Raid_KAD_1)
            Raid_Time['Time'].append(Raid_Time_1)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_1)
            Raid_Complete['Completion'].append(Raid_Complete_1)

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
            LW_Tot_Time += Time
            LW_Tot_K += Kills
            LW_Tot_D += Deaths
        elif Name == 3458480158 or Name == 2659723068:
            Name = "Garden of Salvation"
            GoS_Tot_Time += Time
            GoS_Tot_K += Kills
            GoS_Tot_D += Deaths
        elif Name == 910380154:
            Name = "Deep Stone Crypt"
            DSC_Tot_Time += Time
            DSC_Tot_K += Kills
            DSC_Tot_D += Deaths
        elif Name == 3881495763:
            Name = "Vault of Glass"
            VoG_Tot_Time += Time
            VoG_Tot_K += Kills
            VoG_Tot_D += Deaths
        elif Name == 1441982566:
            Name = "Vow of the Disciple"
            Vow_Tot_Time += Time
            Vow_Tot_K += Kills
            Vow_Tot_D += Deaths
        elif Name == 1374392663 or Name == 2964135793:
            if Name == 1374392663:
                Name = "King's Fall"
            elif Name == 2964135793:
                Name = "King's Fall: Master"
            KF_Tot_Time += Time
            KF_Tot_K += Kills
            KF_Tot_D += Deaths
        elif Name == 2381413764:
            Name = "Root of Nightmares"
            Root_Tot_Time += Time
            Root_Tot_K += Kills
            Root_Tot_D += Deaths
        elif Name == 2693136601:
            Name = "Leviathan"
            Levi_Tot_Time += Time
            Levi_Tot_K += Kills
            Levi_Tot_D += Deaths
        elif Name == 548750096:
            Name = "Scourge of the Past"
            SotP_Tot_Time += Time
            SotP_Tot_K += Kills
            SotP_Tot_D += Deaths

        if Completion == 0:
            Completion = "Activity Incomplete"
        else:
            Completion = "Activity Complete"

        if Deaths == 0 and Completion == 1:
            Deaths = "Flawless"

        Raids = (Name, Kills, Deaths, KD, KAD, Time, Players, Completion)
        Raid_Tot_Kills += Kills
        Raid_Tot_Deaths += Deaths
        Raid_Tot_Time += Time

        print(Raids)

    Seconds = Raid_Tot_Time % 60
    Minutes = Raid_Tot_Time / 60
    Minutes = math.trunc(Minutes)
    Hours = Minutes / 60
    Hours = math.trunc(Hours)
    Minutes = Minutes % 60
    Days = Hours / 24
    Days = math.trunc(Days)
    Hours = Hours % 24
    Weeks = Days / 7
    Weeks = math.trunc(Weeks)
    Days = Days % 7

    Raid_Tot_Time = (f'{Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}')

    print(Raid_Tot_Time, Raid_Tot_Kills, Raid_Tot_Deaths)