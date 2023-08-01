# Connor Downs
# Started: 7-31-2023
# Last Updated: 7-31-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks to three areas of interest, character data, triumph data, and metric data, then
# generates a way of viewing the data in an orderly manner.

import json
from prettytable import PrettyTable


def metricGenerator():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    profile_data_len = len(metric_json["Response"][0]['profileRecords']['data'])
    records_len = len(metric_json["Response"][0]['profileRecords']['data']['records'])
    metrics_data_len = len(metric_json["Response"][0]['metrics']['data']['metrics'])
    character_data_len = len(metric_json["Response"][0]['characters']['data'])


def profileData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    score = metric_json["Response"][0][0]["profileRecords"]['data']['score']
    activeScore = metric_json["Response"][0][0]["profileRecords"]['data']['activeScore']
    legacyScore = metric_json["Response"][0][0]["profileRecords"]['data']['legacyScore']
    lifetimeScore = metric_json["Response"][0][0]["profileRecords"]['data']['lifetimeScore']

    print(f'Triumph Score: {score}\nActive Triumph Score: {activeScore}\nLegacy Triumph Score: '
          f'{legacyScore}\nLifetime Triumph Score: {lifetimeScore}')


def recordsData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    # Aquanaut
    aquanaut = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3570567217']["objectives"][0]['complete']
    aquaProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3570567217']["objectives"][0]['progress']
    aquaCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3570567217']["objectives"][0]['completionValue']
    aquaPerc = (aquaProgress / aquaCompVal) * 100
    aquaPerc = round(aquaPerc, 3)
    # Queensguard
    queensguard = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1722592950']["objectives"][0]['complete']
    queenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1722592950']["objectives"][0]['progress']
    queenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1722592950']["objectives"][0]['completionValue']
    queenPerc = (queenProgress / queenCompVal) * 100
    queenPerc = round(queenPerc, 3)
    # Virtual Fighter
    virtFight = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3906538939']["objectives"][0]['complete']
    virtProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3906538939']["objectives"][0]['progress']
    virtCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3906538939']["objectives"][0]['completionValue']
    virtPerc = (virtProgress / virtCompVal) * 100
    virtPerc = round(virtPerc, 3)
    # Dream Warrior
    rootOfNight = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2889189256']["objectives"][0]['complete']
    rootProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2889189256']["objectives"][0]['progress']
    rootCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2889189256']["objectives"][0]['completionValue']
    rootPerc = (rootProgress / rootCompVal) * 100
    rootPerc = round(rootPerc, 3)
    # Champ
    champ = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3646306576']["objectives"][0]['complete']
    champProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3646306576']["objectives"][0]['progress']
    champCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3646306576']["objectives"][0]['completionValue']
    champPerc = (champProgress / champCompVal) * 100
    champPerc = round(champPerc, 3)
    # Star Baker
    starBaker = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2126152885']["objectives"][0]['complete']
    starProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2126152885']["objectives"][0]['progress']
    starCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2126152885']["objectives"][0]['completionValue']
    starPerc = (starProgress / starCompVal) * 100
    starPerc = round(starPerc, 3)
    # Ghoul
    ghoul = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3974717227']["objectives"][0]['complete']
    ghoulProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3974717227']["objectives"][0]['progress']
    ghoulCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3974717227']["objectives"][0]['completionValue']
    ghoulPerc = (ghoulProgress / ghoulCompVal) * 100
    ghoulPerc = round(ghoulPerc, 3)
    # WANTED
    wanted = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2302993504']["objectives"][0]['complete']
    wantedProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2302993504']["objectives"][0]['progress']
    wantedCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2302993504']["objectives"][0]['completionValue']
    wantedPerc = (wantedProgress / wantedCompVal) * 100
    wantedPerc = round(wantedPerc, 3)
    # Ghost Writer
    ghostWrite = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1089543274']["objectives"][0]['complete']
    ghostProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1089543274']["objectives"][0]['progress']
    ghostCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1089543274']["objectives"][0]['completionValue']
    ghostPerc = (ghostProgress / ghostCompVal) * 100
    ghostPerc = round(ghostPerc, 3)
    # Glorious
    glory = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['969142496']["objectives"][0]['complete']
    gloryProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['969142496']["objectives"][0]['progress']
    gloryCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['969142496']["objectives"][0]['completionValue']
    gloryPerc = (gloryProgress / gloryCompVal) * 100
    gloryPerc = round(gloryPerc, 3)
    # Kingslayer
    kingsFall = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3910736783']["objectives"][0]['complete']
    kingsProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3910736783']["objectives"][0]['progress']
    kingsCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3910736783']["objectives"][0]['completionValue']
    kingsPerc = (kingsProgress / kingsCompVal) * 100
    kingsPerc = round(kingsPerc, 3)
    # Flamekeeper
    flame = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3056675381']["objectives"][0]['complete']
    flameProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3056675381']["objectives"][0]['progress']
    flameCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3056675381']["objectives"][0]['completionValue']
    flamePerc = (flameProgress / flameCompVal) * 100
    flamePerc = round(flamePerc, 3)
    # Reveler
    revel = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1228693527']["objectives"][0]['complete']
    revelProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1228693527']["objectives"][0]['progress']
    revelCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1228693527']["objectives"][0]['completionValue']
    revelPerc = (revelProgress / revelCompVal) * 100
    revelPerc = round(revelPerc, 3)
    # Discerpter
    disc = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3097916612']["objectives"][0]['complete']
    discProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3097916612']["objectives"][0]['progress']
    discCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3097916612']["objectives"][0]['completionValue']
    discPerc = (discProgress / discCompVal) * 100
    discPerc = round(discPerc, 3)
    # Iron Lord
    ironLord = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1564001702']["objectives"][0]['complete']
    ironProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1564001702']["objectives"][0]['progress']
    ironCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1564001702']["objectives"][0]['completionValue']
    ironPerc = (ironProgress / ironCompVal) * 100
    ironPerc = round(ironPerc, 3)
    # Gumshoe
    witchQueen = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2489106733']["objectives"][0]['complete']
    witchProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2489106733']["objectives"][0]['progress']
    witchCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2489106733']["objectives"][0]['completionValue']
    witchPerc = (witchProgress / witchCompVal) * 100
    witchPerc = round(witchPerc, 3)
    # Disciple Slayer
    vowDisciple = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1971228746']["objectives"][0]['complete']
    vowProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1971228746']["objectives"][0]['progress']
    vowCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1971228746']["objectives"][0]['completionValue']
    vowPerc = (vowProgress / vowCompVal) * 100
    vowPerc = round(vowPerc, 3)
    # Vidmaster
    vidMaster = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3588818798']["objectives"][0]['complete']
    vidProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3588818798']["objectives"][0]['progress']
    vidCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3588818798']["objectives"][0]['completionValue']
    vidPerc = (vidProgress / vidCompVal) * 100
    vidPerc = round(vidPerc, 3)
    # Deadeye
    deadEye = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1438167672']["objectives"][0]['complete']
    deadProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1438167672']["objectives"][0]['progress']
    deadCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1438167672']["objectives"][0]['completionValue']
    deadPerc = (deadProgress / deadCompVal) * 100
    deadPerc = round(deadPerc, 3)
    # Flawless
    trials = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3298130972']["objectives"][0]['complete']
    trialsProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3298130972']["objectives"][0]['progress']
    trialsCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3298130972']["objectives"][0]['completionValue']
    trialsPerc = (trialsProgress / trialsCompVal) * 100
    trialsPerc = round(trialsPerc, 3)
    # Conqueror
    conquer = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3464275895']["objectives"][0]['complete']
    conquerProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3464275895']["objectives"][0]['progress']
    conquerCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3464275895']["objectives"][0]['completionValue']
    conquerPerc = (conquerProgress / conquerCompVal) * 100
    conquerPerc = round(conquerPerc, 3)
    # Dredgen
    dredgen = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1556658903']["objectives"][0]['complete']
    dredgenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1556658903']["objectives"][0]['progress']
    dredgenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1556658903']["objectives"][0]['completionValue']
    dredgenPerc = (dredgenProgress / dredgenCompVal) * 100
    dredgenPerc = round(dredgenPerc, 3)
    # Splintered
    splint = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2482004751']["objectives"][0]['complete']
    splintProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2482004751']["objectives"][0]['progress']
    splintCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2482004751']["objectives"][0]['completionValue']
    splintPerc = (splintProgress / splintCompVal) * 100
    splintPerc = round(splintPerc, 3)
    # Fatebreaker
    fate = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4141971983']["objectives"][0]['complete']
    fateProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4141971983']["objectives"][0]['progress']
    fateCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4141971983']["objectives"][0]['completionValue']
    fatePerc = (fateProgress / fateCompVal) * 100
    fatePerc = round(fatePerc, 3)
    # Descendant
    desc = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['540377256']["objectives"][0]['complete']
    descProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['540377256']["objectives"][0]['progress']
    descCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['540377256']["objectives"][0]['completionValue']
    descPerc = (descProgress / descCompVal) * 100
    descPerc = round(descPerc, 3)
    # Harbinger
    harb = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2584970263']["objectives"][0]['complete']
    harbProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2584970263']["objectives"][0]['progress']
    harbCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2584970263']["objectives"][0]['completionValue']
    harbPerc = (harbProgress / harbCompVal) * 100
    harbPerc = round(harbPerc, 3)
    # Enlightened
    enlight = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2909250963']["objectives"][0]['complete']
    enlightProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2909250963']["objectives"][0]['progress']
    enlightCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2909250963']["objectives"][0]['completionValue']
    enlightPerc = (enlightProgress / enlightCompVal) * 100
    enlightPerc = round(enlightPerc, 3)
    # Cursebreaker
    curse = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3214425110']["objectives"][0]['complete']
    curseProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3214425110']["objectives"][0]['progress']
    curseCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3214425110']["objectives"][0]['completionValue']
    cursePerc = (curseProgress / curseCompVal) * 100
    cursePerc = round(cursePerc, 3)
    # RivensBane
    riven = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1384029371']["objectives"][0]['complete']
    rivenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1384029371']["objectives"][0]['progress']
    rivenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1384029371']["objectives"][0]['completionValue']
    rivenPerc = (rivenProgress / rivenCompVal) * 100
    rivenPerc = round(rivenPerc, 3)
    # Seraph
    seraph = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4250626982']["objectives"][0]['complete']
    seraphProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4250626982']["objectives"][0]['progress']
    seraphCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4250626982']["objectives"][0]['completionValue']
    seraphPerc = (seraphProgress / seraphCompVal) * 100
    seraphPerc = round(seraphPerc, 3)
    # Scallywag
    pirate = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4176879201']["objectives"][0]['complete']
    pirateProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4176879201']["objectives"][0]['progress']
    pirateCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['4176879201']["objectives"][0]['completionValue']
    piratePerc = (pirateProgress / pirateCompVal) * 100
    piratePerc = round(piratePerc, 3)
    # Reaper
    haunt = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3947410852']["objectives"][0]['complete']
    hauntProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3947410852']["objectives"][0]['progress']
    hauntCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3947410852']["objectives"][0]['completionValue']
    hauntPerc = (hauntProgress / hauntCompVal) * 100
    hauntPerc = round(hauntPerc, 3)
    # Risen
    risen = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1710217127']["objectives"][0]['complete']
    risenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1710217127']["objectives"][0]['progress']
    risenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1710217127']["objectives"][0]['completionValue']
    risenPerc = (risenProgress / risenCompVal) * 100
    risenPerc = round(risenPerc, 3)
    # Realmwalker
    realm = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2991743002']["objectives"][0]['complete']
    realmProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2991743002']["objectives"][0]['progress']
    realmCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2991743002']["objectives"][0]['completionValue']
    realmPerc = (realmProgress / realmCompVal) * 100
    realmPerc = round(realmPerc, 3)
    # Splicer
    splice = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2796658869']["objectives"][0]['complete']
    spliceProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2796658869']["objectives"][0]['progress']
    spliceCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2796658869']["objectives"][0]['completionValue']
    splicePerc = (spliceProgress / spliceCompVal) * 100
    splicePerc = round(splicePerc, 3)
    # Chosen
    chosen = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1087927672']["objectives"][0]['complete']
    chosenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1087927672']["objectives"][0]['progress']
    chosenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1087927672']["objectives"][0]['completionValue']
    chosenPerc = (chosenProgress / chosenCompVal) * 100
    chosenPerc = round(chosenPerc, 3)
    # Warden
    warden = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1561715947']["objectives"][0]['complete']
    wardenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1561715947']["objectives"][0]['progress']
    wardenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1561715947']["objectives"][0]['completionValue']
    wardenPerc = (wardenProgress / wardenCompVal) * 100
    wardenPerc = round(wardenPerc, 3)
    # Forerunner
    fore = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3169895614']["objectives"][0]['complete']
    foreProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3169895614']["objectives"][0]['progress']
    foreCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3169895614']["objectives"][0]['completionValue']
    forePerc = (foreProgress / foreCompVal) * 100
    forePerc = round(forePerc, 3)
    # Almighty
    almight = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2499679097']["objectives"][0]['complete']
    almightProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2499679097']["objectives"][0]['progress']
    almightCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2499679097']["objectives"][0]['completionValue']
    almightPerc = (almightProgress / almightCompVal) * 100
    almightPerc = round(almightPerc, 3)
    # Savior
    savior = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1185680627']["objectives"][0]['complete']
    saviorProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1185680627']["objectives"][0]['progress']
    saviorCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1185680627']["objectives"][0]['completionValue']
    saviorPerc = (saviorProgress / saviorCompVal) * 100
    saviorPerc = round(saviorPerc, 3)
    # Undying
    undying = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1866578144']["objectives"][0]['complete']
    undyingProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1866578144']["objectives"][0]['progress']
    undyingCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1866578144']["objectives"][0]['completionValue']
    undyingPerc = (undyingProgress / undyingCompVal) * 100
    undyingPerc = round(undyingPerc, 3)
    # Reckoner
    reckon = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2472740040']["objectives"][0]['complete']
    reckonProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2472740040']["objectives"][0]['progress']
    reckonCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2472740040']["objectives"][0]['completionValue']
    reckonPerc = (reckonProgress / reckonCompVal) * 100
    reckonPerc = round(reckonPerc, 3)
    # Shadow
    shadow = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2056461735']["objectives"][0]['complete']
    shadowProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2056461735']["objectives"][0]['progress']
    shadowCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['2056461735']["objectives"][0]['completionValue']
    shadowPerc = (shadowProgress / shadowCompVal) * 100
    shadowPerc = round(shadowPerc, 3)
    # MMXIX
    mmxix = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['966207508']["objectives"][0]['complete']
    mmxixProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['966207508']["objectives"][0]['progress']
    mmxixCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['966207508']["objectives"][0]['completionValue']
    mmxixPerc = (mmxixProgress / mmxixCompVal) * 100
    mmxixPerc = round(mmxixPerc, 3)
    # MMXX
    mmxx = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1109459264']["objectives"][0]['complete']
    mmxxProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1109459264']["objectives"][0]['progress']
    mmxxCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1109459264']["objectives"][0]['completionValue']
    mmxxPerc = (mmxxProgress / mmxxCompVal) * 100
    mmxxPerc = round(mmxxPerc, 3)
    # MMXXI
    mmxxi = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1284946259']["objectives"][0]['complete']
    mmxxiProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1284946259']["objectives"][0]['progress']
    mmxxiCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1284946259']["objectives"][0]['completionValue']
    mmxxiPerc = (mmxxiProgress / mmxxiCompVal) * 100
    mmxxiPerc = round(mmxxiPerc, 3)
    # MMXXII
    mmxxii = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3249408038']["objectives"][0]['complete']
    mmxxiiProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3249408038']["objectives"][0]['progress']
    mmxxiiCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3249408038']["objectives"][0]['completionValue']
    mmxxiiPerc = (mmxxiiProgress / mmxxiiCompVal) * 100
    mmxxiiPerc = round(mmxxiiPerc, 3)
    # Wayfarer
    wayfare = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['758645239']["objectives"][0]['complete']
    wayfareProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['758645239']["objectives"][0]['progress']
    wayfareCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['758645239']["objectives"][0]['completionValue']
    wayfarePerc = (wayfareProgress / wayfareCompVal) * 100
    wayfarePerc = round(wayfarePerc, 3)
    # Unbroken
    unbroken = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1343839969']["objectives"][0]['complete']
    unbrokenProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1343839969']["objectives"][0]['progress']
    unbrokenCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['1343839969']["objectives"][0]['completionValue']
    unbrokenPerc = (unbrokenProgress / unbrokenCompVal) * 100
    unbrokenPerc = round(unbrokenPerc, 3)
    # Blacksmith
    smith = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['317521250']["objectives"][0]['complete']
    smithProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['317521250']["objectives"][0]['progress']
    smithCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['317521250']["objectives"][0]['completionValue']
    smithPerc = (smithProgress / smithCompVal) * 100
    smithPerc = round(smithPerc, 3)
    # Chronicler
    chronicle = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3766199186']["objectives"][0]['complete']
    chronicleProgress = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3766199186']["objectives"][0]['progress']
    chronicleCompVal = metric_json["Response"][0][0][0]['profileRecords']['data']['records']['3766199186']["objectives"][0]['completionValue']
    chroniclePerc = (chronicleProgress / chronicleCompVal) * 100
    chroniclePerc = round(chroniclePerc, 3)

    titleTable = PrettyTable()
    titleTable.field_names = ['Title', 'Source', 'Completion Status', 'Completion Progress', 'Necessary to Complete',
                              'Percent Complete', 'Season Added']
    titleTable.add_rows(
        [
            ['Aquanaut', 'Season of the Deep', aquanaut, aquaProgress, aquaCompVal, aquaPerc,'Season 21 - Season of the Deep'],
            ['Queensguard', 'Season of Defiance', queensguard, queenProgress, queenCompVal, queenPerc,'Season 20 - Season of Defiance'],
            ['Virtual Fighter', 'Lightfall', virtFight, virtProgress, virtCompVal, virtPerc,'Season 20 - Season of Defiance'],
            ['Dream Warrior', 'Root of Nightmare', rootOfNight, rootProgress, rootCompVal, rootPerc,'Season 20 - Season of Defiance'],
            ['Champ', 'Guardian Games', champ, champProgress, champCompVal, champPerc,'Season 16 - Season of the Risen'],
            ['Star Baker', 'The Dawning', starBaker, starProgress, starCompVal, starPerc,'Season 19 - Season of the Seraph'],
            ['Ghoul', 'Ghosts of the Deep', ghoul, ghoulProgress, ghoulCompVal, ghoulPerc,'Season 21 - Season of the Deep'],
            ['WANTED', 'Spire of the Watcher', wanted, wantedProgress, wantedCompVal, wantedPerc,"Season 19 - Season of the Seraph"],
            ['Ghost Writer', 'Festival of the Lost', ghostWrite, ghostProgress, ghostCompVal, ghostPerc,"Season 18 - Season of Plunder"],
            ['Glorious', 'Crucible', glory, gloryProgress, gloryCompVal, gloryPerc, 'Season 19 - Season of the Seraph'],
            ['Kingslayer', "King's Fall", kingsFall, kingsProgress, kingsCompVal, kingsPerc,'Season 18 - Season of Plunder'],
            ['Flamekeeper', 'Solstice of Heroes', flame, flameProgress, flameCompVal, flamePerc, 'Season 17 - Season of the Haunted'],
            ['Reveler', 'Seasonal Event', revel, revelProgress, revelCompVal, revelPerc, 'Season 19 - Season of the Seraph'],
            ['Discerpter', 'Duality', disc, discProgress, discCompVal, discPerc, 'Season 17 - Season of the Haunted'],
            ['Iron Lord', 'Iron Banner', ironLord, ironProgress, ironCompVal, ironPerc, 'Season 17 - Season of the Haunted'],
            ['Gumshoe', 'Witch Queen', witchQueen, witchProgress, witchCompVal, witchPerc, 'Season 16 - Season of the Risen'],
            ['Disciple Slayer', 'Vow of the Disciple', vowDisciple, vowProgress, vowCompVal, vowPerc, 'Season 16 - Season of the Risen'],
            ['Vidmaster', '30th Anniversary', vidMaster, vidProgress, vidCompVal, vidPerc, 'Season 15 - Season of the Lost'],
            ['Deadeye', 'Weapons', deadEye, deadProgress, deadCompVal, deadPerc, 'Season 15 - Season of the Lost'],
            ['Flawless', 'Trials of Osiris', trials, trialsProgress, trialsCompVal, trialsPerc, 'Season 10 - Season of the Worthy'],
            ['Conqueror', 'Grandmaster Nightfalls', conquer, conquerProgress, conquerCompVal, conquerPerc, 'Forsaken'],
            ['Dredgen', 'Gambit', dredgen, dredgenProgress, dredgenCompVal, dredgenPerc, 'Forsaken'],
            ['Splinted', 'Beyond Light', splint, splintProgress, splintCompVal,splintPerc, 'Season 12 - Season of the Hunt'],
            ['Fatebreaker', 'Vault of Glass', fate, fateProgress,fateCompVal,fatePerc, 'Season 14 - Season of the Splicer'],
            ['Descendant', 'Deep Stone Crypt', desc, descProgress, descCompVal, descPerc, 'Season 12 - Season of the Hunt'],
            ['Harbinger', 'Shadowkeep', harb, harbProgress, harbCompVal, harbPerc, 'Season 08 - Season of the Undying'],
            ['Enlightened', 'Garden of Salvation', enlight, enlightProgress, enlightCompVal, enlightPerc, 'Season 08 - Season of the Undying'],
            ['Cursebreaker', 'The Dreaming City', curse, curseProgress, curseCompVal, cursePerc, 'Forsaken'],
            ['Rivensbane', 'Last Wish', riven, rivenProgress, rivenCompVal, rivenPerc, 'Forsaken'],
            ['Seraph', ' Season of the Seraph', seraph, seraphProgress, seraphCompVal, seraphPerc, 'Season 19 - Season of the Seraph'],
            ['Scallywag', 'Season of Plunder', pirate, pirateProgress, pirateCompVal, piratePerc, 'Season 18 - Season of Plunder'],
            ['Reaper', 'Season of the Haunted', haunt, hauntProgress, hauntCompVal, hauntPerc, 'Season 17 - Season of the Haunted'],
            ['Risen', 'Season of the Risen', risen, risenProgress, risenCompVal, risenPerc, 'Season 16 - Season of the Risen'],
            ['Realmwalker', 'Season of the Lost', realm, realmProgress, realmCompVal, realmPerc, 'Season 15 - Season of the Lost'],
            ['Splicer', 'Season of the Splicer', splice, spliceProgress, spliceCompVal, splicePerc, 'Season 14 - Season of the Splicer'],
            ['Chosen', 'Season of the Chosen', chosen, chosenProgress, chosenCompVal, chosenPerc, 'Season 13 - Season of the Chosen'],
            ['Warden', 'Season of the Hunt', warden, wardenProgress, wardenCompVal, wardenPerc, 'Season 12 - Season of the Hunt'],
            ['Forerunner', 'Season of Arrivals', fore, foreProgress, foreCompVal, forePerc, 'Season 11 - Season of Arrivals'],
            ['Almighty', 'Season of the Almghty', almight, almightProgress, almightCompVal, almightPerc, 'Season 10 - Season of the Almighty'],
            ['Savior', 'Season of the Dawn', savior, saviorProgress, saviorCompVal, saviorPerc, 'Season 09 - Season of the Dawn'],
            ['Undying', 'Season of the Undying', undying, undyingProgress, undyingCompVal, undyingPerc, 'Season 08 - Season of the Undying'],
            ['Reckoner', "Joker's Wild", reckon, reckonProgress, reckonCompVal, reckonPerc, 'Season 06 - Season of the Drifter'],
            ['Blacksmith', 'Season of the Forge', smith, smithProgress, smithCompVal, smithPerc, 'Season 05 - Season of the Forge'],
            ['Shadow', 'Season of Opulence', shadow, shadowProgress, shadowCompVal, shadowPerc, 'Season 07 - Season of Opulence'],
            ['MMXIX', 'Season of Opulence', mmxix, mmxixProgress, mmxixCompVal, mmxixPerc, 'Season 07 - Season of Opulence'],
            ['MMXX', 'Season of Arrivals', mmxx, mmxxProgress, mmxxCompVal, mmxxPerc, 'Season 11 - Season of Arrivals'],
            ['MMXXI', 'Season of the Lost', mmxxi, mmxxiProgress, mmxxiCompVal, mmxxiPerc, 'Season 15 - Season of the Lost'],
            ['MMXXII', 'Season of the Seraph', mmxxii, mmxxiiProgress, mmxxiiCompVal, mmxxiiPerc, 'Season 19 - Season of the Seraph'],
            ['Wayfarer', 'Destinations', wayfare, wayfareProgress, wayfareCompVal, wayfarePerc, 'Forsaken'],
            ['Unbroken', 'Crucible', unbroken, unbrokenProgress, unbrokenCompVal, unbrokenPerc, 'Forsaken'],
            ['Chronicler', 'Lore', chronicle, chronicleProgress, chronicleCompVal, chroniclePerc, 'Forsaken']
        ]
    )
    titleTable.reversesort = True
    print(titleTable.get_string(sortby='Season Added'))


def metricsData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    # Seasonal Metrics
    fishCaught = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
        'progress']
    heavyFishCaught = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2691615711']["objectiveProgress"][
        'progress']
    heavyFishCaught = heavyFishCaught / 100
    goodBoyProtocol = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3131994725']["objectiveProgress"][
        'progress']
    print("Seasonal Metrics")
    print(f"Total number of times positive reinforcement was given to the best boy: {goodBoyProtocol}")
    print(f"The total number of fish caught: {fishCaught}")
    print(f"The weight of the heaviest fish caught: {heavyFishCaught}kg")

    # Account Metrics
    ageOfLoss = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1572939289']["objectiveProgress"][
        'progress']
    collectScore = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3526455111']["objectiveProgress"][
        'progress']

    # Element Final Blows
    totalFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2537844000']["objectiveProgress"][
        'progress']
    arcFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1513312460']["objectiveProgress"][
        'progress']
    voidFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2327589890']["objectiveProgress"][
        'progress']
    solarFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2187143539']["objectiveProgress"][
        'progress']
    stasisFinalBLows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
    strandFinalBLows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

    # Weapon Type Final Blows (all data before Beyond Light has been removed from the API)
    # Primary Weapons
    autoFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2094013181']["objectiveProgress"][
        'progress']
    pulseFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['982406257']["objectiveProgress"][
        'progress']
    scoutFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2599646044']["objectiveProgress"][
        'progress']
    handFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2117204340']["objectiveProgress"][
        'progress']
    sidearmFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
    submachineFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
    bowFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3522276357']["objectiveProgress"][
        'progress']

    # Special Weapons
    traceFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3124958797']["objectiveProgress"][
        'progress']
    fusionFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['105734892']["objectiveProgress"][
        'progress']
    shotgunFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
    sniperFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['633604541']["objectiveProgress"][
        'progress']

    # Heavy Weapons
    grenadeLaunchFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
    rocketFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
    swordFinalBlows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1619269474']["objectiveProgress"][
        'progress']
    linearFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
    machineGunFinalBlows = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

    primaryTable = PrettyTable()
    primaryTable.field_names = ['Weapon Types', 'Kills']
    primaryTable.add_rows(
        [
            ['Auto Rifles', autoFinalBlows],
            ['Pulse Rifles', pulseFinalBlows],
            ['Scout Rifle', scoutFinalBlows],
            ['Hand Cannon', handFinalBlows],
            ['Sidearm', sidearmFinalBlows],
            ['Submachine Gun', submachineFinalBlows],
            ['Combat Bow', bowFinalBlows]
        ]
    )
    specialTable = PrettyTable()
    specialTable.field_names = ['Weapon Types', 'Kills']
    specialTable.add_rows(
        [
            ['Trace Rifles', traceFinalBlows],
            ['Fusion Rifles', fusionFinalBlows],
            ['Sniper Rifle', sniperFinalBlows],
            ['Shotgun', shotgunFinalBlows],

        ]
    )
    heavyTable = PrettyTable()
    heavyTable.field_names = ['Weapon Types', 'Kills']
    heavyTable.add_rows(
        [
            ['Grenade Launcher', grenadeLaunchFinalBlows],
            ['Linear Fusion Rifles', linearFinalBlows],
            ['Rocket Launcher', rocketFinalBlows],
            ['Sword', swordFinalBlows],
            ['Machine Gun', machineGunFinalBlows]

        ]
    )

    print("Account Metrics")
    print(f"Age of Loss Triumph Score: {ageOfLoss}")
    print(f"Collection Score: {collectScore}")
    print(f"Number of Total Final Blows: {totalFinalBlows}")
    primaryTable.reversesort = True
    specialTable.reversesort = True
    heavyTable.reversesort = True
    print(primaryTable.get_string(sortby='Kills'))
    print(specialTable.get_string(sortby='Kills'))
    print(heavyTable.get_string(sortby='Kills'))
    print(f"Number of Final Blows per element\nArc: {arcFinalBlows}, Void: {voidFinalBlows}, Solar: {solarFinalBlows}, "
          f"Stasis: {stasisFinalBLows}, Strand: {strandFinalBLows}")

    # Strike/Nightfall Metrics
    # General Values
    strikeComplete = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['793155718']["objectiveProgress"][
        'progress']
    flawlessStrike = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2326329668']["objectiveProgress"][
        'progress']
    champsDefeated = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['41075005']["objectiveProgress"][
        'progress']
    finalBlowsPerS = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3857340681']["objectiveProgress"][
        'progress']
    # Nightfall Highest Scores
    armsDealer = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3036740778']["objectiveProgress"][
        'progress']
    insightTerm = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3146366866']["objectiveProgress"][
        'progress']
    invertedSpire = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3466351705']["objectiveProgress"][
        'progress']
    savaSong = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2894079898']["objectiveProgress"][
        'progress']
    pyramidion = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2457392818']["objectiveProgress"][
        'progress']
    exodusCrash = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1118387860']["objectiveProgress"][
        'progress']
    gardenWorld = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3543375894']["objectiveProgress"][
        'progress']
    treeOfPossibility = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
    strangeTerrain = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['40546883']["objectiveProgress"][
        'progress']
    wardenOfNothing = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['4140273235']["objectiveProgress"][
        'progress']
    broodhold = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['356508148']["objectiveProgress"][
        'progress']
    scarletKeep = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1666283222']["objectiveProgress"][
        'progress']
    lakeOfShadows = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3139878529']["objectiveProgress"][
        'progress']
    theCorrupted = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2920064672']["objectiveProgress"][
        'progress']
    festeringCore = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['326550718']["objectiveProgress"][
        'progress']
    theDisgraced = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['136014172']["objectiveProgress"][
        'progress']
    theGlassway = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2883115929']["objectiveProgress"][
        'progress']
    provingGrounds = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3209483141']["objectiveProgress"][
        'progress']
    devilsLair = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['103014972']["objectiveProgress"][
        'progress']
    fallenSABER = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['2894593528']["objectiveProgress"][
        'progress']
    hollowedLair = metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['449969041']["objectiveProgress"][
        'progress']
    theLightblade = \
    metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['3181525833']["objectiveProgress"][
        'progress']
    birthplaceOTVile = \
        metric_json["Response"][0][0][0][0]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

    strikeTable = PrettyTable()
    strikeTable.field_names = ['Nightfall', 'Highest Nightfall Score']
    strikeTable.add_rows(
        [
            ['Arms Dealer', armsDealer],
            ['Insight Terminus', insightTerm],
            ['The Inverted Spire', invertedSpire],
            ["Savathûn's Song", savaSong],
            ['The Pyramidion', pyramidion],
            ['Exodus Crash', exodusCrash],
            ['A Garden World', gardenWorld],
            ['Tree of Possibilities', treeOfPossibility],
            ['Strange Terrain', strangeTerrain],
            ['Warden of Nothing', wardenOfNothing],
            ['Broodhold', broodhold],
            ['The Scarlet Keep', scarletKeep],
            ['Lake of Shadows', lakeOfShadows],
            ['The Corrupted', theCorrupted],
            ['The Festering Core', festeringCore],
            ['The Disgraced', theDisgraced],
            ['The Glassway', theGlassway],
            ['Proving Grounds', provingGrounds],
            ["The Devil's Lair", devilsLair],
            ['Fallen S.A.B.E.R.', fallenSABER],
            ['The Hollowed Lair', hollowedLair],
            ['The Lightblade', theLightblade],
            ['Birthplace of the Vile', birthplaceOTVile]
        ]
    )
    print(f'Total number of Strike/Nightfall Completions: {strikeComplete}')
    print(f'Total number of flawless Strike/Nightfall Completions: {flawlessStrike}')
    print(f'Total number of Champions Defeated: {champsDefeated}')
    print(f'Final Blows per Strike/Nightfall in the current season: {finalBlowsPerS}')
    strikeTable.reversesort = True
    print(strikeTable.get_string(sortby="Highest Nightfall Score"))


def characterData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    character_data = metric_json["Response"][0]['characters']['data']

    print(character_data)
