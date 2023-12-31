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

def Time_Converter(time):
    Seconds = time % 60
    Minutes = time / 60
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
    print(f'Total Time: {Weeks} week(s), {Days} day(s), {Hours}:{Minutes}:{Seconds}')

print("Players: Connor, Thomas, Douglas, Hunter, Mark, Jack, Cameron, Kade")
print("Player Name: Man in the Moon, The Chrome Leaf, "
      "Piepuns, Lachlan, TheZefraOracle, HeavyChevy, SlayWarsV, Gargoyle Goose")
USER = input("Please type a player or player name from the above lists to analyse: ")
print("Titan, Warlock, Hunter, All, Main")
CHAR = input("Please designate which class to analyse: ")

if USER == "Man in the Moon" or USER == "Connor":
    membershipType = 1
    destinyMembershipId = 4611686018450697084
    if CHAR == "Titan" or CHAR == "Main":
        characterId = 2305843009644414176
        RAID_PAGES = 1
        DUNGEON_PAGES = 2
    elif CHAR == "Warlock":
        characterId = 2305843009663894341
        RAID_PAGES = 1
        DUNGEON_PAGES = 0
    elif CHAR == "Hunter":
        characterId = 2305843009703275457
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")
if USER == "The Chrome Leaf" or USER == "Thomas":
    membershipType = 1
    destinyMembershipId = 4611686018444441571
    if CHAR == "Warlock" or CHAR == "Main":
        characterId = 2305843009265786295
        RAID_PAGES = 2
        DUNGEON_PAGES = 2
    elif CHAR == "Titan":
        characterId = 2305843009283965144
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Hunter":
        characterId = 2305843009569534739
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")
if USER == "Piepuns" or USER == "Douglas":
    membershipType = 1
    destinyMembershipId = 4611686018434621591
    if CHAR == "Hunter" or CHAR == "Main":
        characterId = 2305843010083874501
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Warlock":
        characterId = 2305843009301374530
        RAID_PAGES = 2
        DUNGEON_PAGES = 1
    elif CHAR == "Titan":
        characterId = 2305843009293915719
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")
if USER == "TheZefraOracle" or USER == "Mark":
    membershipType = 1
    destinyMembershipId = 4611686018432221111
    if CHAR == "Titan" or CHAR == "Main":
        characterId = 2305843009668854600
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Hunter":
        characterId = 2305843009348154555
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Warlock":
        characterId = 2305843009802904121
        RAID_PAGES = 0
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")
if USER == "HeavyChevy" or USER == "Jack":
    membershipType = 2
    destinyMembershipId = 4611686018469231992
    if CHAR == "Hunter" or CHAR == "Main":
        characterId = 2305843009268771475
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Warlock":
        characterId = 2305843009891864023
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Titan":
        characterId = 2305843009890274343
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")
if USER == "Lachlan" or USER == "Hunter":
    membershipType = 3
    destinyMembershipId = 4611686018476416864
    if CHAR == "Hunter" or CHAR == "Main":
        characterId = 2305843009359734078
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Warlock":
        characterId = 2305843009359365362
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Titan":
        characterId = 2305843009756404411
        RAID_PAGES = 0
        DUNGEON_PAGES = 0
    else:
        print("Please type an available class")
if USER == "SlayWarsV" or USER == "Cameron":
    membershipType = 3
    destinyMembershipId = 4611686018501646188
    if CHAR == "Warlock" or CHAR == "Main":
        characterId = 2305843009683284493
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Titan":
        characterId = 2305843009624174508
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Hunter":
        characterId = 2305843009683284492
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")
if USER == "Gargoyle Goose" or USER == "Kade":
    membershipType = 1
    destinyMembershipId = 4611686018451886498
    if CHAR == "Warlock" or CHAR == "Main":
        characterId = 2305843009264637524
        RAID_PAGES = 1
        DUNGEON_PAGES = 1
    elif CHAR == "Titan":
        characterId = 2305843009264637527
        RAID_PAGES = 1
        DUNGEON_PAGES = 0
    elif CHAR == "Hunter":
        characterId = 2305843010322954573
        RAID_PAGES = 0
        DUNGEON_PAGES = 1
    else:
        print("Please type an available class")

# Clan ID
groupId = 4268087

MODE = input("Choose either Raid or Dungeon to analyse: ")
if MODE == "Raid":
    MODE = 4
elif MODE == "Dungeon":
    MODE = 82
else:
    print("Please type an available activity type.")
COUNT = 250
PAGE = 0

# 2 Pages of Raid Values per Character
if MODE == 4 and RAID_PAGES == 2:

    # All Raid Data
    # Totals for all Raids
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
    activities_len_2 = len(Raid_data_json["Response"][1]['activities'])

    if activities_len_1 and activities_len_2 > 0:
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
        for number in range(0, activities_len_2):
            Raid_Name_2 = Raid_data_json["Response"][1]["activities"][number]["activityDetails"]["referenceId"]
            Raid_Kills_2 = Raid_data_json["Response"][1]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Raid_Deaths_2 = Raid_data_json["Response"][1]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Raid_KD_2 = \
            Raid_data_json["Response"][1]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                "value"]
            Raid_KAD_2 = \
            Raid_data_json["Response"][1]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                "value"]
            Raid_Time_2 = \
                Raid_data_json["Response"][1]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Raid_PlayerCount_2 = \
                Raid_data_json["Response"][1]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Raid_Complete_2 = Raid_data_json["Response"][1]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Raid_Name['Raid'].append(Raid_Name_2)
            Raid_Kills['Kills'].append(Raid_Kills_2)
            Raid_Deaths['Deaths'].append(Raid_Deaths_2)
            Raid_KD['K/D'].append(Raid_KD_2)
            Raid_KAD['KA/D'].append(Raid_KAD_2)
            Raid_Time['Time'].append(Raid_Time_2)
            Raid_PlayerCount['Player Count'].append(Raid_PlayerCount_2)
            Raid_Complete['Completion'].append(Raid_Complete_2)

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
            if Completion == 1:
                LW_Comp += 1
            LW_Tot_Time += Time
            LW_Tot_K += Kills
            LW_Tot_D += Deaths
        elif Name == 3458480158 or Name == 2659723068:
            Name = "Garden of Salvation"
            GoS_Start += 1
            if Completion == 1:
                GoS_Comp += 1
            GoS_Tot_Time += Time
            GoS_Tot_K += Kills
            GoS_Tot_D += Deaths
        elif Name == 910380154:
            Name = "Deep Stone Crypt"
            DSC_Start += 1
            if Completion == 1:
                DSC_Comp += 1
            DSC_Tot_Time += Time
            DSC_Tot_K += Kills
            DSC_Tot_D += Deaths
        elif Name == 3881495763:
            Name = "Vault of Glass"
            VoG_Start += 1
            if Completion == 1:
                VoG_Comp += 1
            VoG_Tot_Time += Time
            VoG_Tot_K += Kills
            VoG_Tot_D += Deaths
        elif Name == 1441982566:
            Name = "Vow of the Disciple"
            Vow_Start += 1
            if Completion == 1:
                Vow_Comp += 1
            Vow_Tot_Time += Time
            Vow_Tot_K += Kills
            Vow_Tot_D += Deaths
        elif Name == 1374392663 or Name == 2964135793:
            if Name == 1374392663:
                Name = "King's Fall"
            elif Name == 2964135793:
                Name = "King's Fall: Master"
            KF_Start += 1
            if Completion == 1:
                KF_Comp += 1
            KF_Tot_Time += Time
            KF_Tot_K += Kills
            KF_Tot_D += Deaths
        elif Name == 2381413764:
            Name = "Root of Nightmares"
            Root_Start += 1
            if Completion == 1:
                Root_Comp += 1
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
            if Completion == 1:
                Levi_Comp += 1
            Levi_Tot_Time += Time
            Levi_Tot_K += Kills
            Levi_Tot_D += Deaths
        elif Name == 548750096:
            Name = "Scourge of the Past"
            SotP_Start += 1
            if Completion == 1:
                SotP_Comp += 1
            SotP_Tot_Time += Time
            SotP_Tot_K += Kills
            SotP_Tot_D += Deaths
        elif Name == 3333172150:
            Name = "Crown of Sorrow"
            Crown_Start += 1
            if Completion == 1:
                Crown_Comp += 1
            Crown_Tot_Time += Time
            Crown_Tot_K += Kills
            Crown_Tot_D += Deaths
        elif Name == 3089205900 or Name == 809170886:
            if Name == 3089205900:
                Name = "Eater of Worlds"
            elif Name == 809170886:
                Name ="Prestige Eater of Worlds"
            EoW_Start += 1
            if Completion == 1:
                EoW_Comp += 1
            EoW_Tot_Time += Time
            EoW_Tot_K += Kills
            EoW_Tot_D += Deaths
        elif Name == 119944200:
            Name = "Spire of Stars"
            SoS_Start += 1
            if Completion == 1:
                SoS_Comp += 1
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

        # print(Raids)

    print(f'Total Kills: {round(Raid_Tot_Kills)}\nTotal Deaths: {round(Raid_Tot_Deaths)}')
    Time_Converter(Raid_Tot_Time)

    All_Starts = (Levi_Start, SoS_Start, EoW_Start, Crown_Start, SotP_Start, LW_Start, GoS_Start, DSC_Start, VoG_Start, Vow_Start, KF_Start, Root_Start)
    All_Comps = (Levi_Comp, SoS_Comp, EoW_Comp, Crown_Comp, SotP_Comp, LW_Comp, GoS_Comp, DSC_Comp, VoG_Comp, Vow_Comp, KF_Comp, Root_Comp)
    All_Tot_K = (Levi_Tot_K, SoS_Tot_K, EoW_Tot_K, Crown_Tot_K, SotP_Tot_K, LW_Tot_K, GoS_Tot_K, DSC_Tot_K, VoG_Tot_K, Vow_Tot_K, KF_Tot_K, Root_Tot_K)
    All_Tot_D = (Levi_Tot_D, SoS_Tot_D, EoW_Tot_D, Crown_Tot_D, SotP_Tot_D, LW_Tot_D, GoS_Tot_D, DSC_Tot_D, VoG_Tot_D, Vow_Tot_D, KF_Tot_D, Root_Tot_D)

    All_Stats = (f'Raids Starts: {All_Starts}\nRaids Finished: {All_Comps}\n'
                 f'Total Raid Kills: {All_Tot_K}\nTotal Raid Deaths: {All_Tot_D}')

    print(All_Stats)
    Time_Converter(Levi_Tot_Time)
    Time_Converter(SoS_Tot_Time)
    Time_Converter(EoW_Tot_Time)
    Time_Converter(Crown_Tot_Time)
    Time_Converter(SotP_Tot_Time)
    Time_Converter(LW_Tot_Time)
    Time_Converter(GoS_Tot_Time)
    Time_Converter(DSC_Tot_Time)
    Time_Converter(VoG_Tot_Time)
    Time_Converter(Vow_Tot_Time)
    Time_Converter(KF_Tot_Time)
    Time_Converter(Root_Tot_Time)

# 2 Pages of Dungeon Values per Character
if MODE == 82 and DUNGEON_PAGES == 2:

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
            Spire_Start += 1
            if Completion == 1:
                Spire_Comp += 1
            Spire_Tot_Time += Time
            Spire_Tot_K += Kills
            Spire_Tot_D += Deaths
        elif Name == 2823159265 or Name == 1668217731:
            Name = "Duality"
            Duality_Start += 1
            if Completion == 1:
                Duality_Comp += 1
            Duality_Tot_Time += Time
            Duality_Tot_K += Kills
            Duality_Tot_D += Deaths
        elif Name == 4078656646 or Name == 3774021532:
            Name = "Grasp of Avarice"
            Grasp_Start += 1
            if Completion == 1:
                Grasp_Comp += 1
            Grasp_Tot_Time += Time
            Grasp_Tot_K += Kills
            Grasp_Tot_D += Deaths
        elif Name == 313828469 or Name == 2716998124:
            Name = "Ghosts of the Deep"
            GotD_Start += 1
            if Completion == 1:
                GotD_Comp += 1
            GotD_Tot_Time += Time
            GotD_Tot_K += Kills
            GotD_Tot_D += Deaths
        elif Name == 2032534090:
            Name = "The Shattered Throne"
            ST_Start += 1
            if Completion == 1:
                ST_Comp += 1
            ST_Tot_Time += Time
            ST_Tot_K += Kills
            ST_Tot_D += Deaths
        elif Name == 2582501063 or Name == 1375089621:
            Name = "Pit of Heresy"
            Pit_Start += 1
            if Completion == 1:
                Pit_Comp += 1
            Pit_Tot_Time += Time
            Pit_Tot_K += Kills
            Pit_Tot_D += Deaths
        elif Name == 4148187374 or Name == 1077850348:
            Name = "Prophecy"
            Proph_Start += 1
            if Completion == 1:
                Proph_Comp += 1
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
                    Completion = "Solo Flawless"
        else:
            Completion = "Activity Incompolete"


        Dungeon_Tot_Kills += Kills
        Dungeon_Tot_Deaths += Deaths
        Dungeon_Tot_Time += Time

        Dungeons = (Name, Kills, Deaths, KD, KAD, Time, Players, Completion)

        All_Starts = (ST_Start, Pit_Start, Proph_Start, Grasp_Start, Duality_Start, Spire_Start, GotD_Start)
        All_Comps = (ST_Comp, Pit_Comp, Proph_Comp, Grasp_Comp, Duality_Comp, Spire_Comp, GotD_Comp)
        # All_Tot_Time = (ST_Tot_Time, Pit_Tot_Time, Proph_Tot_Time, Grasp_Tot_Time, Duality_Tot_Time,
        #                Spire_Tot_Time, GotD_Tot_Time)
        All_Tot_K = (round(ST_Tot_K), round(Pit_Tot_K), round(Proph_Tot_K), round(Grasp_Tot_K),
                     round(Duality_Tot_K), round(Spire_Tot_K), round(GotD_Tot_K))
        All_Tot_D = (round(ST_Tot_D), round(Pit_Tot_D), round(Proph_Tot_D), round(Grasp_Tot_D),
                     round(Duality_Tot_D), round(Spire_Tot_D), round(GotD_Tot_D))

        All_Stats = (f'Dungeon Starts: {All_Starts}\nDungeon Finished: {All_Comps}\n'
                     f'Total Dungeon Kills: {All_Tot_K}\nTotal Dungeon Deaths: {All_Tot_D}')

        # print(Dungeons)

    Time_Converter(Dungeon_Tot_Time)

    print(f'Total Kills: {round(Dungeon_Tot_Kills)}\nTotal Deaths: {round(Dungeon_Tot_Deaths)}')
    print(All_Stats)
    Time_Converter(ST_Tot_Time)
    Time_Converter(Pit_Tot_Time)
    Time_Converter(Proph_Tot_Time)
    Time_Converter(Grasp_Tot_Time)
    Time_Converter(Duality_Tot_Time)
    Time_Converter(Spire_Tot_Time)
    Time_Converter(GotD_Tot_Time)

# 1 Page of Raid Values per Character
if MODE == 4 and RAID_PAGES == 1:

    # All Raid Data
    # Totals for all Raids
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
            LW_Start += 1
            if Completion == 1:
                LW_Comp += 1
            LW_Tot_Time += Time
            LW_Tot_K += Kills
            LW_Tot_D += Deaths
        elif Name == 3458480158 or Name == 2659723068:
            Name = "Garden of Salvation"
            GoS_Start += 1
            if Completion == 1:
                GoS_Comp += 1
            GoS_Tot_Time += Time
            GoS_Tot_K += Kills
            GoS_Tot_D += Deaths
        elif Name == 910380154:
            Name = "Deep Stone Crypt"
            DSC_Start += 1
            if Completion == 1:
                DSC_Comp += 1
            DSC_Tot_Time += Time
            DSC_Tot_K += Kills
            DSC_Tot_D += Deaths
        elif Name == 3881495763:
            Name = "Vault of Glass"
            VoG_Start += 1
            if Completion == 1:
                VoG_Comp += 1
            VoG_Tot_Time += Time
            VoG_Tot_K += Kills
            VoG_Tot_D += Deaths
        elif Name == 1441982566:
            Name = "Vow of the Disciple"
            Vow_Start += 1
            if Completion == 1:
                Vow_Comp += 1
            Vow_Tot_Time += Time
            Vow_Tot_K += Kills
            Vow_Tot_D += Deaths
        elif Name == 1374392663 or Name == 2964135793:
            if Name == 1374392663:
                Name = "King's Fall"
            elif Name == 2964135793:
                Name = "King's Fall: Master"
            KF_Start += 1
            if Completion == 1:
                KF_Comp += 1
            KF_Tot_Time += Time
            KF_Tot_K += Kills
            KF_Tot_D += Deaths
        elif Name == 2381413764:
            Name = "Root of Nightmares"
            Root_Start += 1
            if Completion == 1:
                Root_Comp += 1
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
            if Completion == 1:
                Levi_Comp += 1
            Levi_Tot_Time += Time
            Levi_Tot_K += Kills
            Levi_Tot_D += Deaths
        elif Name == 548750096:
            Name = "Scourge of the Past"
            SotP_Start += 1
            if Completion == 1:
                SotP_Comp += 1
            SotP_Tot_Time += Time
            SotP_Tot_K += Kills
            SotP_Tot_D += Deaths
        elif Name == 3333172150:
            Name = "Crown of Sorrow"
            Crown_Start += 1
            if Completion == 1:
                Crown_Comp += 1
            Crown_Tot_Time += Time
            Crown_Tot_K += Kills
            Crown_Tot_D += Deaths
        elif Name == 3089205900 or Name == 809170886:
            if Name == 3089205900:
                Name = "Eater of Worlds"
            elif Name == 809170886:
                Name ="Prestige Eater of Worlds"
            EoW_Start += 1
            if Completion == 1:
                EoW_Comp += 1
            EoW_Tot_Time += Time
            EoW_Tot_K += Kills
            EoW_Tot_D += Deaths
        elif Name == 119944200:
            Name = "Spire of Stars"
            SoS_Start += 1
            if Completion == 1:
                SoS_Comp += 1
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

        # print(Raids)


    print(f'Total Kills: {round(Raid_Tot_Kills)}\nTotal Deaths: {round(Raid_Tot_Deaths)}')
    Time_Converter(Raid_Tot_Time)

    All_Starts = (Levi_Start, SoS_Start, EoW_Start, Crown_Start, SotP_Start, LW_Start, GoS_Start, DSC_Start, VoG_Start, Vow_Start, KF_Start, Root_Start)
    All_Comps = (Levi_Comp, SoS_Comp, EoW_Comp, Crown_Comp, SotP_Comp, LW_Comp, GoS_Comp, DSC_Comp, VoG_Comp, Vow_Comp, KF_Comp, Root_Comp)
    All_Tot_K = (Levi_Tot_K, SoS_Tot_K, EoW_Tot_K, Crown_Tot_K, SotP_Tot_K, LW_Tot_K, GoS_Tot_K, DSC_Tot_K, VoG_Tot_K, Vow_Tot_K, KF_Tot_K, Root_Tot_K)
    All_Tot_D = (Levi_Tot_D, SoS_Tot_D, EoW_Tot_D, Crown_Tot_D, SotP_Tot_D, LW_Tot_D, GoS_Tot_D, DSC_Tot_D, VoG_Tot_D, Vow_Tot_D, KF_Tot_D, Root_Tot_D)

    All_Stats = (f'Raids Starts: {All_Starts}\nRaids Finished: {All_Comps}\n'
                 f'Total Raid Kills: {All_Tot_K}\nTotal Raid Deaths: {All_Tot_D}')

    print(All_Stats)
    Time_Converter(Levi_Tot_Time)
    Time_Converter(SoS_Tot_Time)
    Time_Converter(EoW_Tot_Time)
    Time_Converter(Crown_Tot_Time)
    Time_Converter(SotP_Tot_Time)
    Time_Converter(LW_Tot_Time)
    Time_Converter(GoS_Tot_Time)
    Time_Converter(DSC_Tot_Time)
    Time_Converter(VoG_Tot_Time)
    Time_Converter(Vow_Tot_Time)
    Time_Converter(KF_Tot_Time)
    Time_Converter(Root_Tot_Time)

# 1 Page of Dungeon Values per Character
if MODE == 82 and DUNGEON_PAGES == 1:

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

    if activities_len_1 > 0:
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
            if Completion == 1:
                Spire_Comp += 1
            Spire_Tot_Time += Time
            Spire_Tot_K += Kills
            Spire_Tot_D += Deaths
        elif Name == 2823159265 or Name == 1668217731:
            Name = "Duality"
            Duality_Start += 1
            if Completion == 1:
                Duality_Comp += 1
            Duality_Tot_Time += Time
            Duality_Tot_K += Kills
            Duality_Tot_D += Deaths
        elif Name == 4078656646 or Name == 3774021532:
            Name = "Grasp of Avarice"
            Grasp_Start += 1
            if Completion == 1:
                Grasp_Comp += 1
            Grasp_Tot_Time += Time
            Grasp_Tot_K += Kills
            Grasp_Tot_D += Deaths
        elif Name == 313828469 or Name == 2716998124:
            Name = "Ghosts of the Deep"
            GotD_Start += 1
            if Completion == 1:
                GotD_Comp += 1
            GotD_Tot_Time += Time
            GotD_Tot_K += Kills
            GotD_Tot_D += Deaths
        elif Name == 2032534090:
            Name = "The Shattered Throne"
            ST_Start += 1
            if Completion == 1:
                ST_Comp += 1
            ST_Tot_Time += Time
            ST_Tot_K += Kills
            ST_Tot_D += Deaths
        elif Name == 2582501063 or Name == 1375089621:
            Name = "Pit of Heresy"
            Pit_Start += 1
            if Completion == 1:
                Pit_Comp += 1
            Pit_Tot_Time += Time
            Pit_Tot_K += Kills
            Pit_Tot_D += Deaths
        elif Name == 4148187374 or Name == 1077850348:
            Name = "Prophecy"
            Proph_Start += 1
            if Completion == 1:
                Proph_Comp += 1
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
                    Completion = "Solo Flawless"
        else:
            Completion = "Activity Incompolete"


        Dungeon_Tot_Kills += Kills
        Dungeon_Tot_Deaths += Deaths
        Dungeon_Tot_Time += Time

        Dungeons = (Name, Kills, Deaths, KD, KAD, Time, Players, Completion)

        All_Starts = (ST_Start, Pit_Start, Proph_Start, Grasp_Start, Duality_Start, Spire_Start, GotD_Start)
        All_Comps = (ST_Comp, Pit_Comp, Proph_Comp, Grasp_Comp, Duality_Comp, Spire_Comp, GotD_Comp)
        # All_Tot_Time = (ST_Tot_Time, Pit_Tot_Time, Proph_Tot_Time, Grasp_Tot_Time, Duality_Tot_Time,
        #                Spire_Tot_Time, GotD_Tot_Time)
        All_Tot_K = (round(ST_Tot_K), round(Pit_Tot_K), round(Proph_Tot_K), round(Grasp_Tot_K),
                     round(Duality_Tot_K), round(Spire_Tot_K), round(GotD_Tot_K))
        All_Tot_D = (round(ST_Tot_D), round(Pit_Tot_D), round(Proph_Tot_D), round(Grasp_Tot_D),
                     round(Duality_Tot_D), round(Spire_Tot_D), round(GotD_Tot_D))

        All_Stats = (f'Dungeon Starts: {All_Starts}\nDungeon Finished: {All_Comps}\n'
                     f'Total Dungeon Kills: {All_Tot_K}\nTotal Dungeon Deaths: {All_Tot_D}')

        # print(Dungeons)

    Time_Converter(Dungeon_Tot_Time)

    print(f'Total Kills: {round(Dungeon_Tot_Kills)}\nTotal Deaths: {round(Dungeon_Tot_Deaths)}')
    print(All_Stats)
    Time_Converter(ST_Tot_Time)
    Time_Converter(Pit_Tot_Time)
    Time_Converter(Proph_Tot_Time)
    Time_Converter(Grasp_Tot_Time)
    Time_Converter(Duality_Tot_Time)
    Time_Converter(Spire_Tot_Time)
    Time_Converter(GotD_Tot_Time)
