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
          f"{characterId}/Stats/Activities/?mode={MODE}&count=250&page=1"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    char_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Char_4.json', 'w')
    writeFile.write(char_data)


def allCharsFourPages(MODE):
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

        items1 = data1["Response"]
        items2 = data2["Response"]
        items3 = data3["Response"]
        items4 = data4["Response"]

        char_json = {"Response": []}

        char_json['Response'].append(items1)
        char_json["Response"].append(items2)
        char_json["Response"].append(items3)
        char_json["Response"].append(items4)

        with open('char.json', "w") as f:
            f.write(json.dumps(char_json, indent=2))

        activities_len_1 = len(char_json["Response"][0]['activities'])
        activities_len_2 = len(char_json["Response"][1]['activities'])
        activities_len_3 = len(char_json["Response"][2]['activities'])
        activities_len_4 = len(char_json["Response"][3]['activities'])

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
        Dungeon_Tot_Kills = 0
        Dungeon_Tot_Deaths = 0
        Dungeon_Tot_Time = 0

        # Total for specific Dungeons
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
        with open('Char_3.json') as f:
            data3 = json.load(f)
        with open('Char_4.json') as f:
            data4 = json.load(f)

        items1 = data1["Response"]
        items2 = data2["Response"]
        items3 = data3["Response"]
        items4 = data4["Response"]

        char_json = {"Response": []}

        char_json['Response'].append(items1)
        char_json["Response"].append(items2)
        char_json["Response"].append(items3)
        char_json["Response"].append(items4)

        with open('char.json', "w") as f:
            f.write(json.dumps(char_json, indent=2))

        activities_len_1 = len(char_json["Response"][0]['activities'])
        activities_len_2 = len(char_json["Response"][1]['activities'])
        activities_len_3 = len(char_json["Response"][2]['activities'])
        activities_len_4 = len(char_json["Response"][3]['activities'])

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
        for number in range(0, activities_len_3):
            Dungeon_Name_3 = char_json["Response"][2]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_3 = char_json["Response"][2]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_3 = char_json["Response"][2]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_3 = \
                char_json["Response"][2]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_3 = \
                char_json["Response"][2]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_3 = \
                char_json["Response"][2]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_3 = \
                char_json["Response"][2]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_3 = char_json["Response"][2]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_3)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_3)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_3)
            Dungeon_KD['K/D'].append(Dungeon_KD_3)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_3)
            Dungeon_Time['Time'].append(Dungeon_Time_3)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_3)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_3)
        for number in range(0, activities_len_4):
            Dungeon_Name_4 = char_json["Response"][3]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_4 = char_json["Response"][3]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_4 = char_json["Response"][3]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_4 = \
                char_json["Response"][3]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_4 = \
                char_json["Response"][3]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_4 = \
                char_json["Response"][3]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_4 = \
                char_json["Response"][3]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_4 = char_json["Response"][3]["activities"][number]["values"]["completed"]["basic"][
                "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_4)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_4)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_4)
            Dungeon_KD['K/D'].append(Dungeon_KD_4)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_4)
            Dungeon_Time['Time'].append(Dungeon_Time_4)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_4)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_4)
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
