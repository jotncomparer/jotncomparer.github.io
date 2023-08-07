# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-7-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at triumph score for all players.

import json
from prettytable import PrettyTable

def allProfileData():
    with open('Metrics.json') as f:
        data1 = json.load(f)
    with open('Metrics_2.json') as f:
        data2 = json.load(f)
    with open('Metrics_3.json') as f:
        data3 = json.load(f)
    with open('Metrics_4.json') as f:
        data4 = json.load(f)
    with open('Metrics_5.json') as f:
        data5 = json.load(f)
    with open('Metrics_6.json') as f:
        data6 = json.load(f)
    with open('Metrics_7.json') as f:
        data7 = json.load(f)
    with open('Metrics_8.json') as f:
        data8 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]
    items4 = data4["Response"]
    items5 = data5["Response"]
    items6 = data6["Response"]
    items7 = data7["Response"]
    items8 = data8["Response"]

    metric_json = {"Response": []}
    metric_json['Response'].append(items1)
    metric_json['Response'].append(items2)
    metric_json['Response'].append(items3)
    metric_json['Response'].append(items4)
    metric_json['Response'].append(items5)
    metric_json['Response'].append(items6)
    metric_json['Response'].append(items7)
    metric_json['Response'].append(items8)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    scoreCon = metric_json["Response"][0]["profileRecords"]['data']['score']
    activeScoreCon = metric_json["Response"][0]["profileRecords"]['data']['activeScore']
    legacyScoreCon = metric_json["Response"][0]["profileRecords"]['data']['legacyScore']
    lifetimeScoreCon = metric_json["Response"][0]["profileRecords"]['data']['lifetimeScore']

    scoreTom = metric_json["Response"][1]["profileRecords"]['data']['score']
    activeScoreTom = metric_json["Response"][1]["profileRecords"]['data']['activeScore']
    legacyScoreTom = metric_json["Response"][1]["profileRecords"]['data']['legacyScore']
    lifetimeScoreTom = metric_json["Response"][1]["profileRecords"]['data']['lifetimeScore']

    scoreDoug = metric_json["Response"][2]["profileRecords"]['data']['score']
    activeScoreDoug = metric_json["Response"][2]["profileRecords"]['data']['activeScore']
    legacyScoreDoug = metric_json["Response"][2]["profileRecords"]['data']['legacyScore']
    lifetimeScoreDoug = metric_json["Response"][2]["profileRecords"]['data']['lifetimeScore']

    scoreMark = metric_json["Response"][3]["profileRecords"]['data']['score']
    activeScoreMark = metric_json["Response"][3]["profileRecords"]['data']['activeScore']
    legacyScoreMark = metric_json["Response"][3]["profileRecords"]['data']['legacyScore']
    lifetimeScoreMark = metric_json["Response"][3]["profileRecords"]['data']['lifetimeScore']

    scoreJack = metric_json["Response"][4]["profileRecords"]['data']['score']
    activeScoreJack = metric_json["Response"][4]["profileRecords"]['data']['activeScore']
    legacyScoreJack = metric_json["Response"][4]["profileRecords"]['data']['legacyScore']
    lifetimeScoreJack = metric_json["Response"][4]["profileRecords"]['data']['lifetimeScore']

    scoreHunt = metric_json["Response"][5]["profileRecords"]['data']['score']
    activeScoreHunt = metric_json["Response"][5]["profileRecords"]['data']['activeScore']
    legacyScoreHunt = metric_json["Response"][5]["profileRecords"]['data']['legacyScore']
    lifetimeScoreHunt = metric_json["Response"][5]["profileRecords"]['data']['lifetimeScore']

    scoreCam = metric_json["Response"][6]["profileRecords"]['data']['score']
    activeScoreCam = metric_json["Response"][6]["profileRecords"]['data']['activeScore']
    legacyScoreCam = metric_json["Response"][6]["profileRecords"]['data']['legacyScore']
    lifetimeScoreCam = metric_json["Response"][6]["profileRecords"]['data']['lifetimeScore']

    scoreKade = metric_json["Response"][7]["profileRecords"]['data']['score']
    activeScoreKade = metric_json["Response"][7]["profileRecords"]['data']['activeScore']
    legacyScoreKade = metric_json["Response"][7]["profileRecords"]['data']['legacyScore']
    lifetimeScoreKade = metric_json["Response"][7]["profileRecords"]['data']['lifetimeScore']

    profileTable = PrettyTable()
    profileTable.field_names = ['Triumph Score', 'Connor', 'Thomas', 'Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron', 'Kade']
    profileTable.add_rows(
        [
            ['Lifetime Score', lifetimeScoreCon, lifetimeScoreTom, lifetimeScoreDoug, lifetimeScoreMark, lifetimeScoreJack, lifetimeScoreHunt, lifetimeScoreCam, lifetimeScoreKade],
            ['Active Score', activeScoreCon, activeScoreTom, activeScoreDoug, activeScoreMark, activeScoreJack, activeScoreHunt, activeScoreCam, activeScoreKade],
            ['Legacy Score', legacyScoreCon, legacyScoreTom, legacyScoreDoug, legacyScoreMark, legacyScoreJack, legacyScoreHunt, legacyScoreCam, legacyScoreKade],
            ['Score', scoreCon, scoreTom, scoreDoug, scoreMark, scoreJack, scoreHunt, scoreCam, scoreKade]
        ]
    )
    profileTable.reversesort = True
    print(profileTable)