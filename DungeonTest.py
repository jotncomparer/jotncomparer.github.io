# Connor Downs
# Started: 11-10-2023
# Last Updated: 11-17-2023
# This program requires these programs to operate properly: Time_Converter, and JOTUNN.py
# Performs the task of oneCharOnePage and oneCharTwoPages with room to be used for what would have been oneCharThreePages

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


# membershipType = 1
# destinyMembershipId = 4611686018444441571
# characterId = 2305843009265786295
# MODE = 82
# PAGE = 0

def DungeonTest(membershipType, destinyMembershipId, characterId, MODE, PAGE):
    PageCount = 1

    class Dungeon:
        def __init__(self, dungeon_id, dungeon_name):
            self.id = dungeon_id
            self.name = dungeon_name
            self.start = 0
            self.completion = 0
            self.time = 0
            self.kills = 0
            self.deaths = 0
            self.Solo = 0
            self.Flawless = 0
            self.SF = 0

        def dungeonData(self, start, completion, time, kills, deaths, Solo, Flawless, SF):
            self.start += 1
            if Completion == 1:
                self.completion += 1
            self.time += Time
            self.kills += Kills
            self.deaths += Deaths
            if Deaths == 0:
                self.Flawless += 1
            if Players == 1:
                self.Solo += 1
                if Deaths == 0:
                    self.SF += 1

    shatteredThrone = Dungeon(2032534090, 'Shattered Throne')
    pitOfHeresy = Dungeon(2582501063, 'Pit of Heresy')
    pitOfHeresyOld = Dungeon(1375089621, 'Pit of Heresy')
    prophecy = Dungeon(4148187374, 'Prophecy')
    prophecyOld = Dungeon(1077850348, 'Prophecy')
    graspOfAvarice = Dungeon(4078656646, 'Grasp of Avarice')
    goaMaster = Dungeon(3774021532, 'Grasp of Avarice: Master Mode')
    duality = Dungeon(2823159265, 'Duality')
    dMaster = Dungeon(1668217731, 'Duality: Master Mode')
    spireOfTheWatcher = Dungeon(1262462921, 'Spire of the Watcher')
    sotwMaster = Dungeon(1801496203, 'Spire of the Watcher: Master Mode')
    ghostsOfTheDeep = Dungeon(313828469, 'Ghosts of the Deep')
    gotdMaster = Dungeon(2716998124, 'Ghosts of the Deep: Master Mode')

    url = f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/' \
          f'{characterId}/Stats/Activities/?mode={MODE}&count=250&page={PAGE}'
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    response.content.decode('utf-8')
    pretty_Dungeon_data = json.dumps(json.loads(response.content), indent=2)
    writeFile = open('Dungeon_data_1.json', 'w')
    writeFile.write(pretty_Dungeon_data)

    with open('Dungeon_data_1.json.') as f:
        data1 = json.load(f)

    items1 = data1["Response"]

    Dungeon_data_json = {"Response": []}
    Dungeon_data_json['Response'].append(items1)

    with open('Dungeon_data_1.json', "w") as f:
        f.write(json.dumps(Dungeon_data_json, indent=2))

    activities_len_1 = len(Dungeon_data_json["Response"][0]['activities'])

    if activities_len_1 == 250:
        PageCount += 1
        PAGE += 1

        url2 = f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/' \
               f'{characterId}/Stats/Activities/?mode={MODE}&count=250&page={PAGE}'
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url2, headers=headers, data=payload)
        response.content.decode('utf-8')
        pretty_Dungeon_data_2 = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Dungeon_data_2.json', 'w')
        writeFile.write(pretty_Dungeon_data_2)

        with open('Dungeon_data_2.json.') as f:
            data2 = json.load(f)

        items2 = data2["Response"]

        Dungeon_data_json_2 = {"Response": []}
        Dungeon_data_json_2['Response'].append(items2)

        with open('Dungeon_data_2.json', "w") as f:
            f.write(json.dumps(Dungeon_data_json_2, indent=2))

        activities_len_2 = len(Dungeon_data_json_2["Response"][0]['activities'])

        if activities_len_2 == 250:
            PageCount += 1
            PAGE += 1

            url3 = f'https://www.bungie.net/Platform/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/' \
                   f'{characterId}/Stats/Activities/?mode={MODE}&count=250&page={PAGE}'
            payload = {}
            headers = {
                'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
            }

            response = requests.request("GET", url3, headers=headers, data=payload)
            response.content.decode('utf-8')
            pretty_Dungeon_data_3 = json.dumps(json.loads(response.content), indent=2)
            writeFile = open('Dungeon_data_3.json', 'w')
            writeFile.write(pretty_Dungeon_data_3)

            with open('Dungeon_data_3.json.') as f:
                data3 = json.load(f)

            items3 = data3["Response"]

            Dungeon_data_json_3 = {"Response": []}
            Dungeon_data_json_3['Response'].append(items3)

            with open('Dungeon_data_3.json', "w") as f:
                f.write(json.dumps(Dungeon_data_json_3, indent=2))

            activities_len_3 = len(Dungeon_data_json_3["Response"][0]['activities'])

            if activities_len_3 == 250:
                PageCount += 1
                PAGE += 1
            else:
                PageCount == PageCount
                PAGE == PAGE
        else:
            PageCount == PageCount
            PAGE == PAGE
    else:
        PageCount == PageCount
        PAGE == PAGE

    if PageCount == 1:

        with open('Dungeon_data_1.json.') as f:
            data1 = json.load(f)

        items1 = data1["Response"]
        Dungeon_data_json = {"Response": []}
        Dungeon_data_json['Response'].append(items1)

        with open('Dungeon_data.json', "w") as f:
            f.write(json.dumps(Dungeon_data_json, indent=2))

        activities_len_1 = len(Dungeon_data_json["Response"][0][0]['activities'])

        Dungeon_Name = {"Dungeon": []}
        Dungeon_Kills = {"Kills": []}
        Dungeon_Deaths = {"Deaths": []}
        Dungeon_KD = {"K/D": []}
        Dungeon_KAD = {"KA/D": []}
        Dungeon_Time = {"Time": []}
        Dungeon_PlayerCount = {"Player Count": []}
        Dungeon_Complete = {"Completion": []}
        for number in range(0, activities_len_1):
            Dungeon_Name_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["completed"]["basic"][
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
                spireOfTheWatcher.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 2823159265 or Name == 1668217731:
                duality.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 4078656646 or Name == 3774021532:
                graspOfAvarice.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 313828469 or Name == 2716998124:
                ghostsOfTheDeep.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 2032534090:
                shatteredThrone.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 2582501063 or Name == 1375089621:
                pitOfHeresy.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 4148187374 or Name == 1077850348:
                prophecy.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)

        Dungeon_Tot_Start = shatteredThrone.start + pitOfHeresy.start + prophecy.start + graspOfAvarice.start + duality.start + spireOfTheWatcher.start + ghostsOfTheDeep.start
        Dungeon_Tot_Comp = shatteredThrone.completion + pitOfHeresy.completion + prophecy.completion + graspOfAvarice.completion + duality.completion + spireOfTheWatcher.completion + ghostsOfTheDeep.completion
        Dungeon_Tot_Kills = shatteredThrone.kills + pitOfHeresy.kills + prophecy.kills + graspOfAvarice.kills + duality.kills + spireOfTheWatcher.kills + ghostsOfTheDeep.kills
        Dungeon_Tot_Deaths = shatteredThrone.deaths + pitOfHeresy.deaths + prophecy.deaths + graspOfAvarice.deaths + duality.deaths + spireOfTheWatcher.deaths + ghostsOfTheDeep.deaths
        Dungeon_Tot_Time = shatteredThrone.time + pitOfHeresy.time + prophecy.time + graspOfAvarice.time + duality.time + spireOfTheWatcher.time + ghostsOfTheDeep.time

        dungeonTable = PrettyTable()
        dungeonTable.field_names = ["Dungeon", "Starts", "Completions", "Kills", "Deaths", "Total Time"]
        dungeonTable.add_row(["All Dungeons", Dungeon_Tot_Start, Dungeon_Tot_Comp, round(Dungeon_Tot_Kills),
                              round(Dungeon_Tot_Deaths), Time_Converter(Dungeon_Tot_Time)], divider=True)
        dungeonTable.add_row(["Shattered Throne", shatteredThrone.start, shatteredThrone.completion,
                              round(shatteredThrone.kills), round(shatteredThrone.deaths),
                              Time_Converter(shatteredThrone.time)])
        dungeonTable.add_row(["Pit of Heresy", pitOfHeresy.start, pitOfHeresy.completion, round(pitOfHeresy.kills),
                              round(pitOfHeresy.deaths),
                              Time_Converter(pitOfHeresy.time)])
        dungeonTable.add_row(
            ["Prophecy", prophecy.start, prophecy.completion, round(prophecy.kills), round(prophecy.deaths),
             Time_Converter(prophecy.time)])
        dungeonTable.add_row(
            ["Grasp of Avarice", graspOfAvarice.start, graspOfAvarice.completion, round(graspOfAvarice.kills),
             round(graspOfAvarice.deaths),
             Time_Converter(graspOfAvarice.time)])
        dungeonTable.add_row(["Duality", duality.start, duality.completion, round(duality.kills), round(duality.deaths),
                              Time_Converter(duality.time)])
        dungeonTable.add_row(
            ["Spire of the Watcher", spireOfTheWatcher.start, spireOfTheWatcher.completion,
             round(spireOfTheWatcher.kills),
             round(spireOfTheWatcher.deaths),
             Time_Converter(spireOfTheWatcher.time)])
        dungeonTable.add_row(
            ["Ghosts of the Deep", ghostsOfTheDeep.start, ghostsOfTheDeep.completion, round(ghostsOfTheDeep.kills),
             round(ghostsOfTheDeep.deaths),
             Time_Converter(ghostsOfTheDeep.time)])
        print(dungeonTable)

        # SoloTable = PrettyTable()
        # SoloTable.field_names = ["Dungeon", "Solo", "Flawless", "Solo Flawless"]
        # SoloTable.add_row(["All Dungeons", Dungeon_Tot_Solo, Dungeon_Tot_Flawless, Dungeon_Tot_Solo_Flawless],
        #                   divider=True)
        # SoloTable.add_row(["Shattered Throne", ST_Tot_Solo, ST_Tot_Flawless, ST_Tot_Solo_Flawless])
        # SoloTable.add_row(["Pit of Heresy", Pit_Tot_Solo, Pit_Tot_Flawless, Pit_Tot_Solo_Flawless])
        # SoloTable.add_row(["Prophecy", Proph_Tot_Solo, Proph_Tot_Flawless, Proph_Tot_Solo_Flawless])
        # SoloTable.add_row(["Grasp of Avarice", Grasp_Tot_Solo, Grasp_Tot_Flawless, Grasp_Tot_Solo_Flawless])
        # SoloTable.add_row(["Duality", Duality_Tot_Solo, Duality_Tot_Flawless, Duality_Tot_Solo_Flawless])
        # SoloTable.add_row(["Spire of the Watcher", Spire_Tot_Solo, Spire_Tot_Flawless, Spire_Tot_Solo_Flawless])
        # SoloTable.add_row(["Ghosts of the Deep", GotD_Tot_Solo, GotD_Tot_Flawless, GotD_Tot_Solo_Flawless])
        # print(SoloTable)

    elif PageCount == 2:

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

        Dungeon_Name = {"Dungeon": []}
        Dungeon_Kills = {"Kills": []}
        Dungeon_Deaths = {"Deaths": []}
        Dungeon_KD = {"K/D": []}
        Dungeon_KAD = {"KA/D": []}
        Dungeon_Time = {"Time": []}
        Dungeon_PlayerCount = {"Player Count": []}
        Dungeon_Complete = {"Completion": []}
        for number in range(0, activities_len_1):
            Dungeon_Name_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["completed"]["basic"][
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
            Dungeon_Name_2 = Dungeon_data_json["Response"][1][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_2 = Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_2 = Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["completed"]["basic"][
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
                spireOfTheWatcher.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 2823159265 or Name == 1668217731:
                duality.dungeonData(1, 1, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 4078656646 or Name == 3774021532:
                graspOfAvarice.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 313828469 or Name == 2716998124:
                ghostsOfTheDeep.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 2032534090:
                shatteredThrone.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 2582501063 or Name == 1375089621:
                pitOfHeresy.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 4148187374 or Name == 1077850348:
                prophecy.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)

        Dungeon_Tot_Start = shatteredThrone.start + pitOfHeresy.start + prophecy.start + graspOfAvarice.start + duality.start + spireOfTheWatcher.start + ghostsOfTheDeep.start
        Dungeon_Tot_Comp = shatteredThrone.completion + pitOfHeresy.completion + prophecy.completion + graspOfAvarice.completion + duality.completion + spireOfTheWatcher.completion + ghostsOfTheDeep.completion
        Dungeon_Tot_Kills = shatteredThrone.kills + pitOfHeresy.kills + prophecy.kills + graspOfAvarice.kills + duality.kills + spireOfTheWatcher.kills + ghostsOfTheDeep.kills
        Dungeon_Tot_Deaths = shatteredThrone.deaths + pitOfHeresy.deaths + prophecy.deaths + graspOfAvarice.deaths + duality.deaths + spireOfTheWatcher.deaths + ghostsOfTheDeep.deaths
        Dungeon_Tot_Time = shatteredThrone.time + pitOfHeresy.time + prophecy.time + graspOfAvarice.time + duality.time + spireOfTheWatcher.time + ghostsOfTheDeep.time

        dungeonTable = PrettyTable()
        dungeonTable.field_names = ["Dungeon", "Starts", "Completions", "Kills", "Deaths", "Total Time"]
        dungeonTable.add_row(["All Dungeons", Dungeon_Tot_Start, Dungeon_Tot_Comp, round(Dungeon_Tot_Kills),
                              round(Dungeon_Tot_Deaths), Time_Converter(Dungeon_Tot_Time)], divider=True)
        dungeonTable.add_row(["Shattered Throne", shatteredThrone.start, shatteredThrone.completion,
                              round(shatteredThrone.kills), round(shatteredThrone.deaths),
                              Time_Converter(shatteredThrone.time)])
        dungeonTable.add_row(["Pit of Heresy", pitOfHeresy.start, pitOfHeresy.completion, round(pitOfHeresy.kills),
                              round(pitOfHeresy.deaths),
                              Time_Converter(pitOfHeresy.time)])
        dungeonTable.add_row(
            ["Prophecy", prophecy.start, prophecy.completion, round(prophecy.kills), round(prophecy.deaths),
             Time_Converter(prophecy.time)])
        dungeonTable.add_row(
            ["Grasp of Avarice", graspOfAvarice.start, graspOfAvarice.completion, round(graspOfAvarice.kills),
             round(graspOfAvarice.deaths),
             Time_Converter(graspOfAvarice.time)])
        dungeonTable.add_row(["Duality", duality.start, duality.completion, round(duality.kills), round(duality.deaths),
                              Time_Converter(duality.time)])
        dungeonTable.add_row(
            ["Spire of the Watcher", spireOfTheWatcher.start, spireOfTheWatcher.completion,
             round(spireOfTheWatcher.kills),
             round(spireOfTheWatcher.deaths),
             Time_Converter(spireOfTheWatcher.time)])
        dungeonTable.add_row(
            ["Ghosts of the Deep", ghostsOfTheDeep.start, ghostsOfTheDeep.completion, round(ghostsOfTheDeep.kills),
             round(ghostsOfTheDeep.deaths),
             Time_Converter(ghostsOfTheDeep.time)])
        print(dungeonTable)

        # SoloTable = PrettyTable()
        # SoloTable.field_names = ["Dungeon", "Solo", "Flawless", "Solo Flawless"]
        # SoloTable.add_row(["All Dungeons", Dungeon_Tot_Solo, Dungeon_Tot_Flawless, Dungeon_Tot_Solo_Flawless],
        #                   divider=True)
        # SoloTable.add_row(["Shattered Throne", ST_Tot_Solo, ST_Tot_Flawless, ST_Tot_Solo_Flawless])
        # SoloTable.add_row(["Pit of Heresy", Pit_Tot_Solo, Pit_Tot_Flawless, Pit_Tot_Solo_Flawless])
        # SoloTable.add_row(["Prophecy", Proph_Tot_Solo, Proph_Tot_Flawless, Proph_Tot_Solo_Flawless])
        # SoloTable.add_row(["Grasp of Avarice", Grasp_Tot_Solo, Grasp_Tot_Flawless, Grasp_Tot_Solo_Flawless])
        # SoloTable.add_row(["Duality", Duality_Tot_Solo, Duality_Tot_Flawless, Duality_Tot_Solo_Flawless])
        # SoloTable.add_row(["Spire of the Watcher", Spire_Tot_Solo, Spire_Tot_Flawless, Spire_Tot_Solo_Flawless])
        # SoloTable.add_row(["Ghosts of the Deep", GotD_Tot_Solo, GotD_Tot_Flawless, GotD_Tot_Solo_Flawless])
        # print(SoloTable)
    elif PageCount == 3:

        with open('Dungeon_data_1.json.') as f:
            data1 = json.load(f)
        with open('Dungeon_data_2.json') as f:
            data2 = json.load(f)
        with open('Dungeon_data_3.json') as f:
            data3 = json.load(f)

        items1 = data1["Response"]
        items2 = data2["Response"]
        items3 = data3["Response"]

        Dungeon_data_json = {"Response": []}

        Dungeon_data_json['Response'].append(items1)
        Dungeon_data_json["Response"].append(items2)
        Dungeon_data_json["Response"].append(items3)

        with open('Dungeon_data.json', "w") as f:
            f.write(json.dumps(Dungeon_data_json, indent=2))

        Dungeon_Name = {"Dungeon": []}
        Dungeon_Kills = {"Kills": []}
        Dungeon_Deaths = {"Deaths": []}
        Dungeon_KD = {"K/D": []}
        Dungeon_KAD = {"KA/D": []}
        Dungeon_Time = {"Time": []}
        Dungeon_PlayerCount = {"Player Count": []}
        Dungeon_Complete = {"Completion": []}
        for number in range(0, activities_len_1):
            Dungeon_Name_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_1 = Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_1 = \
                Dungeon_data_json["Response"][0][0]["activities"][number]["values"]["completed"]["basic"][
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
            Dungeon_Name_2 = Dungeon_data_json["Response"][1][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_2 = Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_2 = Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_2 = \
                Dungeon_data_json["Response"][1][0]["activities"][number]["values"]["completed"]["basic"][
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
            Dungeon_Name_3 = Dungeon_data_json["Response"][2][0]["activities"][number]["activityDetails"]["referenceId"]
            Dungeon_Kills_3 = Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["kills"]["basic"][
                "value"]
            Dungeon_Deaths_3 = Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["deaths"]["basic"][
                "value"]
            Dungeon_KD_3 = \
                Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["killsDeathsRatio"]["basic"][
                    "value"]
            Dungeon_KAD_3 = \
                Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["killsDeathsAssists"]["basic"][
                    "value"]
            Dungeon_Time_3 = \
                Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["activityDurationSeconds"]["basic"][
                    "value"]
            Dungeon_PlayerCount_3 = \
                Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["playerCount"]["basic"]["value"]
            Dungeon_Complete_3 = \
                Dungeon_data_json["Response"][2][0]["activities"][number]["values"]["completed"]["basic"][
                    "value"]
            Dungeon_Name['Dungeon'].append(Dungeon_Name_3)
            Dungeon_Kills['Kills'].append(Dungeon_Kills_3)
            Dungeon_Deaths['Deaths'].append(Dungeon_Deaths_3)
            Dungeon_KD['K/D'].append(Dungeon_KD_3)
            Dungeon_KAD['KA/D'].append(Dungeon_KAD_3)
            Dungeon_Time['Time'].append(Dungeon_Time_3)
            Dungeon_PlayerCount['Player Count'].append(Dungeon_PlayerCount_3)
            Dungeon_Complete['Completion'].append(Dungeon_Complete_3)
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
                spireOfTheWatcher.dungeonData(1, 1, Time, Kills, Deaths, 1, 1, 1)
            elif Name == 2823159265 or Name == 1668217731:
                duality.dungeonData(1, 1, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 4078656646 or Name == 3774021532:
                graspOfAvarice.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 313828469 or Name == 2716998124:
                ghostsOfTheDeep.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 2032534090:
                shatteredThrone.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 2582501063 or Name == 1375089621:
                pitOfHeresy.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)
            elif Name == 4148187374 or Name == 1077850348:
                prophecy.dungeonData(1, 0, Time, Kills, Deaths, 0, 0, 0)

        Dungeon_Tot_Start = shatteredThrone.start + pitOfHeresy.start + prophecy.start + graspOfAvarice.start + duality.start + spireOfTheWatcher.start + ghostsOfTheDeep.start
        Dungeon_Tot_Comp = shatteredThrone.completion + pitOfHeresy.completion + prophecy.completion + graspOfAvarice.completion + duality.completion + spireOfTheWatcher.completion + ghostsOfTheDeep.completion
        Dungeon_Tot_Kills = shatteredThrone.kills + pitOfHeresy.kills + prophecy.kills + graspOfAvarice.kills + duality.kills + spireOfTheWatcher.kills + ghostsOfTheDeep.kills
        Dungeon_Tot_Deaths = shatteredThrone.deaths + pitOfHeresy.deaths + prophecy.deaths + graspOfAvarice.deaths + duality.deaths + spireOfTheWatcher.deaths + ghostsOfTheDeep.deaths
        Dungeon_Tot_Time = shatteredThrone.time + pitOfHeresy.time + prophecy.time + graspOfAvarice.time + duality.time + spireOfTheWatcher.time + ghostsOfTheDeep.time

        dungeonTable = PrettyTable()
        dungeonTable.field_names = ["Dungeon", "Starts", "Completions", "Kills", "Deaths", "Total Time"]
        dungeonTable.add_row(["All Dungeons", Dungeon_Tot_Start, Dungeon_Tot_Comp, round(Dungeon_Tot_Kills),
                              round(Dungeon_Tot_Deaths), Time_Converter(Dungeon_Tot_Time)], divider=True)
        dungeonTable.add_row(["Shattered Throne", shatteredThrone.start, shatteredThrone.completion,
                              round(shatteredThrone.kills), round(shatteredThrone.deaths),
                              Time_Converter(shatteredThrone.time)])
        dungeonTable.add_row(["Pit of Heresy", pitOfHeresy.start, pitOfHeresy.completion, round(pitOfHeresy.kills),
                              round(pitOfHeresy.deaths),
                              Time_Converter(pitOfHeresy.time)])
        dungeonTable.add_row(
            ["Prophecy", prophecy.start, prophecy.completion, round(prophecy.kills), round(prophecy.deaths),
             Time_Converter(prophecy.time)])
        dungeonTable.add_row(
            ["Grasp of Avarice", graspOfAvarice.start, graspOfAvarice.completion, round(graspOfAvarice.kills),
             round(graspOfAvarice.deaths),
             Time_Converter(graspOfAvarice.time)])
        dungeonTable.add_row(["Duality", duality.start, duality.completion, round(duality.kills), round(duality.deaths),
                              Time_Converter(duality.time)])
        dungeonTable.add_row(
            ["Spire of the Watcher", spireOfTheWatcher.start, spireOfTheWatcher.completion,
             round(spireOfTheWatcher.kills),
             round(spireOfTheWatcher.deaths),
             Time_Converter(spireOfTheWatcher.time)])
        dungeonTable.add_row(
            ["Ghosts of the Deep", ghostsOfTheDeep.start, ghostsOfTheDeep.completion, round(ghostsOfTheDeep.kills),
             round(ghostsOfTheDeep.deaths),
             Time_Converter(ghostsOfTheDeep.time)])
        print(dungeonTable)

        # SoloTable = PrettyTable()
        # SoloTable.field_names = ["Dungeon", "Solo", "Flawless", "Solo Flawless"]
        # SoloTable.add_row(["All Dungeons", Dungeon_Tot_Solo, Dungeon_Tot_Flawless, Dungeon_Tot_Solo_Flawless],
        #                   divider=True)
        # SoloTable.add_row(["Shattered Throne", ST_Tot_Solo, ST_Tot_Flawless, ST_Tot_Solo_Flawless])
        # SoloTable.add_row(["Pit of Heresy", Pit_Tot_Solo, Pit_Tot_Flawless, Pit_Tot_Solo_Flawless])
        # SoloTable.add_row(["Prophecy", Proph_Tot_Solo, Proph_Tot_Flawless, Proph_Tot_Solo_Flawless])
        # SoloTable.add_row(["Grasp of Avarice", Grasp_Tot_Solo, Grasp_Tot_Flawless, Grasp_Tot_Solo_Flawless])
        # SoloTable.add_row(["Duality", Duality_Tot_Solo, Duality_Tot_Flawless, Duality_Tot_Solo_Flawless])
        # SoloTable.add_row(["Spire of the Watcher", Spire_Tot_Solo, Spire_Tot_Flawless, Spire_Tot_Solo_Flawless])
        # SoloTable.add_row(["Ghosts of the Deep", GotD_Tot_Solo, GotD_Tot_Flawless, GotD_Tot_Solo_Flawless])
        # print(SoloTable)
