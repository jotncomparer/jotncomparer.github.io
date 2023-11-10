# Connor Downs
# Started: 8-7-2023
# Last Updated: 11-10-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at commendation scores and commendation card breakdowns for all players.

import json
from prettytable import PrettyTable

def allCommendationData():
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
    with open('Metrics_9.json') as f:
        data9 = json.load(f)

    items1 = data1["Response"]
    items2 = data2["Response"]
    items3 = data3["Response"]
    items4 = data4["Response"]
    items5 = data5["Response"]
    items6 = data6["Response"]
    items7 = data7["Response"]
    items8 = data8["Response"]
    items9 = data9["Response"]

    metric_json = {"Response": []}
    metric_json['Response'].append(items1)
    metric_json['Response'].append(items2)
    metric_json['Response'].append(items3)
    metric_json['Response'].append(items4)
    metric_json['Response'].append(items5)
    metric_json['Response'].append(items6)
    metric_json['Response'].append(items7)
    metric_json['Response'].append(items8)
    metric_json['Response'].append(items9)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    # Guardian Rank Data
    guardianRankCon = metric_json["Response"][0]['profile']['data']['currentGuardianRank']
    guardianRankTom = metric_json["Response"][1]['profile']['data']['currentGuardianRank']
    guardianRankDoug = metric_json["Response"][2]['profile']['data']['currentGuardianRank']
    guardianRankMark = metric_json["Response"][3]['profile']['data']['currentGuardianRank']
    guardianRankJack = metric_json["Response"][4]['profile']['data']['currentGuardianRank']
    guardianRankHunt = metric_json["Response"][5]['profile']['data']['currentGuardianRank']
    guardianRankCam = metric_json["Response"][6]['profile']['data']['currentGuardianRank']
    guardianRankKade = metric_json["Response"][7]['profile']['data']['currentGuardianRank']
    guardianRankNoz = metric_json["Response"][8]['profile']['data']['currentGuardianRank']

    if guardianRankCon <= 6:
        guardianRankTitleCon = 'Blueberry'
    elif guardianRankCon == 7:
        guardianRankTitleCon = 'Elite'
    elif guardianRankCon == 8:
        guardianRankTitleCon = 'Justiciar'
    elif guardianRankCon == 9:
        guardianRankTitleCon = 'Vanquisher'
    elif guardianRankCon == 10:
        guardianRankTitleCon = 'Exemplar'
    elif guardianRankCon == 11:
        guardianRankTitleCon = 'Paragon'

    if guardianRankTom <= 6:
        guardianRankTitleTom = 'Blueberry'
    elif guardianRankTom == 7:
        guardianRankTitleTom = 'Elite'
    elif guardianRankTom == 8:
        guardianRankTitleTom = 'Justiciar'
    elif guardianRankTom == 9:
        guardianRankTitleTom = 'Vanquisher'
    elif guardianRankTom == 10:
        guardianRankTitleTom = 'Exemplar'
    elif guardianRankTom == 11:
        guardianRankTitleTom = 'Paragon'

    if guardianRankDoug <= 6:
        guardianRankTitleTom = 'Blueberry'
    elif guardianRankDoug == 7:
        guardianRankTitleDoug = 'Elite'
    elif guardianRankDoug == 8:
        guardianRankTitleDoug = 'Justiciar'
    elif guardianRankDoug == 9:
        guardianRankTitleDoug = 'Vanquisher'
    elif guardianRankDoug == 10:
        guardianRankTitleDoug = 'Exemplar'
    elif guardianRankDoug == 11:
        guardianRankTitleDoug = 'Paragon'

    if guardianRankMark <= 6:
        guardianRankTitleMark = 'Blueberry'
    elif guardianRankMark == 7:
        guardianRankTitleMark = 'Elite'
    elif guardianRankMark == 8:
        guardianRankTitleMark = 'Justiciar'
    elif guardianRankMark == 9:
        guardianRankTitleMark = 'Vanquisher'
    elif guardianRankMark == 10:
        guardianRankTitleMark = 'Exemplar'
    elif guardianRankMark == 11:
        guardianRankTitleMark = 'Paragon'

    if guardianRankJack <= 6:
        guardianRankTitleJack = 'Blueberry'
    elif guardianRankJack == 7:
        guardianRankTitleJack = 'Elite'
    elif guardianRankJack == 8:
        guardianRankTitleJack = 'Justiciar'
    elif guardianRankJack == 9:
        guardianRankTitleJack = 'Vanquisher'
    elif guardianRankJack == 10:
        guardianRankTitleJack = 'Exemplar'
    elif guardianRankJack == 11:
        guardianRankTitleJack = 'Paragon'

    if guardianRankHunt <= 6:
        guardianRankTitleHunt = 'Blueberry'
    elif guardianRankHunt == 7:
        guardianRankTitleHunt = 'Elite'
    elif guardianRankHunt == 8:
        guardianRankTitleHunt = 'Justiciar'
    elif guardianRankHunt == 9:
        guardianRankTitleHunt = 'Vanquisher'
    elif guardianRankHunt == 10:
        guardianRankTitleHunt = 'Exemplar'
    elif guardianRankHunt == 11:
        guardianRankTitleHunt = 'Paragon'

    if guardianRankCam <= 6:
        guardianRankTitleCam = 'Blueberry'
    elif guardianRankCam == 7:
        guardianRankTitleCam = 'Elite'
    elif guardianRankCam == 8:
        guardianRankTitleCam = 'Justiciar'
    elif guardianRankCam == 9:
        guardianRankTitleCam = 'Vanquisher'
    elif guardianRankCam == 10:
        guardianRankTitleCam = 'Exemplar'
    elif guardianRankCam == 11:
        guardianRankTitleCam = 'Paragon'

    if guardianRankKade <= 6:
        guardianRankTitleKade = 'Blueberry'
    elif guardianRankKade == 7:
        guardianRankTitleKade = 'Elite'
    elif guardianRankKade == 8:
        guardianRankTitleKade = 'Justiciar'
    elif guardianRankKade == 9:
        guardianRankTitleKade = 'Vanquisher'
    elif guardianRankKade == 10:
        guardianRankTitleKade = 'Exemplar'
    elif guardianRankKade == 11:
        guardianRankTitleKade = 'Paragon'

    if guardianRankNoz <= 6:
        guardianRankTitleNoz = 'Blueberry'
    elif guardianRankNoz == 7:
        guardianRankTitleNoz = 'Elite'
    elif guardianRankNoz == 8:
        guardianRankTitleNoz = 'Justiciar'
    elif guardianRankNoz == 9:
        guardianRankTitleNoz = 'Vanquisher'
    elif guardianRankNoz == 10:
        guardianRankTitleNoz = 'Exemplar'
    elif guardianRankNoz == 11:
        guardianRankTitleNoz = 'Paragon'

    guardianRankTable = PrettyTable()
    guardianRankTable.field_names = ['Player', 'Rank', 'Title']
    guardianRankTable.add_rows(
        [
            ['Connor', guardianRankCon, guardianRankTitleCon],
            ['Thomas', guardianRankTom, guardianRankTitleTom],
            ['Douglas', guardianRankDoug, guardianRankTitleDoug],
            ['Mark', guardianRankMark, guardianRankTitleMark],
            ['Jack', guardianRankJack, guardianRankTitleJack],
            ['Hunter', guardianRankHunt, guardianRankTitleHunt],
            ['Cameron', guardianRankCam, guardianRankTitleCam],
            ['Kade', guardianRankKade, guardianRankTitleKade],
            ['Nozyric', guardianRankNoz, guardianRankTitleNoz]
        ]
    )
    print(guardianRankTable)

    # Commendation Score by Types
    totalScoreCon = metric_json["Response"][0]['profileCommendations']['data']['totalScore']
    allyScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreTom = metric_json["Response"][1]['profileCommendations']['data']['totalScore']
    allyScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['totalScore']
    allyScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreMark = metric_json["Response"][3]['profileCommendations']['data']['totalScore']
    allyScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreJack = metric_json["Response"][4]['profileCommendations']['data']['totalScore']
    allyScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['totalScore']
    allyScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreCam = metric_json["Response"][6]['profileCommendations']['data']['totalScore']
    allyScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreKade = metric_json["Response"][7]['profileCommendations']['data']['totalScore']
    allyScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    totalScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['totalScore']
    allyScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    funScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    leadershipScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    masteryScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']

    commendationTable = PrettyTable()
    commendationTable.field_names = ['Commendation Category', 'Connor', 'Thomas', 'Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron', 'Kade', 'Nozyric']
    commendationTable.add_rows(
        [
            ['Ally', allyScoreCon, allyScoreTom, allyScoreDoug, allyScoreMark, allyScoreJack, allyScoreHunt, allyScoreCam, allyScoreKade, allyScoreNoz],
            ['Fun', funScoreCon, funScoreTom, funScoreDoug, funScoreMark, funScoreJack, funScoreHunt, funScoreCam, funScoreKade, funScoreNoz],
            ['Leadership', leadershipScoreCon, leadershipScoreTom, leadershipScoreDoug, leadershipScoreMark, leadershipScoreJack, leadershipScoreHunt, leadershipScoreCam, leadershipScoreKade, leadershipScoreNoz],
            ['Mastery', masteryScoreCon, masteryScoreTom, masteryScoreDoug, masteryScoreMark, masteryScoreJack, masteryScoreHunt, masteryScoreCam, masteryScoreKade, masteryScoreNoz],
            ['Total', totalScoreCon, totalScoreTom, totalScoreDoug, totalScoreMark, totalScoreJack, totalScoreHunt, totalScoreCam, totalScoreKade, totalScoreNoz]
        ]
    )
    commendationTable.reversesort = True
    print(commendationTable.get_string(sortby='Connor'))

    # Specific Commendation Cards
    selflessScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreCon = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreTom = metric_json["Response"][1]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreDoug = metric_json["Response"][2]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreMark = metric_json["Response"][3]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreJack = metric_json["Response"][4]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreHunt = metric_json["Response"][5]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreCam = metric_json["Response"][6]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreKade = metric_json["Response"][7]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # Specific Commendation Cards
    selflessScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    bestDressedScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['357212819']
    primevalInstinctScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    indispensableScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    patientConsiderateScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['2506835299']
    levelHeadedScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    joyBringerScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    thoughfulScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    heroicScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    perceptiveScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    knowledgeableScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['3970150545']
    playmakerScoreNoz = metric_json["Response"][8]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']
    # totalScore = metric_json["Response"][0]['profileCommendations']['data']['commendationScoresByHash']['']

    commendationCardTable = PrettyTable()
    commendationCardTable.field_names = ['Commendation Card', 'Category', 'Connor', 'Thomas', 'Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron', 'Kade', 'Nozyric']
    commendationCardTable.add_rows(
        [
            ['Perceptive', 'Leadership', perceptiveScoreCon, perceptiveScoreTom, perceptiveScoreDoug, perceptiveScoreMark, perceptiveScoreJack, perceptiveScoreHunt, perceptiveScoreCam, perceptiveScoreKade, perceptiveScoreNoz],
            ['Knowledgeable', 'Leadership', knowledgeableScoreCon, knowledgeableScoreTom, knowledgeableScoreDoug, knowledgeableScoreMark, knowledgeableScoreJack, knowledgeableScoreHunt, knowledgeableScoreCam, knowledgeableScoreKade, knowledgeableScoreNoz],
            ['Joy Bringer', 'Fun', joyBringerScoreCon, joyBringerScoreTom, joyBringerScoreDoug, joyBringerScoreMark, joyBringerScoreJack, joyBringerScoreHunt, joyBringerScoreCam, joyBringerScoreKade, joyBringerScoreNoz],
            ['Level-headed', 'Fun', levelHeadedScoreCon, levelHeadedScoreTom, levelHeadedScoreDoug, levelHeadedScoreMark, levelHeadedScoreJack, levelHeadedScoreHunt, levelHeadedScoreCam, levelHeadedScoreKade, levelHeadedScoreNoz],
            ['Best Dressed', 'Fun', bestDressedScoreCon, bestDressedScoreTom, bestDressedScoreDoug, bestDressedScoreMark, bestDressedScoreJack, bestDressedScoreHunt, bestDressedScoreCam, bestDressedScoreKade, bestDressedScoreNoz],
            ['Playmaker', 'Mastery', playmakerScoreCon, playmakerScoreTom, playmakerScoreDoug, playmakerScoreMark, playmakerScoreJack, playmakerScoreHunt, playmakerScoreCam, playmakerScoreKade, playmakerScoreNoz],
            ['Primeval Instinct', 'Mastery', primevalInstinctScoreCon, primevalInstinctScoreTom, primevalInstinctScoreDoug, primevalInstinctScoreMark, primevalInstinctScoreJack, primevalInstinctScoreHunt, primevalInstinctScoreCam, primevalInstinctScoreKade, primevalInstinctScoreNoz],
            ['Heroic', 'Mastery', heroicScoreCon, heroicScoreTom, heroicScoreDoug, heroicScoreMark, heroicScoreJack, heroicScoreHunt, heroicScoreCam, heroicScoreKade, heroicScoreNoz],
            ['Indispensable', 'Ally', indispensableScoreCon, indispensableScoreTom, indispensableScoreDoug, indispensableScoreMark, indispensableScoreJack, indispensableScoreHunt, indispensableScoreCam, indispensableScoreKade, indispensableScoreNoz],
            ['Selfless', 'Ally', selflessScoreCon, selflessScoreTom, selflessScoreDoug, selflessScoreMark, selflessScoreJack, selflessScoreHunt, selflessScoreCam, selflessScoreKade, selflessScoreNoz],
            ['Thoughtful', 'Ally', thoughfulScoreCon, thoughfulScoreTom, thoughfulScoreDoug, thoughfulScoreMark, thoughfulScoreJack, thoughfulScoreHunt, thoughfulScoreCam, thoughfulScoreKade, thoughfulScoreNoz],
            ['Patience and Consideration', 'Ally', patientConsiderateScoreCon, patientConsiderateScoreTom, patientConsiderateScoreDoug, patientConsiderateScoreMark, patientConsiderateScoreJack, patientConsiderateScoreHunt, patientConsiderateScoreCam, patientConsiderateScoreKade, patientConsiderateScoreNoz]
        ]
    )
    commendationCardTable.reversesort = False
    print(commendationCardTable.get_string(sortby='Category'))
