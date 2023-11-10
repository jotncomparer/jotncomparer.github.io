# Connor Downs
# Started: 8-7-2023
# Last Updated: 11-10-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at title completion for all players.

import json
from prettytable import PrettyTable


def allRecordsData():
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

    connorTitle = 0
    thomasTitle = 0
    douglasTitle = 0
    markTitle = 0
    jackTitle = 0
    hunterTitle = 0
    cameronTitle = 0
    kadeTitle = 0
    nozTitle = 0

    # Haruspex
    harusCon = metric_json["Response"][0]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusCon == True:
        connorTitle += 1
    harusTom = metric_json["Response"][1]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusTom == True:
        thomasTitle += 1
    harusDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusDoug == True:
        douglasTitle += 1
    harusMark = metric_json["Response"][3]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusMark == True:
        markTitle += 1
    harusJack = metric_json["Response"][4]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusJack == True:
        jackTitle += 1
    harusHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusHunt == True:
        hunterTitle += 1
    harusCam = metric_json["Response"][6]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusCam == True:
        cameronTitle += 1
    harusKade = metric_json["Response"][7]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusKade == True:
        kadeTitle += 1
    harusNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2269203216']["objectives"][0][
        'complete']
    if harusNoz == True:
        nozTitle += 1
    # Swordbearer
    swordCon = metric_json["Response"][0]['profileRecords']['data']['records']['865076293']["objectives"][0]['complete']
    if swordCon == True:
        connorTitle += 1
    swordTom = metric_json["Response"][1]['profileRecords']['data']['records']['865076293']["objectives"][0]['complete']
    if swordTom == True:
        thomasTitle += 1
    swordDoug = metric_json["Response"][2]['profileRecords']['data']['records']['865076293']["objectives"][0][
        'complete']
    if swordDoug == True:
        douglasTitle += 1
    swordMark = metric_json["Response"][3]['profileRecords']['data']['records']['865076293']["objectives"][0][
        'complete']
    if swordMark == True:
        markTitle += 1
    swordJack = metric_json["Response"][4]['profileRecords']['data']['records']['865076293']["objectives"][0][
        'complete']
    if swordJack == True:
        jackTitle += 1
    swordHunt = metric_json["Response"][5]['profileRecords']['data']['records']['865076293']["objectives"][0][
        'complete']
    if swordHunt == True:
        hunterTitle += 1
    swordCam = metric_json["Response"][6]['profileRecords']['data']['records']['865076293']["objectives"][0]['complete']
    if swordCam == True:
        cameronTitle += 1
    swordKade = metric_json["Response"][7]['profileRecords']['data']['records']['865076293']["objectives"][0][
        'complete']
    if swordKade == True:
        kadeTitle += 1
    swordNoz = metric_json["Response"][8]['profileRecords']['data']['records']['865076293']["objectives"][0]['complete']
    if swordNoz == True:
        nozTitle += 1
    # Aquanaut
    aquanautCon = metric_json["Response"][0]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautCon == True:
        connorTitle += 1
    aquanautTom = metric_json["Response"][1]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautTom == True:
        thomasTitle += 1
    aquanautDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautDoug == True:
        douglasTitle += 1
    aquanautMark = metric_json["Response"][3]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautMark == True:
        markTitle += 1
    aquanautJack = metric_json["Response"][4]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautJack == True:
        jackTitle += 1
    aquanautHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautHunt == True:
        hunterTitle += 1
    aquanautCam = metric_json["Response"][6]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautCam == True:
        cameronTitle += 1
    aquanautKade = metric_json["Response"][7]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautKade == True:
        kadeTitle += 1
    aquanautNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3570567217']["objectives"][0][
        'complete']
    if aquanautNoz == True:
        nozTitle += 1
    # Queensguard
    queensCon = metric_json["Response"][0]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensCon == True:
        connorTitle += 1
    queensTom = metric_json["Response"][1]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensTom == True:
        thomasTitle += 1
    queensDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensDoug == True:
        douglasTitle += 1
    queensMark = metric_json["Response"][3]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensMark == True:
        markTitle += 1
    queensJack = metric_json["Response"][4]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensJack == True:
        jackTitle += 1
    queensHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensHunt == True:
        hunterTitle += 1
    queensCam = metric_json["Response"][6]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensCam == True:
        cameronTitle += 1
    queensKade = metric_json["Response"][7]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensKade == True:
        kadeTitle += 1
    queensNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1722592950']["objectives"][0][
        'complete']
    if queensNoz == True:
        nozTitle += 1
    # Virtual Fighter
    virtFightCon = metric_json["Response"][0]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightCon == True:
        connorTitle += 1
    virtFightTom = metric_json["Response"][1]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightTom == True:
        thomasTitle += 1
    virtFightDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightDoug == True:
        douglasTitle += 1
    virtFightMark = metric_json["Response"][3]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightMark == True:
        markTitle += 1
    virtFightJack = metric_json["Response"][4]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightJack == True:
        jackTitle += 1
    virtFightHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightHunt == True:
        hunterTitle += 1
    virtFightCam = metric_json["Response"][6]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightCam == True:
        cameronTitle += 1
    virtFightKade = metric_json["Response"][7]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightKade == True:
        kadeTitle += 1
    virtFightNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3906538939']["objectives"][0][
        'complete']
    if virtFightNoz == True:
        nozTitle += 1
    # Dream Warrior
    rootOfNightCon = metric_json["Response"][0]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightCon == True:
        connorTitle += 1
    rootOfNightTom = metric_json["Response"][1]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightTom == True:
        thomasTitle += 1
    rootOfNightDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightDoug == True:
        douglasTitle += 1
    rootOfNightMark = metric_json["Response"][3]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightMark == True:
        markTitle += 1
    rootOfNightJack = metric_json["Response"][4]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightJack == True:
        jackTitle += 1
    rootOfNightHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightHunt == True:
        hunterTitle += 1
    rootOfNightCam = metric_json["Response"][6]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightCam == True:
        cameronTitle += 1
    rootOfNightKade = metric_json["Response"][7]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightKade == True:
        kadeTitle += 1
    rootOfNightNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2889189256']["objectives"][0][
        'complete']
    if rootOfNightNoz == True:
        nozTitle += 1
    # Champ
    champCon = metric_json["Response"][0]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champCon == True:
        connorTitle += 1
    champTom = metric_json["Response"][1]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champTom == True:
        thomasTitle += 1
    champDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champDoug == True:
        douglasTitle += 1
    champMark = metric_json["Response"][3]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champMark == True:
        markTitle += 1
    champJack = metric_json["Response"][4]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champJack == True:
        jackTitle += 1
    champHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champHunt == True:
        hunterTitle += 1
    champCam = metric_json["Response"][6]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champCam == True:
        cameronTitle += 1
    champKade = metric_json["Response"][7]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champKade == True:
        kadeTitle += 1
    champNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3646306576']["objectives"][0][
        'complete']
    if champNoz == True:
        nozTitle += 1
    # Star Baker
    starBakerCon = metric_json["Response"][0]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerCon == True:
        connorTitle += 1
    starBakerTom = metric_json["Response"][1]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerTom == True:
        thomasTitle += 1
    starBakerDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerDoug == True:
        douglasTitle += 1
    starBakerMark = metric_json["Response"][3]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerMark == True:
        markTitle += 1
    starBakerJack = metric_json["Response"][4]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerJack == True:
        jackTitle += 1
    starBakerHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerHunt == True:
        hunterTitle += 1
    starBakerCam = metric_json["Response"][6]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerCam == True:
        cameronTitle += 1
    starBakerKade = metric_json["Response"][7]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerKade == True:
        kadeTitle += 1
    starBakerNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2126152885']["objectives"][0][
        'complete']
    if starBakerNoz == True:
        nozTitle += 1
    # Ghoul
    ghoulCon = metric_json["Response"][0]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulCon == True:
        connorTitle += 1
    ghoulTom = metric_json["Response"][1]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulTom == True:
        thomasTitle += 1
    ghoulDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulDoug == True:
        douglasTitle += 1
    ghoulMark = metric_json["Response"][3]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulMark == True:
        markTitle += 1
    ghoulJack = metric_json["Response"][4]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulJack == True:
        jackTitle += 1
    ghoulHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulHunt == True:
        hunterTitle += 1
    ghoulCam = metric_json["Response"][6]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulCam == True:
        cameronTitle += 1
    ghoulKade = metric_json["Response"][7]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulKade == True:
        kadeTitle += 1
    ghoulNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3974717227']["objectives"][0][
        'complete']
    if ghoulNoz == True:
        nozTitle += 1
    # WANTED
    wantedCon = metric_json["Response"][0]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedCon == True:
        connorTitle += 1
    wantedTom = metric_json["Response"][1]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedTom == True:
        thomasTitle += 1
    wantedDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedDoug == True:
        douglasTitle += 1
    wantedMark = metric_json["Response"][3]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedMark == True:
        markTitle += 1
    wantedJack = metric_json["Response"][4]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedJack == True:
        jackTitle += 1
    wantedHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedHunt == True:
        hunterTitle += 1
    wantedCam = metric_json["Response"][6]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedCam == True:
        cameronTitle += 1
    wantedKade = metric_json["Response"][7]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedKade == True:
        kadeTitle += 1
    wantedNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2302993504']["objectives"][0][
        'complete']
    if wantedNoz == True:
        nozTitle += 1
    # Ghost Writer
    ghostWriteCon = metric_json["Response"][0]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteCon == True:
        connorTitle += 1
    ghostWriteTom = metric_json["Response"][1]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteTom == True:
        thomasTitle += 1
    ghostWriteDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteDoug == True:
        douglasTitle += 1
    ghostWriteMark = metric_json["Response"][3]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteMark == True:
        markTitle += 1
    ghostWriteJack = metric_json["Response"][4]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteJack == True:
        jackTitle += 1
    ghostWriteHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteHunt == True:
        hunterTitle += 1
    ghostWriteCam = metric_json["Response"][6]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteCam == True:
        cameronTitle += 1
    ghostWriteKade = metric_json["Response"][7]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteKade == True:
        kadeTitle += 1
    ghostWriteNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1089543274']["objectives"][0][
        'complete']
    if ghostWriteNoz == True:
        nozTitle += 1
    # Glorious
    gloryCon = metric_json["Response"][0]['profileRecords']['data']['records']['969142496']["objectives"][0]['complete']
    if gloryCon == True:
        connorTitle += 1
    gloryTom = metric_json["Response"][1]['profileRecords']['data']['records']['969142496']["objectives"][0]['complete']
    if gloryTom == True:
        thomasTitle += 1
    gloryDoug = metric_json["Response"][2]['profileRecords']['data']['records']['969142496']["objectives"][0][
        'complete']
    if gloryDoug == True:
        douglasTitle += 1
    gloryMark = metric_json["Response"][3]['profileRecords']['data']['records']['969142496']["objectives"][0][
        'complete']
    if gloryMark == True:
        markTitle += 1
    gloryJack = metric_json["Response"][4]['profileRecords']['data']['records']['969142496']["objectives"][0][
        'complete']
    if gloryJack == True:
        jackTitle += 1
    gloryHunt = metric_json["Response"][5]['profileRecords']['data']['records']['969142496']["objectives"][0][
        'complete']
    if gloryHunt == True:
        hunterTitle += 1
    gloryCam = metric_json["Response"][6]['profileRecords']['data']['records']['969142496']["objectives"][0]['complete']
    if gloryCam == True:
        cameronTitle += 1
    gloryKade = metric_json["Response"][7]['profileRecords']['data']['records']['969142496']["objectives"][0][
        'complete']
    if gloryKade == True:
        kadeTitle += 1
    gloryNoz = metric_json["Response"][8]['profileRecords']['data']['records']['969142496']["objectives"][0][
        'complete']
    if gloryNoz == True:
        nozTitle += 1
    # Kingslayer
    kingsFallCon = metric_json["Response"][0]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallCon == True:
        connorTitle += 1
    kingsFallTom = metric_json["Response"][1]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallTom == True:
        thomasTitle += 1
    kingsFallDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallDoug == True:
        douglasTitle += 1
    kingsFallMark = metric_json["Response"][3]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallMark == True:
        markTitle += 1
    kingsFallJack = metric_json["Response"][4]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallJack == True:
        jackTitle += 1
    kingsFallHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallHunt == True:
        hunterTitle += 1
    kingsFallCam = metric_json["Response"][6]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallCam == True:
        cameronTitle += 1
    kingsFallKade = metric_json["Response"][7]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallKade == True:
        kadeTitle += 1
    kingsFallNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3910736783']["objectives"][0][
        'complete']
    if kingsFallNoz == True:
        nozTitle += 1
    # Flamekeeper
    flameCon = metric_json["Response"][0]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameCon == True:
        connorTitle += 1
    flameTom = metric_json["Response"][1]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameTom == True:
        thomasTitle += 1
    flameDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameDoug == True:
        douglasTitle += 1
    flameMark = metric_json["Response"][3]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameMark == True:
        markTitle += 1
    flameJack = metric_json["Response"][4]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameJack == True:
        jackTitle += 1
    flameHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameHunt == True:
        hunterTitle += 1
    flameCam = metric_json["Response"][6]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameCam == True:
        cameronTitle += 1
    flameKade = metric_json["Response"][7]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameKade == True:
        kadeTitle += 1
    flameNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3056675381']["objectives"][0][
        'complete']
    if flameNoz == True:
        nozTitle += 1
    # Reveler
    revelCon = metric_json["Response"][0]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelCon == True:
        connorTitle += 1
    revelTom = metric_json["Response"][1]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelTom == True:
        thomasTitle += 1
    revelDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelDoug == True:
        douglasTitle += 1
    revelMark = metric_json["Response"][3]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelMark == True:
        markTitle += 1
    revelJack = metric_json["Response"][4]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelJack == True:
        jackTitle += 1
    revelHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelHunt == True:
        hunterTitle += 1
    revelCam = metric_json["Response"][6]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelCam == True:
        cameronTitle += 1
    revelKade = metric_json["Response"][7]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelKade == True:
        kadeTitle += 1
    revelNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1228693527']["objectives"][0][
        'complete']
    if revelNoz == True:
        nozTitle += 1
    # Discerpter
    discCon = metric_json["Response"][0]['profileRecords']['data']['records']['3097916612']["objectives"][0]['complete']
    if discCon == True:
        connorTitle += 1
    discTom = metric_json["Response"][1]['profileRecords']['data']['records']['3097916612']["objectives"][0]['complete']
    if discTom == True:
        thomasTitle += 1
    discDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3097916612']["objectives"][0][
        'complete']
    if discDoug == True:
        douglasTitle += 1
    discMark = metric_json["Response"][3]['profileRecords']['data']['records']['3097916612']["objectives"][0][
        'complete']
    if discMark == True:
        markTitle += 1
    discJack = metric_json["Response"][4]['profileRecords']['data']['records']['3097916612']["objectives"][0][
        'complete']
    if discJack == True:
        jackTitle += 1
    discHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3097916612']["objectives"][0][
        'complete']
    if discHunt == True:
        hunterTitle += 1
    discCam = metric_json["Response"][6]['profileRecords']['data']['records']['3097916612']["objectives"][0]['complete']
    if discCam == True:
        cameronTitle += 1
    discKade = metric_json["Response"][7]['profileRecords']['data']['records']['3097916612']["objectives"][0][
        'complete']
    if discKade == True:
        kadeTitle += 1
    discNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3097916612']["objectives"][0][
        'complete']
    if discNoz == True:
        nozTitle += 1
    # Iron Lord
    ironLordCon = metric_json["Response"][0]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordCon == True:
        connorTitle += 1
    ironLordTom = metric_json["Response"][1]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordTom == True:
        thomasTitle += 1
    ironLordDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordDoug == True:
        douglasTitle += 1
    ironLordMark = metric_json["Response"][3]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordMark == True:
        markTitle += 1
    ironLordJack = metric_json["Response"][4]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordJack == True:
        jackTitle += 1
    ironLordHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordHunt == True:
        hunterTitle += 1
    ironLordCam = metric_json["Response"][6]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordCam == True:
        cameronTitle += 1
    ironLordKade = metric_json["Response"][7]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordKade == True:
        kadeTitle += 1
    ironLordNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1564001702']["objectives"][0][
        'complete']
    if ironLordNoz == True:
        nozTitle += 1
    # Gumshoe
    witchQueenCon = metric_json["Response"][0]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenCon == True:
        connorTitle += 1
    witchQueenTom = metric_json["Response"][1]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenTom == True:
        thomasTitle += 1
    witchQueenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenDoug == True:
        douglasTitle += 1
    witchQueenMark = metric_json["Response"][3]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenMark == True:
        markTitle += 1
    witchQueenJack = metric_json["Response"][4]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenJack == True:
        jackTitle += 1
    witchQueenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenHunt == True:
        hunterTitle += 1
    witchQueenCam = metric_json["Response"][6]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenCam == True:
        cameronTitle += 1
    witchQueenKade = metric_json["Response"][7]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenKade == True:
        kadeTitle += 1
    witchQueenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2489106733']["objectives"][0][
        'complete']
    if witchQueenNoz == True:
        nozTitle += 1
    # Disciple Slayer
    vowDiscipleCon = metric_json["Response"][0]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleCon == True:
        connorTitle += 1
    vowDiscipleTom = metric_json["Response"][1]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleTom == True:
        thomasTitle += 1
    vowDiscipleDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleDoug == True:
        douglasTitle += 1
    vowDiscipleMark = metric_json["Response"][3]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleMark == True:
        markTitle += 1
    vowDiscipleJack = metric_json["Response"][4]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleJack == True:
        jackTitle += 1
    vowDiscipleHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleHunt == True:
        hunterTitle += 1
    vowDiscipleCam = metric_json["Response"][6]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleCam == True:
        cameronTitle += 1
    vowDiscipleKade = metric_json["Response"][7]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleKade == True:
        kadeTitle += 1
    vowDiscipleNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1971228746']["objectives"][0][
        'complete']
    if vowDiscipleNoz == True:
        nozTitle += 1
    # Vidmaster
    vidMasterCon = metric_json["Response"][0]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterCon == True:
        connorTitle += 1
    vidMasterTom = metric_json["Response"][1]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterTom == True:
        thomasTitle += 1
    vidMasterDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterDoug == True:
        douglasTitle += 1
    vidMasterMark = metric_json["Response"][3]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterMark == True:
        markTitle += 1
    vidMasterJack = metric_json["Response"][4]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterJack == True:
        jackTitle += 1
    vidMasterHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterHunt == True:
        hunterTitle += 1
    vidMasterCam = metric_json["Response"][6]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterCam == True:
        cameronTitle += 1
    vidMasterKade = metric_json["Response"][7]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterKade == True:
        kadeTitle += 1
    vidMasterNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3588818798']["objectives"][0][
        'complete']
    if vidMasterNoz == True:
        nozTitle += 1
    # Deadeye
    deadEyeCon = metric_json["Response"][0]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeCon == True:
        connorTitle += 1
    deadEyeTom = metric_json["Response"][1]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeTom == True:
        thomasTitle += 1
    deadEyeDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeDoug == True:
        douglasTitle += 1
    deadEyeMark = metric_json["Response"][3]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeMark == True:
        markTitle += 1
    deadEyeJack = metric_json["Response"][4]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeJack == True:
        jackTitle += 1
    deadEyeHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeHunt == True:
        hunterTitle += 1
    deadEyeCam = metric_json["Response"][6]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeCam == True:
        cameronTitle += 1
    deadEyeKade = metric_json["Response"][7]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeKade == True:
        kadeTitle += 1
    deadEyeNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1438167672']["objectives"][0][
        'complete']
    if deadEyeNoz == True:
        nozTitle += 1
    # Flawless
    trialsCon = metric_json["Response"][0]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsCon == True:
        connorTitle += 1
    trialsTom = metric_json["Response"][1]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsTom == True:
        thomasTitle += 1
    trialsDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsDoug == True:
        douglasTitle += 1
    trialsMark = metric_json["Response"][3]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsMark == True:
        markTitle += 1
    trialsJack = metric_json["Response"][4]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsJack == True:
        jackTitle += 1
    trialsHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsHunt == True:
        hunterTitle += 1
    trialsCam = metric_json["Response"][6]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsCam == True:
        cameronTitle += 1
    trialsKade = metric_json["Response"][7]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsKade == True:
        kadeTitle += 1
    trialsNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3298130972']["objectives"][0][
        'complete']
    if trialsNoz == True:
        nozTitle += 1
    # Conqueror
    conquerCon = metric_json["Response"][0]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerCon == True:
        connorTitle += 1
    conquerTom = metric_json["Response"][1]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerTom == True:
        thomasTitle += 1
    conquerDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerDoug == True:
        douglasTitle += 1
    conquerMark = metric_json["Response"][3]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerMark == True:
        markTitle += 1
    conquerJack = metric_json["Response"][4]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerJack == True:
        jackTitle += 1
    conquerHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerHunt == True:
        hunterTitle += 1
    conquerCam = metric_json["Response"][6]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerCam == True:
        cameronTitle += 1
    conquerKade = metric_json["Response"][7]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerKade == True:
        kadeTitle += 1
    conquerNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3464275895']["objectives"][0][
        'complete']
    if conquerNoz == True:
        nozTitle += 1
    # Dredgen
    dredgenCon = metric_json["Response"][0]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenCon == True:
        connorTitle += 1
    dredgenTom = metric_json["Response"][1]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenTom == True:
        thomasTitle += 1
    dredgenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenDoug == True:
        douglasTitle += 1
    dredgenMark = metric_json["Response"][3]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenMark == True:
        markTitle += 1
    dredgenJack = metric_json["Response"][4]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenJack == True:
        jackTitle += 1
    dredgenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenHunt == True:
        hunterTitle += 1
    dredgenCam = metric_json["Response"][6]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenCam == True:
        cameronTitle += 1
    dredgenKade = metric_json["Response"][7]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenKade == True:
        kadeTitle += 1
    dredgenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1556658903']["objectives"][0][
        'complete']
    if dredgenNoz == True:
        nozTitle += 1
    # Splintered
    splintCon = metric_json["Response"][0]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintCon == True:
        connorTitle += 1
    splintTom = metric_json["Response"][1]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintTom == True:
        thomasTitle += 1
    splintDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintDoug == True:
        douglasTitle += 1
    splintMark = metric_json["Response"][3]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintMark == True:
        markTitle += 1
    splintJack = metric_json["Response"][4]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintJack == True:
        jackTitle += 1
    splintHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintHunt == True:
        hunterTitle += 1
    splintCam = metric_json["Response"][6]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintCam == True:
        cameronTitle += 1
    splintKade = metric_json["Response"][7]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintKade == True:
        kadeTitle += 1
    splintNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2482004751']["objectives"][0][
        'complete']
    if splintNoz == True:
        nozTitle += 1
    # Fatebreaker
    fateCon = metric_json["Response"][0]['profileRecords']['data']['records']['4141971983']["objectives"][0]['complete']
    if fateCon == True:
        connorTitle += 1
    fateTom = metric_json["Response"][1]['profileRecords']['data']['records']['4141971983']["objectives"][0]['complete']
    if fateTom == True:
        thomasTitle += 1
    fateDoug = metric_json["Response"][2]['profileRecords']['data']['records']['4141971983']["objectives"][0][
        'complete']
    if fateDoug == True:
        douglasTitle += 1
    fateMark = metric_json["Response"][3]['profileRecords']['data']['records']['4141971983']["objectives"][0][
        'complete']
    if fateMark == True:
        markTitle += 1
    fateJack = metric_json["Response"][4]['profileRecords']['data']['records']['4141971983']["objectives"][0][
        'complete']
    if fateJack == True:
        jackTitle += 1
    fateHunt = metric_json["Response"][5]['profileRecords']['data']['records']['4141971983']["objectives"][0][
        'complete']
    if fateHunt == True:
        hunterTitle += 1
    fateCam = metric_json["Response"][6]['profileRecords']['data']['records']['4141971983']["objectives"][0]['complete']
    if fateCam == True:
        cameronTitle += 1
    fateKade = metric_json["Response"][7]['profileRecords']['data']['records']['4141971983']["objectives"][0][
        'complete']
    if fateKade == True:
        kadeTitle += 1
    fateNoz = metric_json["Response"][8]['profileRecords']['data']['records']['4141971983']["objectives"][0][
        'complete']
    if fateNoz == True:
        nozTitle += 1
    # Descendant
    descCon = metric_json["Response"][0]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descCon == True:
        connorTitle += 1
    descTom = metric_json["Response"][1]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descTom == True:
        thomasTitle += 1
    descDoug = metric_json["Response"][2]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descDoug == True:
        douglasTitle += 1
    descMark = metric_json["Response"][3]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descMark == True:
        markTitle += 1
    descJack = metric_json["Response"][4]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descJack == True:
        jackTitle += 1
    descHunt = metric_json["Response"][5]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descHunt == True:
        hunterTitle += 1
    descCam = metric_json["Response"][6]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descCam == True:
        cameronTitle += 1
    descKade = metric_json["Response"][7]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descKade == True:
        kadeTitle += 1
    descNoz = metric_json["Response"][8]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    if descNoz == True:
        nozTitle += 1
    # Harbinger
    harbCon = metric_json["Response"][0]['profileRecords']['data']['records']['2584970263']["objectives"][0]['complete']
    if harbCon == True:
        connorTitle += 1
    harbTom = metric_json["Response"][1]['profileRecords']['data']['records']['2584970263']["objectives"][0]['complete']
    if harbTom == True:
        thomasTitle += 1
    harbDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2584970263']["objectives"][0][
        'complete']
    if harbDoug == True:
        douglasTitle += 1
    harbMark = metric_json["Response"][3]['profileRecords']['data']['records']['2584970263']["objectives"][0][
        'complete']
    if harbMark == True:
        markTitle += 1
    harbJack = metric_json["Response"][4]['profileRecords']['data']['records']['2584970263']["objectives"][0][
        'complete']
    if harbJack == True:
        jackTitle += 1
    harbHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2584970263']["objectives"][0][
        'complete']
    if harbHunt == True:
        hunterTitle += 1
    harbCam = metric_json["Response"][6]['profileRecords']['data']['records']['2584970263']["objectives"][0]['complete']
    if harbCam == True:
        cameronTitle += 1
    harbKade = metric_json["Response"][7]['profileRecords']['data']['records']['2584970263']["objectives"][0][
        'complete']
    if harbKade == True:
        kadeTitle += 1
    harbNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2584970263']["objectives"][0][
        'complete']
    if harbNoz == True:
        nozTitle += 1
    # Enlightened
    enlightCon = metric_json["Response"][0]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightCon == True:
        connorTitle += 1
    enlightTom = metric_json["Response"][1]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightTom == True:
        thomasTitle += 1
    enlightDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightDoug == True:
        douglasTitle += 1
    enlightMark = metric_json["Response"][3]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightMark == True:
        markTitle += 1
    enlightJack = metric_json["Response"][4]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightJack == True:
        jackTitle += 1
    enlightHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightHunt == True:
        hunterTitle += 1
    enlightCam = metric_json["Response"][6]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightCam == True:
        cameronTitle += 1
    enlightKade = metric_json["Response"][7]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightKade == True:
        kadeTitle += 1
    enlightNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2909250963']["objectives"][0][
        'complete']
    if enlightNoz == True:
        nozTitle += 1
    # Cursebreaker
    curseCon = metric_json["Response"][0]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseCon == True:
        connorTitle += 1
    curseTom = metric_json["Response"][1]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseTom == True:
        thomasTitle += 1
    curseDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseDoug == True:
        douglasTitle += 1
    curseMark = metric_json["Response"][3]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseMark == True:
        markTitle += 1
    curseJack = metric_json["Response"][4]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseJack == True:
        jackTitle += 1
    curseHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseHunt == True:
        hunterTitle += 1
    curseCam = metric_json["Response"][6]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseCam == True:
        cameronTitle += 1
    curseKade = metric_json["Response"][7]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseKade == True:
        kadeTitle += 1
    curseNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3214425110']["objectives"][0][
        'complete']
    if curseNoz == True:
        nozTitle += 1
    # RivensBane
    rivenCon = metric_json["Response"][0]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenCon == True:
        connorTitle += 1
    rivenTom = metric_json["Response"][1]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenTom == True:
        thomasTitle += 1
    rivenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenDoug == True:
        douglasTitle += 1
    rivenMark = metric_json["Response"][3]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenMark == True:
        markTitle += 1
    rivenJack = metric_json["Response"][4]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenJack == True:
        jackTitle += 1
    rivenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenHunt == True:
        hunterTitle += 1
    rivenCam = metric_json["Response"][6]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenCam == True:
        cameronTitle += 1
    rivenKade = metric_json["Response"][7]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenKade == True:
        kadeTitle += 1
    rivenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1384029371']["objectives"][0][
        'complete']
    if rivenNoz == True:
        nozTitle += 1
    # Seraph
    seraphCon = metric_json["Response"][0]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphCon == True:
        connorTitle += 1
    seraphTom = metric_json["Response"][1]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphTom == True:
        thomasTitle += 1
    seraphDoug = metric_json["Response"][2]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphDoug == True:
        douglasTitle += 1
    seraphMark = metric_json["Response"][3]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphMark == True:
        markTitle += 1
    seraphJack = metric_json["Response"][4]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphJack == True:
        jackTitle += 1
    seraphHunt = metric_json["Response"][5]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphHunt == True:
        hunterTitle += 1
    seraphCam = metric_json["Response"][6]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphCam == True:
        cameronTitle += 1
    seraphKade = metric_json["Response"][7]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphKade == True:
        kadeTitle += 1
    seraphNoz = metric_json["Response"][8]['profileRecords']['data']['records']['4250626982']["objectives"][0][
        'complete']
    if seraphNoz == True:
        nozTitle += 1
    # Scallywag
    pirateCon = metric_json["Response"][0]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateCon == True:
        connorTitle += 1
    pirateTom = metric_json["Response"][1]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateTom == True:
        thomasTitle += 1
    pirateDoug = metric_json["Response"][2]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateDoug == True:
        douglasTitle += 1
    pirateMark = metric_json["Response"][3]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateMark == True:
        markTitle += 1
    pirateJack = metric_json["Response"][4]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateJack == True:
        jackTitle += 1
    pirateHunt = metric_json["Response"][5]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateHunt == True:
        hunterTitle += 1
    pirateCam = metric_json["Response"][6]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateCam == True:
        cameronTitle += 1
    pirateKade = metric_json["Response"][7]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateKade == True:
        kadeTitle += 1
    pirateNoz = metric_json["Response"][8]['profileRecords']['data']['records']['4176879201']["objectives"][0][
        'complete']
    if pirateNoz == True:
        nozTitle += 1
    # Reaper
    hauntCon = metric_json["Response"][0]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntCon == True:
        connorTitle += 1
    hauntTom = metric_json["Response"][1]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntTom == True:
        thomasTitle += 1
    hauntDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntDoug == True:
        douglasTitle += 1
    hauntMark = metric_json["Response"][3]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntMark == True:
        markTitle += 1
    hauntJack = metric_json["Response"][4]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntJack == True:
        jackTitle += 1
    hauntHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntHunt == True:
        hunterTitle += 1
    hauntCam = metric_json["Response"][6]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntCam == True:
        cameronTitle += 1
    hauntKade = metric_json["Response"][7]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntKade == True:
        kadeTitle += 1
    hauntNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3947410852']["objectives"][0][
        'complete']
    if hauntNoz == True:
        nozTitle += 1
    # Risen
    risenCon = metric_json["Response"][0]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenCon == True:
        connorTitle += 1
    risenTom = metric_json["Response"][1]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenTom == True:
        thomasTitle += 1
    risenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenDoug == True:
        douglasTitle += 1
    risenMark = metric_json["Response"][3]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenMark == True:
        markTitle += 1
    risenJack = metric_json["Response"][4]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenJack == True:
        jackTitle += 1
    risenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenHunt == True:
        hunterTitle += 1
    risenCam = metric_json["Response"][6]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenCam == True:
        cameronTitle += 1
    risenKade = metric_json["Response"][7]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenKade == True:
        kadeTitle += 1
    risenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1710217127']["objectives"][0][
        'complete']
    if risenNoz == True:
        nozTitle += 1
    # Realmwalker
    realmCon = metric_json["Response"][0]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmCon == True:
        connorTitle += 1
    realmTom = metric_json["Response"][1]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmTom == True:
        thomasTitle += 1
    realmDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmDoug == True:
        douglasTitle += 1
    realmMark = metric_json["Response"][3]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmMark == True:
        markTitle += 1
    realmJack = metric_json["Response"][4]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmJack == True:
        jackTitle += 1
    realmHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmHunt == True:
        hunterTitle += 1
    realmCam = metric_json["Response"][6]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmCam == True:
        cameronTitle += 1
    realmKade = metric_json["Response"][7]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmKade == True:
        kadeTitle += 1
    realmNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2991743002']["objectives"][0][
        'complete']
    if realmNoz == True:
        nozTitle += 1
    # Splicer
    spliceCon = metric_json["Response"][0]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceCon == True:
        connorTitle += 1
    spliceTom = metric_json["Response"][1]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceTom == True:
        thomasTitle += 1
    spliceDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceDoug == True:
        douglasTitle += 1
    spliceMark = metric_json["Response"][3]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceMark == True:
        markTitle += 1
    spliceJack = metric_json["Response"][4]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceJack == True:
        jackTitle += 1
    spliceHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceHunt == True:
        hunterTitle += 1
    spliceCam = metric_json["Response"][6]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceCam == True:
        cameronTitle += 1
    spliceKade = metric_json["Response"][7]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceKade == True:
        kadeTitle += 1
    spliceNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2796658869']["objectives"][0][
        'complete']
    if spliceNoz == True:
        nozTitle += 1
    # Chosen
    chosenCon = metric_json["Response"][0]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenCon == True:
        connorTitle += 1
    chosenTom = metric_json["Response"][1]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenTom == True:
        thomasTitle += 1
    chosenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenDoug == True:
        douglasTitle += 1
    chosenMark = metric_json["Response"][3]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenMark == True:
        markTitle += 1
    chosenJack = metric_json["Response"][4]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenJack == True:
        jackTitle += 1
    chosenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenHunt == True:
        hunterTitle += 1
    chosenCam = metric_json["Response"][6]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenCam == True:
        cameronTitle += 1
    chosenKade = metric_json["Response"][7]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenKade == True:
        kadeTitle += 1
    chosenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1087927672']["objectives"][0][
        'complete']
    if chosenNoz == True:
        nozTitle += 1
    # Warden
    wardenCon = metric_json["Response"][0]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenCon == True:
        connorTitle += 1
    wardenTom = metric_json["Response"][1]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenTom == True:
        thomasTitle += 1
    wardenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenDoug == True:
        douglasTitle += 1
    wardenMark = metric_json["Response"][3]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenMark == True:
        markTitle += 1
    wardenJack = metric_json["Response"][4]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenJack == True:
        jackTitle += 1
    wardenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenHunt == True:
        hunterTitle += 1
    wardenCam = metric_json["Response"][6]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenCam == True:
        cameronTitle += 1
    wardenKade = metric_json["Response"][7]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenKade == True:
        kadeTitle += 1
    wardenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1561715947']["objectives"][0][
        'complete']
    if wardenNoz == True:
        nozTitle += 1
    # Forerunner
    foreCon = metric_json["Response"][0]['profileRecords']['data']['records']['3169895614']["objectives"][0]['complete']
    if foreCon == True:
        connorTitle += 1
    foreTom = metric_json["Response"][1]['profileRecords']['data']['records']['3169895614']["objectives"][0]['complete']
    if foreTom == True:
        thomasTitle += 1
    foreDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3169895614']["objectives"][0][
        'complete']
    if foreDoug == True:
        douglasTitle += 1
    foreMark = metric_json["Response"][3]['profileRecords']['data']['records']['3169895614']["objectives"][0][
        'complete']
    if foreMark == True:
        markTitle += 1
    foreJack = metric_json["Response"][4]['profileRecords']['data']['records']['3169895614']["objectives"][0][
        'complete']
    if foreJack == True:
        jackTitle += 1
    foreHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3169895614']["objectives"][0][
        'complete']
    if foreHunt == True:
        hunterTitle += 1
    foreCam = metric_json["Response"][6]['profileRecords']['data']['records']['3169895614']["objectives"][0]['complete']
    if foreCam == True:
        cameronTitle += 1
    foreKade = metric_json["Response"][7]['profileRecords']['data']['records']['3169895614']["objectives"][0][
        'complete']
    if foreKade == True:
        kadeTitle += 1
    foreNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3169895614']["objectives"][0][
        'complete']
    if foreNoz == True:
        nozTitle += 1
    # Almighty
    worthCon = metric_json["Response"][0]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthCon == True:
        connorTitle += 1
    worthTom = metric_json["Response"][1]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthTom == True:
        thomasTitle += 1
    worthDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthDoug == True:
        douglasTitle += 1
    worthMark = metric_json["Response"][3]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthMark == True:
        markTitle += 1
    worthJack = metric_json["Response"][4]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthJack == True:
        jackTitle += 1
    worthHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthHunt == True:
        hunterTitle += 1
    worthCam = metric_json["Response"][6]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthCam == True:
        cameronTitle += 1
    worthKade = metric_json["Response"][7]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthKade == True:
        kadeTitle += 1
    worthNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2499679097']["objectives"][0][
        'complete']
    if worthNoz == True:
        nozTitle += 1
    # Savior
    saviorCon = metric_json["Response"][0]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorCon == True:
        connorTitle += 1
    saviorTom = metric_json["Response"][1]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorTom == True:
        thomasTitle += 1
    saviorDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorDoug == True:
        douglasTitle += 1
    saviorMark = metric_json["Response"][3]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorMark == True:
        markTitle += 1
    saviorJack = metric_json["Response"][4]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorJack == True:
        jackTitle += 1
    saviorHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorHunt == True:
        hunterTitle += 1
    saviorCam = metric_json["Response"][6]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorCam == True:
        cameronTitle += 1
    saviorKade = metric_json["Response"][7]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorKade == True:
        kadeTitle += 1
    saviorNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1185680627']["objectives"][0][
        'complete']
    if saviorNoz == True:
        nozTitle += 1
    # Undying
    undyingCon = metric_json["Response"][0]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingCon == True:
        connorTitle += 1
    undyingTom = metric_json["Response"][1]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingTom == True:
        thomasTitle += 1
    undyingDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingDoug == True:
        douglasTitle += 1
    undyingMark = metric_json["Response"][3]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingMark == True:
        markTitle += 1
    undyingJack = metric_json["Response"][4]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingJack == True:
        jackTitle += 1
    undyingHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingHunt == True:
        hunterTitle += 1
    undyingCam = metric_json["Response"][6]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingCam == True:
        cameronTitle += 1
    undyingKade = metric_json["Response"][7]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingKade == True:
        kadeTitle += 1
    undyingNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1866578144']["objectives"][0][
        'complete']
    if undyingNoz == True:
        nozTitle += 1
    # Reckoner
    reckonCon = metric_json["Response"][0]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonCon == True:
        connorTitle += 1
    reckonTom = metric_json["Response"][1]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonTom == True:
        thomasTitle += 1
    reckonDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonDoug == True:
        douglasTitle += 1
    reckonMark = metric_json["Response"][3]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonMark == True:
        markTitle += 1
    reckonJack = metric_json["Response"][4]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonJack == True:
        jackTitle += 1
    reckonHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonHunt == True:
        hunterTitle += 1
    reckonCam = metric_json["Response"][6]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonCam == True:
        cameronTitle += 1
    reckonKade = metric_json["Response"][7]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonKade == True:
        kadeTitle += 1
    reckonNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2472740040']["objectives"][0][
        'complete']
    if reckonNoz == True:
        nozTitle += 1
    # Shadow
    shadowCon = metric_json["Response"][0]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowCon == True:
        connorTitle += 1
    shadowTom = metric_json["Response"][1]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowTom == True:
        thomasTitle += 1
    shadowDoug = metric_json["Response"][2]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowDoug == True:
        douglasTitle += 1
    shadowMark = metric_json["Response"][3]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowMark == True:
        markTitle += 1
    shadowJack = metric_json["Response"][4]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowJack == True:
        jackTitle += 1
    shadowHunt = metric_json["Response"][5]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowHunt == True:
        hunterTitle += 1
    shadowCam = metric_json["Response"][6]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowCam == True:
        cameronTitle += 1
    shadowKade = metric_json["Response"][7]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowKade == True:
        kadeTitle += 1
    shadowNoz = metric_json["Response"][8]['profileRecords']['data']['records']['2056461735']["objectives"][0][
        'complete']
    if shadowNoz == True:
        nozTitle += 1
    # MMXIX
    mmxixCon = metric_json["Response"][0]['profileRecords']['data']['records']['966207508']["objectives"][0]['complete']
    if mmxixCon == True:
        connorTitle += 1
    mmxixTom = metric_json["Response"][1]['profileRecords']['data']['records']['966207508']["objectives"][0]['complete']
    if mmxixTom == True:
        thomasTitle += 1
    mmxixDoug = metric_json["Response"][2]['profileRecords']['data']['records']['966207508']["objectives"][0][
        'complete']
    if mmxixDoug == True:
        douglasTitle += 1
    mmxixMark = metric_json["Response"][3]['profileRecords']['data']['records']['966207508']["objectives"][0][
        'complete']
    if mmxixMark == True:
        markTitle += 1
    mmxixJack = metric_json["Response"][4]['profileRecords']['data']['records']['966207508']["objectives"][0][
        'complete']
    if mmxixJack == True:
        jackTitle += 1
    mmxixHunt = metric_json["Response"][5]['profileRecords']['data']['records']['966207508']["objectives"][0][
        'complete']
    if mmxixHunt == True:
        hunterTitle += 1
    mmxixCam = metric_json["Response"][6]['profileRecords']['data']['records']['966207508']["objectives"][0]['complete']
    if mmxixCam == True:
        cameronTitle += 1
    mmxixKade = metric_json["Response"][7]['profileRecords']['data']['records']['966207508']["objectives"][0][
        'complete']
    if mmxixKade == True:
        kadeTitle += 1
    mmxixNoz = metric_json["Response"][8]['profileRecords']['data']['records']['966207508']["objectives"][0][
        'complete']
    if mmxixNoz == True:
        nozTitle += 1
    # MMXX
    mmxxCon = metric_json["Response"][0]['profileRecords']['data']['records']['1109459264']["objectives"][0]['complete']
    if mmxxCon == True:
        connorTitle += 1
    mmxxTom = metric_json["Response"][1]['profileRecords']['data']['records']['1109459264']["objectives"][0]['complete']
    if mmxxTom == True:
        thomasTitle += 1
    mmxxDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1109459264']["objectives"][0][
        'complete']
    if mmxxDoug == True:
        douglasTitle += 1
    mmxxMark = metric_json["Response"][3]['profileRecords']['data']['records']['1109459264']["objectives"][0][
        'complete']
    if mmxxMark == True:
        markTitle += 1
    mmxxJack = metric_json["Response"][4]['profileRecords']['data']['records']['1109459264']["objectives"][0][
        'complete']
    if mmxxJack == True:
        jackTitle += 1
    mmxxHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1109459264']["objectives"][0][
        'complete']
    if mmxxHunt == True:
        hunterTitle += 1
    mmxxCam = metric_json["Response"][6]['profileRecords']['data']['records']['1109459264']["objectives"][0]['complete']
    if mmxxCam == True:
        cameronTitle += 1
    mmxxKade = metric_json["Response"][7]['profileRecords']['data']['records']['1109459264']["objectives"][0][
        'complete']
    if mmxxKade == True:
        kadeTitle += 1
    mmxxNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1109459264']["objectives"][0][
        'complete']
    if mmxxNoz == True:
        nozTitle += 1
    # MMXXI
    mmxxiCon = metric_json["Response"][0]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiCon == True:
        connorTitle += 1
    mmxxiTom = metric_json["Response"][1]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiTom == True:
        thomasTitle += 1
    mmxxiDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiDoug == True:
        douglasTitle += 1
    mmxxiMark = metric_json["Response"][3]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiMark == True:
        markTitle += 1
    mmxxiJack = metric_json["Response"][4]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiJack == True:
        jackTitle += 1
    mmxxiHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiHunt == True:
        hunterTitle += 1
    mmxxiCam = metric_json["Response"][6]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiCam == True:
        cameronTitle += 1
    mmxxiKade = metric_json["Response"][7]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiKade == True:
        kadeTitle += 1
    mmxxiNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1284946259']["objectives"][0][
        'complete']
    if mmxxiNoz == True:
        nozTitle += 1
    # MMXXII
    mmxxiiCon = metric_json["Response"][0]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiCon == True:
        connorTitle += 1
    mmxxiiTom = metric_json["Response"][1]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiTom == True:
        thomasTitle += 1
    mmxxiiDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiDoug == True:
        douglasTitle += 1
    mmxxiiMark = metric_json["Response"][3]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiMark == True:
        markTitle += 1
    mmxxiiJack = metric_json["Response"][4]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiJack == True:
        jackTitle += 1
    mmxxiiHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiHunt == True:
        hunterTitle += 1
    mmxxiiCam = metric_json["Response"][6]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiCam == True:
        cameronTitle += 1
    mmxxiiKade = metric_json["Response"][7]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiKade == True:
        kadeTitle += 1
    mmxxiiNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3249408038']["objectives"][0][
        'complete']
    if mmxxiiNoz == True:
        nozTitle += 1
    # Wayfarer
    wayfareCon = metric_json["Response"][0]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareCon == True:
        connorTitle += 1
    wayfareTom = metric_json["Response"][1]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareTom == True:
        thomasTitle += 1
    wayfareDoug = metric_json["Response"][2]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareDoug == True:
        douglasTitle += 1
    wayfareMark = metric_json["Response"][3]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareMark == True:
        markTitle += 1
    wayfareJack = metric_json["Response"][4]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareJack == True:
        jackTitle += 1
    wayfareHunt = metric_json["Response"][5]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareHunt == True:
        hunterTitle += 1
    wayfareCam = metric_json["Response"][6]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareCam == True:
        cameronTitle += 1
    wayfareKade = metric_json["Response"][7]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareKade == True:
        kadeTitle += 1
    wayfareNoz = metric_json["Response"][8]['profileRecords']['data']['records']['758645239']["objectives"][0][
        'complete']
    if wayfareNoz == True:
        nozTitle += 1
    # Unbroken
    unbrokenCon = metric_json["Response"][0]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenCon == True:
        connorTitle += 1
    unbrokenTom = metric_json["Response"][1]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenTom == True:
        thomasTitle += 1
    unbrokenDoug = metric_json["Response"][2]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenDoug == True:
        douglasTitle += 1
    unbrokenMark = metric_json["Response"][3]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenMark == True:
        markTitle += 1
    unbrokenJack = metric_json["Response"][4]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenJack == True:
        jackTitle += 1
    unbrokenHunt = metric_json["Response"][5]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenHunt == True:
        hunterTitle += 1
    unbrokenCam = metric_json["Response"][6]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenCam == True:
        cameronTitle += 1
    unbrokenKade = metric_json["Response"][7]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenKade == True:
        kadeTitle += 1
    unbrokenNoz = metric_json["Response"][8]['profileRecords']['data']['records']['1343839969']["objectives"][0][
        'complete']
    if unbrokenNoz == True:
        nozTitle += 1
    # Blacksmith
    smithCon = metric_json["Response"][0]['profileRecords']['data']['records']['317521250']["objectives"][0]['complete']
    if smithCon == True:
        connorTitle += 1
    smithTom = metric_json["Response"][1]['profileRecords']['data']['records']['317521250']["objectives"][0]['complete']
    if smithTom == True:
        thomasTitle += 1
    smithDoug = metric_json["Response"][2]['profileRecords']['data']['records']['317521250']["objectives"][0][
        'complete']
    if smithDoug == True:
        douglasTitle += 1
    smithMark = metric_json["Response"][3]['profileRecords']['data']['records']['317521250']["objectives"][0][
        'complete']
    if smithMark == True:
        markTitle += 1
    smithJack = metric_json["Response"][4]['profileRecords']['data']['records']['317521250']["objectives"][0][
        'complete']
    if smithJack == True:
        jackTitle += 1
    smithHunt = metric_json["Response"][5]['profileRecords']['data']['records']['317521250']["objectives"][0][
        'complete']
    if smithHunt == True:
        hunterTitle += 1
    smithCam = metric_json["Response"][6]['profileRecords']['data']['records']['317521250']["objectives"][0]['complete']
    if smithCam == True:
        cameronTitle += 1
    smithKade = metric_json["Response"][7]['profileRecords']['data']['records']['317521250']["objectives"][0][
        'complete']
    if smithKade == True:
        kadeTitle += 1
    smithNoz = metric_json["Response"][8]['profileRecords']['data']['records']['317521250']["objectives"][0][
        'complete']
    if smithNoz == True:
        nozTitle += 1
    # Chronicler
    loreCon = metric_json["Response"][0]['profileRecords']['data']['records']['3766199186']["objectives"][0]['complete']
    if loreCon == True:
        connorTitle += 1
    loreTom = metric_json["Response"][1]['profileRecords']['data']['records']['3766199186']["objectives"][0]['complete']
    if loreTom == True:
        thomasTitle += 1
    loreDoug = metric_json["Response"][2]['profileRecords']['data']['records']['3766199186']["objectives"][0][
        'complete']
    if loreDoug == True:
        douglasTitle += 1
    loreMark = metric_json["Response"][3]['profileRecords']['data']['records']['3766199186']["objectives"][0][
        'complete']
    if loreMark == True:
        markTitle += 1
    loreJack = metric_json["Response"][4]['profileRecords']['data']['records']['3766199186']["objectives"][0][
        'complete']
    if loreJack == True:
        jackTitle += 1
    loreHunt = metric_json["Response"][5]['profileRecords']['data']['records']['3766199186']["objectives"][0][
        'complete']
    if loreHunt == True:
        hunterTitle += 1
    loreCam = metric_json["Response"][6]['profileRecords']['data']['records']['3766199186']["objectives"][0]['complete']
    if loreCam == True:
        cameronTitle += 1
    loreKade = metric_json["Response"][7]['profileRecords']['data']['records']['3766199186']["objectives"][0][
        'complete']
    if loreKade == True:
        kadeTitle += 1
    loreNoz = metric_json["Response"][8]['profileRecords']['data']['records']['3766199186']["objectives"][0][
        'complete']
    if loreNoz == True:
        nozTitle += 1

    titleTable = PrettyTable()
    titleTable.field_names = ['Title', 'Connor', 'Thomas', 'Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron', 'Kade', 'Nozyric',
                              'Season Added']
    titleTable.add_rows(
        [
            ['Haruspex', harusCon, harusTom, harusDoug, harusMark, harusJack, harusHunt, harusCam, harusKade, harusNoz, ' Season 22 - Season of the Witch'],
            ['Swordbearer', swordCon, swordTom, swordDoug, swordMark, swordJack, swordHunt, swordCam, swordKade, swordNoz, ' Season 22 - Season of the Witch'],
            ['Aquanaut', aquanautCon, aquanautTom, aquanautDoug, aquanautMark, aquanautJack, aquanautHunt, aquanautCam,
             aquanautKade, aquanautNoz, 'Season 21 - Season of the Deep'],
            ['Queensguard', queensCon, queensTom, queensDoug, queensMark, queensJack, queensHunt, queensCam, queensKade, queensNoz,
             'Season 20 - Season of Defiance'],
            ['Virtual Fighter', virtFightCon, virtFightTom, virtFightDoug, virtFightMark, virtFightJack, virtFightHunt,
             virtFightCam, virtFightKade, virtFightNoz, 'Season 20 - Season of Defiance'],
            ['Dream Warrior', rootOfNightCon, rootOfNightTom, rootOfNightDoug, rootOfNightMark, rootOfNightJack,
             rootOfNightHunt, rootOfNightCam, rootOfNightKade, rootOfNightNoz, 'Season 20 - Season of Defiance'],
            ['Champ', champCon, champTom, champDoug, champMark, champJack, champHunt, champCam, champKade, champNoz,
             'Season 16 - Season of the Risen'],
            ['Star Baker', starBakerCon, starBakerTom, starBakerDoug, starBakerMark, starBakerJack, starBakerHunt,
             starBakerCam, starBakerKade, starBakerNoz, 'Season 19 - Season of the Seraph'],
            ['Ghoul', ghoulCon, ghoulTom, ghoulDoug, ghoulMark, ghoulJack, ghoulHunt, ghoulCam, ghoulKade, ghoulNoz,
             'Season 21 - Season of the Deep'],
            ['WANTED', wantedCon, wantedTom, wantedDoug, wantedMark, wantedJack, wantedHunt, wantedCam, wantedKade, wantedNoz,
             "Season 19 - Season of the Seraph"],
            ['Ghost Writer', ghostWriteCon, ghostWriteTom, ghostWriteDoug, ghostWriteMark, ghostWriteJack,
             ghostWriteHunt, ghostWriteCam, ghostWriteKade, ghostWriteNoz, "Season 18 - Season of Plunder"],
            ['Glorious', gloryCon, gloryTom, gloryDoug, gloryMark, gloryJack, gloryHunt, gloryCam, gloryKade, gloryNoz,
             'Season 19 - Season of the Seraph'],
            ['Kingslayer', kingsFallCon, kingsFallTom, kingsFallDoug, kingsFallMark, kingsFallJack, kingsFallHunt,
             kingsFallCam, kingsFallKade, kingsFallNoz, 'Season 18 - Season of Plunder'],
            ['Flamekeeper', flameCon, flameTom, flameDoug, flameMark, flameJack, flameHunt, flameCam, flameKade, flameNoz,
             'Season 17 - Season of the Haunted'],
            ['Reveler', revelCon, revelTom, revelDoug, revelMark, revelJack, revelHunt, revelCam, revelKade, revelNoz,
             'Season 19 - Season of the Seraph'],
            ['Discerpter', discCon, discTom, discDoug, discMark, discJack, discHunt, discCam, discKade, discNoz,
             'Season 17 - Season of the Haunted'],
            ['Iron Lord', ironLordCon, ironLordTom, ironLordDoug, ironLordMark, ironLordJack, ironLordHunt, ironLordCam,
             ironLordKade, ironLordNoz, 'Season 17 - Season of the Haunted'],
            ['Gumshoe', witchQueenCon, witchQueenTom, witchQueenDoug, witchQueenMark, witchQueenJack, witchQueenHunt,
             witchQueenCam, witchQueenKade, witchQueenNoz, 'Season 16 - Season of the Risen'],
            ['Disciple Slayer', vowDiscipleCon, vowDiscipleTom, vowDiscipleDoug, vowDiscipleMark, vowDiscipleJack,
             vowDiscipleHunt, vowDiscipleCam, vowDiscipleKade, vowDiscipleNoz, 'Season 16 - Season of the Risen'],
            ['Vidmaster', vidMasterCon, vidMasterTom, vidMasterDoug, vidMasterMark, vidMasterJack, vidMasterHunt,
             vidMasterCam, vidMasterKade, vidMasterNoz, 'Season 15 - Season of the Lost'],
            ['Deadeye', deadEyeCon, deadEyeTom, deadEyeDoug, deadEyeMark, deadEyeJack, deadEyeHunt, deadEyeCam,
             deadEyeKade, deadEyeNoz, 'Season 15 - Season of the Lost'],
            ['Flawless', trialsCon, trialsTom, trialsDoug, trialsMark, trialsJack, trialsHunt, trialsCam, trialsKade, trialsNoz,
             'Season 10 - Season of the Worthy'],
            ['Conqueror', conquerCon, conquerTom, conquerDoug, conquerMark, conquerJack, conquerHunt, conquerCam,
             conquerKade, conquerNoz, 'Forsaken'],
            ['Dredgen', dredgenCon, dredgenTom, dredgenDoug, dredgenMark, dredgenJack, dredgenHunt, dredgenCam,
             dredgenKade, dredgenNoz, 'Forsaken'],
            ['Splinted', splintCon, splintTom, splintDoug, splintMark, splintJack, splintHunt, splintCam, splintKade, splintNoz,
             'Season 12 - Season of the Hunt'],
            ['Fatebreaker', fateCon, fateTom, fateDoug, fateMark, fateJack, fateHunt, fateCam, fateKade, fateNoz,
             'Season 14 - Season of the Splicer'],
            ['Descendant', descCon, descTom, descDoug, descMark, descJack, descHunt, descCam, descKade, descNoz,
             'Season 12 - Season of the Hunt'],
            ['Harbinger', harbCon, harbTom, harbDoug, harbMark, harbJack, harbHunt, harbCam, harbKade, harbNoz,
             'Season 08 - Season of the Undying'],
            ['Enlightened', enlightCon, enlightTom, enlightDoug, enlightMark, enlightJack, enlightHunt, enlightCam,
             enlightKade, enlightNoz, 'Season 08 - Season of the Undying'],
            ['Cursebreaker', curseCon, curseTom, curseDoug, curseMark, curseJack, curseHunt, curseCam, curseKade, curseNoz,
             'Forsaken'],
            ['Rivensbane', rivenCon, rivenTom, rivenDoug, rivenMark, rivenJack, rivenHunt, rivenCam, rivenKade, rivenNoz,
             'Forsaken'],
            ['Seraph', seraphCon, seraphTom, seraphDoug, seraphMark, seraphJack, seraphHunt, seraphCam, seraphKade, seraphNoz,
             'Season 19 - Season of the Seraph'],
            ['Scallywag', pirateCon, pirateTom, pirateDoug, pirateMark, pirateJack, pirateHunt, pirateCam, pirateKade, pirateNoz,
             'Season 18 - Season of Plunder'],
            ['Reaper', hauntCon, hauntTom, hauntDoug, hauntMark, hauntJack, hauntHunt, hauntCam, hauntKade, hauntNoz,
             'Season 17 - Season of the Haunted'],
            ['Risen', risenCon, risenTom, risenDoug, risenMark, risenJack, risenHunt, risenCam, risenKade, risenNoz,
             'Season 16 - Season of the Risen'],
            ['Realmwalker', realmCon, realmTom, realmDoug, realmMark, realmJack, realmHunt, realmCam, realmKade, realmNoz,
             'Season 15 - Season of the Lost'],
            ['Splicer', spliceCon, spliceTom, spliceDoug, spliceMark, spliceJack, spliceHunt, spliceCam, spliceKade, spliceNoz,
             'Season 14 - Season of the Splicer'],
            ['Chosen', chosenCon, chosenTom, chosenDoug, chosenMark, chosenJack, chosenHunt, chosenCam, chosenKade, chosenNoz,
             'Season 13 - Season of the Chosen'],
            ['Warden', wardenCon, wardenTom, wardenDoug, wardenMark, wardenJack, wardenHunt, wardenCam, wardenKade, wardenNoz,
             'Season 12 - Season of the Hunt'],
            ['Forerunner', foreCon, foreTom, foreDoug, foreMark, foreJack, foreHunt, foreCam, foreKade, foreNoz,
             'Season 11 - Season of Arrivals'],
            ['Almighty', worthCon, worthTom, worthDoug, worthMark, worthJack, worthHunt, worthCam, worthKade, worthNoz,
             'Season 10 - Season of the Worthy'],
            ['Savior', saviorCon, saviorTom, saviorDoug, saviorMark, saviorJack, saviorHunt, saviorCam, saviorKade, saviorNoz,
             'Season 09 - Season of the Dawn'],
            ['Undying', undyingCon, undyingTom, undyingDoug, undyingMark, undyingJack, undyingHunt, undyingCam, undyingNoz,
             undyingKade, 'Season 08 - Season of the Undying'],
            ['Reckoner', reckonCon, reckonTom, reckonDoug, reckonMark, reckonJack, reckonHunt, reckonCam, reckonKade, reckonNoz,
             'Season 06 - Season of the Drifter'],
            ['Blacksmith', smithCon, smithTom, smithDoug, smithMark, smithJack, smithHunt, smithCam, smithKade, smithNoz,
             'Season 05 - Season of the Forge'],
            ['Shadow', shadowCon, shadowTom, shadowDoug, shadowMark, shadowJack, shadowHunt, shadowCam, shadowKade, shadowNoz,
             'Season 07 - Season of Opulence'],
            ['MMXIX', mmxixCon, mmxixTom, mmxixDoug, mmxixMark, mmxixJack, mmxixHunt, mmxixCam, mmxixKade, mmxixNoz,
             'Season 07 - Season of Opulence'],
            ['MMXX', mmxxCon, mmxxTom, mmxxDoug, mmxxMark, mmxxJack, mmxxHunt, mmxxCam, mmxxKade, mmxxNoz,
             'Season 11 - Season of Arrivals'],
            ['MMXXI', mmxxiCon, mmxxiTom, mmxxiDoug, mmxxiMark, mmxxiJack, mmxxiHunt, mmxxiCam, mmxxiKade, mmxxiNoz,
             'Season 15 - Season of the Lost'],
            ['MMXXII', mmxxiiCon, mmxxiiTom, mmxxiiDoug, mmxxiiMark, mmxxiiJack, mmxxiiHunt, mmxxiiCam, mmxxiiKade, mmxxiiNoz,
             'Season 19 - Season of the Seraph'],
            ['Wayfarer', wayfareCon, wayfareTom, wayfareDoug, wayfareMark, wayfareJack, wayfareHunt, wayfareCam,
             wayfareKade, wayfareNoz, 'Forsaken'],
            ['Unbroken', unbrokenCon, unbrokenTom, unbrokenDoug, unbrokenMark, unbrokenJack, unbrokenHunt, unbrokenCam,
             unbrokenKade, unbrokenNoz, 'Forsaken'],
            ['Chronicler', loreCon, loreTom, loreDoug, loreMark, loreJack, loreHunt, loreCam, loreKade, loreNoz, 'Forsaken'],
            ['All Titles', connorTitle, thomasTitle, douglasTitle, markTitle, jackTitle, hunterTitle, cameronTitle,
             kadeTitle, nozTitle, 'All Titles']
        ]
    )
    titleTable.reversesort = True
    print(titleTable.get_string(sortby='Season Added'))
