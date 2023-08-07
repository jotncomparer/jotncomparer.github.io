# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-7-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at metric data that can be found on the player emblem screen in game.

import json
from prettytable import PrettyTable

def metricsData():
    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    # Seasonal Metrics
    fishCaught = metric_json["Response"][0]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
        'progress']
    heavyFishCaught = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2691615711']["objectiveProgress"][
        'progress']
    heavyFishCaught = heavyFishCaught / 100
    goodBoyProtocol = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3131994725']["objectiveProgress"][
        'progress']
    print("Seasonal Metrics")
    print(f"Total number of times positive reinforcement was given to the best boy: {goodBoyProtocol}")
    print(f"The total number of fish caught: {fishCaught}")
    print(f"The weight of the heaviest fish caught: {heavyFishCaught}kg")

    # Account Metrics
    ageOfLoss = metric_json["Response"][0]['metrics']['data']['metrics']['1572939289']["objectiveProgress"][
        'progress']
    collectScore = metric_json["Response"][0]['metrics']['data']['metrics']['3526455111']["objectiveProgress"][
        'progress']

    # Element Final Blows
    totalFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2537844000']["objectiveProgress"][
        'progress']
    arcFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['1513312460']["objectiveProgress"][
        'progress']
    voidFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2327589890']["objectiveProgress"][
        'progress']
    solarFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2187143539']["objectiveProgress"][
        'progress']
    stasisFinalBLows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
    strandFinalBLows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

    # Weapon Type Final Blows (all data before Beyond Light has been removed from the API)
    # Primary Weapons
    autoFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2094013181']["objectiveProgress"][
        'progress']
    pulseFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['982406257']["objectiveProgress"][
        'progress']
    scoutFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2599646044']["objectiveProgress"][
        'progress']
    handFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2117204340']["objectiveProgress"][
        'progress']
    sidearmFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
    submachineFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
    bowFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3522276357']["objectiveProgress"][
        'progress']

    # Special Weapons
    traceFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3124958797']["objectiveProgress"][
        'progress']
    fusionFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['105734892']["objectiveProgress"][
        'progress']
    shotgunFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
    sniperFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['633604541']["objectiveProgress"][
        'progress']
    # The API does not distinguish between special weapon grenade launchers and heavy grenade launchers. It is to be assumed it means special grenade launchers
    grenadeLaunchFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
    # Heavy Weapons

    rocketFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
    swordFinalBlows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['1619269474']["objectiveProgress"][
        'progress']
    linearFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
    machineGunFinalBlows = \
        metric_json["Response"][0]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

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
            ['Grenade Launcher', grenadeLaunchFinalBlows]
        ]
    )
    heavyTable = PrettyTable()
    heavyTable.field_names = ['Weapon Types', 'Kills']
    heavyTable.add_rows(
        [
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
    metric_json["Response"][0]['metrics']['data']['metrics']['793155718']["objectiveProgress"][
        'progress']
    flawlessStrike = \
    metric_json["Response"][0]['metrics']['data']['metrics']['2326329668']["objectiveProgress"][
        'progress']
    champsDefeated = metric_json["Response"][0]['metrics']['data']['metrics']['41075005']["objectiveProgress"][
        'progress']
    finalBlowsPerS = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3857340681']["objectiveProgress"][
        'progress']
    # Nightfall Highest Scores
    armsDealer = metric_json["Response"][0]['metrics']['data']['metrics']['3036740778']["objectiveProgress"][
        'progress']
    insightTerm = metric_json["Response"][0]['metrics']['data']['metrics']['3146366866']["objectiveProgress"][
        'progress']
    invertedSpire = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3466351705']["objectiveProgress"][
        'progress']
    savaSong = metric_json["Response"][0]['metrics']['data']['metrics']['2894079898']["objectiveProgress"][
        'progress']
    pyramidion = metric_json["Response"][0]['metrics']['data']['metrics']['2457392818']["objectiveProgress"][
        'progress']
    exodusCrash = metric_json["Response"][0]['metrics']['data']['metrics']['1118387860']["objectiveProgress"][
        'progress']
    gardenWorld = metric_json["Response"][0]['metrics']['data']['metrics']['3543375894']["objectiveProgress"][
        'progress']
    treeOfPossibility = \
        metric_json["Response"][0]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
    strangeTerrain = metric_json["Response"][0]['metrics']['data']['metrics']['40546883']["objectiveProgress"][
        'progress']
    wardenOfNothing = \
    metric_json["Response"][0]['metrics']['data']['metrics']['4140273235']["objectiveProgress"][
        'progress']
    broodhold = metric_json["Response"][0]['metrics']['data']['metrics']['356508148']["objectiveProgress"][
        'progress']
    scarletKeep = metric_json["Response"][0]['metrics']['data']['metrics']['1666283222']["objectiveProgress"][
        'progress']
    lakeOfShadows = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3139878529']["objectiveProgress"][
        'progress']
    theCorrupted = metric_json["Response"][0]['metrics']['data']['metrics']['2920064672']["objectiveProgress"][
        'progress']
    festeringCore = metric_json["Response"][0]['metrics']['data']['metrics']['326550718']["objectiveProgress"][
        'progress']
    theDisgraced = metric_json["Response"][0]['metrics']['data']['metrics']['136014172']["objectiveProgress"][
        'progress']
    theGlassway = metric_json["Response"][0]['metrics']['data']['metrics']['2883115929']["objectiveProgress"][
        'progress']
    provingGrounds = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3209483141']["objectiveProgress"][
        'progress']
    devilsLair = metric_json["Response"][0]['metrics']['data']['metrics']['103014972']["objectiveProgress"][
        'progress']
    fallenSABER = metric_json["Response"][0]['metrics']['data']['metrics']['2894593528']["objectiveProgress"][
        'progress']
    hollowedLair = metric_json["Response"][0]['metrics']['data']['metrics']['449969041']["objectiveProgress"][
        'progress']
    theLightblade = \
    metric_json["Response"][0]['metrics']['data']['metrics']['3181525833']["objectiveProgress"][
        'progress']
    birthplaceOTVile = \
        metric_json["Response"][0]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

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