# Connor Downs
# Started: 8-8-2023
# Last Updated: 8-8-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at emblem metric data for all players.

import json
from prettytable import PrettyTable


def allMetricsData():
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

    def seasonalMetrics():
        fishCaughtCon = metric_json["Response"][0]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtCon = \
            metric_json["Response"][0]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtCon = heavyFishCaughtCon / 100
        goodBoyProtocolCon = \
            metric_json["Response"][0]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtTom = metric_json["Response"][1]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtTom = \
            metric_json["Response"][1]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtTom = heavyFishCaughtTom / 100
        goodBoyProtocolTom = \
            metric_json["Response"][1]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtDoug = metric_json["Response"][2]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtDoug = \
            metric_json["Response"][2]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtDoug = heavyFishCaughtDoug / 100
        goodBoyProtocolDoug = \
            metric_json["Response"][2]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtMark = metric_json["Response"][3]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtMark = \
            metric_json["Response"][3]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtMark = heavyFishCaughtMark / 100
        goodBoyProtocolMark = \
            metric_json["Response"][3]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtJack = metric_json["Response"][4]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtJack = \
            metric_json["Response"][4]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtJack = heavyFishCaughtJack / 100
        goodBoyProtocolJack = \
            metric_json["Response"][4]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtHunt = metric_json["Response"][5]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtHunt = \
            metric_json["Response"][5]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtHunt = heavyFishCaughtHunt / 100
        goodBoyProtocolHunt = \
            metric_json["Response"][5]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtCam = metric_json["Response"][6]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtCam = \
            metric_json["Response"][6]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtCam = heavyFishCaughtCam / 100
        goodBoyProtocolCam = \
            metric_json["Response"][6]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        fishCaughtKade = metric_json["Response"][7]['metrics']['data']['metrics']['24768693']["objectiveProgress"][
            'progress']
        heavyFishCaughtKade = \
            metric_json["Response"][7]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress']
        heavyFishCaughtKade = heavyFishCaughtKade / 100
        goodBoyProtocolKade = \
            metric_json["Response"][7]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']

        seasonalTable = PrettyTable()
        seasonalTable.field_names = ['Player', 'Fish Caught', 'Heaviest Fish', 'Good Boy Protocol']
        seasonalTable.add_rows(
            [
                ['Connor', fishCaughtCon, f'{heavyFishCaughtCon}kg', goodBoyProtocolCon],
                ['Thomas', fishCaughtTom, f'{heavyFishCaughtTom}kg', goodBoyProtocolTom],
                ['Douglas', fishCaughtDoug, f'{heavyFishCaughtDoug}kg', goodBoyProtocolDoug],
                ['Mark', fishCaughtMark, f'{heavyFishCaughtMark}kg', goodBoyProtocolMark],
                ['Jack', fishCaughtJack, f'{heavyFishCaughtJack}kg', goodBoyProtocolJack],
                ['Hunter', fishCaughtHunt, f'{heavyFishCaughtHunt}kg', goodBoyProtocolHunt],
                ['Cameron', fishCaughtCam, f'{heavyFishCaughtCam}kg', goodBoyProtocolCam],
                ['Kade', fishCaughtKade, f'{heavyFishCaughtKade}kg', goodBoyProtocolKade]
            ]
        )
        print(seasonalTable)

    def accountMetrics():
        def elementFinalBlows():
            sumTotal = 0
            sumArc = 0
            sumVoid = 0
            sumSolar = 0
            sumStatis = 0
            sumStrand = 0

            totalFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            totalFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2537844000']["objectiveProgress"]['progress']
            arcFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['1513312460']["objectiveProgress"]['progress']
            voidFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2327589890']["objectiveProgress"]['progress']
            solarFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2187143539']["objectiveProgress"]['progress']
            stasisFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2464463405']["objectiveProgress"]['progress']
            strandFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2889561660']["objectiveProgress"]['progress']

            sumTotal += (totalFinalBlowsCon + totalFinalBlowsTom + totalFinalBlowsDoug + totalFinalBlowsMark +
                         totalFinalBlowsJack + totalFinalBlowsHunt + totalFinalBlowsCam + totalFinalBlowsKade)
            sumArc += (arcFinalBlowsCon + arcFinalBlowsTom + arcFinalBlowsDoug + arcFinalBlowsMark + arcFinalBlowsJack +
                       arcFinalBlowsHunt + arcFinalBlowsCam + arcFinalBlowsKade)
            sumVoid += (voidFinalBlowsCon + voidFinalBlowsTom + voidFinalBlowsDoug + voidFinalBlowsMark +
                        voidFinalBlowsJack + voidFinalBlowsHunt + voidFinalBlowsCam + voidFinalBlowsKade)
            sumSolar += (solarFinalBlowsCon + solarFinalBlowsTom + solarFinalBlowsDoug + solarFinalBlowsMark +
                         solarFinalBlowsJack + solarFinalBlowsHunt + solarFinalBlowsCam + solarFinalBlowsKade)
            sumStatis += (stasisFinalBlowsCon + stasisFinalBlowsTom + stasisFinalBlowsDoug + stasisFinalBlowsMark +
                          stasisFinalBlowsJack + stasisFinalBlowsHunt + stasisFinalBlowsCam + stasisFinalBlowsKade)
            sumStrand += (strandFinalBlowsCon + strandFinalBlowsTom + strandFinalBlowsDoug + strandFinalBlowsMark +
                          strandFinalBlowsJack + strandFinalBlowsHunt + strandFinalBlowsCam + strandFinalBlowsKade)

            elementTable = PrettyTable()
            elementTable.field_names = ['Player', 'Arc', 'Solar', 'Void', 'Stasis', 'Strand', 'Total']
            elementTable.add_rows(
                [
                    ['Connor', arcFinalBlowsCon, solarFinalBlowsCon, voidFinalBlowsCon, stasisFinalBlowsCon,
                     strandFinalBlowsCon, totalFinalBlowsCon],
                    ['Thomas', arcFinalBlowsTom, solarFinalBlowsTom, voidFinalBlowsTom, stasisFinalBlowsTom,
                     strandFinalBlowsTom, totalFinalBlowsTom],
                    ['Douglas', arcFinalBlowsDoug, solarFinalBlowsDoug, voidFinalBlowsDoug, stasisFinalBlowsDoug,
                     strandFinalBlowsDoug, totalFinalBlowsDoug],
                    ['Mark', arcFinalBlowsMark, solarFinalBlowsMark, voidFinalBlowsMark, stasisFinalBlowsMark,
                     strandFinalBlowsMark, totalFinalBlowsMark],
                    ['Jack', arcFinalBlowsJack, solarFinalBlowsJack, voidFinalBlowsJack, stasisFinalBlowsJack,
                     strandFinalBlowsJack, totalFinalBlowsJack],
                    ['Hunter', arcFinalBlowsHunt, solarFinalBlowsHunt, voidFinalBlowsHunt, stasisFinalBlowsHunt,
                     strandFinalBlowsHunt, totalFinalBlowsHunt],
                    ['Cameron', arcFinalBlowsCam, solarFinalBlowsCam, voidFinalBlowsCam, stasisFinalBlowsCam,
                     strandFinalBlowsCam, totalFinalBlowsCam],
                    ['Kade', arcFinalBlowsKade, solarFinalBlowsKade, voidFinalBlowsKade, stasisFinalBlowsKade,
                     strandFinalBlowsKade, totalFinalBlowsKade],
                    ['Total', sumArc, sumSolar, sumVoid, sumStatis, sumStrand, sumTotal]
                ]
            )
            print(elementTable)

        def weaponFinalBlows():
            # Weapon Type Final Blows (all data before Beyond Light has been removed from the API)
            sumAuto = 0
            sumPulse = 0
            sumScout = 0
            sumHand = 0
            sumSide = 0
            sumSub = 0
            sumBow = 0
            sumFusion = 0
            sumShotgun = 0
            sumSniper = 0
            sumTrace = 0
            sumGrenade = 0
            sumSword = 0
            sumLMG = 0
            sumLinear = 0
            sumRocket = 0

            autoFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsCon = \
                metric_json["Response"][0]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsTom = \
                metric_json["Response"][1]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsDoug = \
                metric_json["Response"][2]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsMark = \
                metric_json["Response"][3]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsJack = \
                metric_json["Response"][4]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsHunt = \
                metric_json["Response"][5]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsCam = \
                metric_json["Response"][6]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            autoFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
            pulseFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
            scoutFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
            handFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
            sidearmFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
            submachineFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
            bowFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
            traceFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
            fusionFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
            shotgunFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
            sniperFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
            grenadeLaunchFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
            rocketFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
            swordFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
            linearFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
            machineGunFinalBlowsKade = \
                metric_json["Response"][7]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']

            sumAuto += autoFinalBlowsCon + autoFinalBlowsTom + autoFinalBlowsDoug + autoFinalBlowsMark + autoFinalBlowsJack + autoFinalBlowsHunt + autoFinalBlowsCam + autoFinalBlowsKade
            sumPulse += pulseFinalBlowsCon + pulseFinalBlowsTom + pulseFinalBlowsDoug + pulseFinalBlowsMark + pulseFinalBlowsJack + pulseFinalBlowsHunt + pulseFinalBlowsCam + pulseFinalBlowsKade
            sumScout += scoutFinalBlowsCon + scoutFinalBlowsTom + scoutFinalBlowsDoug + scoutFinalBlowsMark + scoutFinalBlowsJack + scoutFinalBlowsHunt + scoutFinalBlowsCam + scoutFinalBlowsKade
            sumHand += handFinalBlowsCon + handFinalBlowsTom + handFinalBlowsDoug + handFinalBlowsMark + handFinalBlowsJack + handFinalBlowsHunt + handFinalBlowsCam + handFinalBlowsKade
            sumSide += sidearmFinalBlowsCon + sidearmFinalBlowsTom + sidearmFinalBlowsDoug + sidearmFinalBlowsMark + sidearmFinalBlowsJack + sidearmFinalBlowsHunt + sidearmFinalBlowsCam + sidearmFinalBlowsKade
            sumSub += submachineFinalBlowsCon + submachineFinalBlowsTom + submachineFinalBlowsDoug + submachineFinalBlowsMark + submachineFinalBlowsJack + submachineFinalBlowsHunt + submachineFinalBlowsCam + submachineFinalBlowsKade
            sumBow += bowFinalBlowsCon + bowFinalBlowsTom + bowFinalBlowsDoug + bowFinalBlowsMark + bowFinalBlowsJack + bowFinalBlowsHunt + bowFinalBlowsCam + bowFinalBlowsKade
            sumFusion += fusionFinalBlowsCon + fusionFinalBlowsTom + fusionFinalBlowsDoug + fusionFinalBlowsMark + fusionFinalBlowsJack + fusionFinalBlowsHunt + fusionFinalBlowsCam + fusionFinalBlowsKade
            sumShotgun += shotgunFinalBlowsCon + shotgunFinalBlowsTom + shotgunFinalBlowsDoug + shotgunFinalBlowsMark + shotgunFinalBlowsJack + shotgunFinalBlowsHunt + shotgunFinalBlowsCam + shotgunFinalBlowsKade
            sumSniper += sniperFinalBlowsCon + sniperFinalBlowsTom + sniperFinalBlowsDoug + sniperFinalBlowsMark + sniperFinalBlowsJack + sniperFinalBlowsHunt + sniperFinalBlowsCam + sniperFinalBlowsKade
            sumTrace += traceFinalBlowsCon + traceFinalBlowsTom + traceFinalBlowsDoug + traceFinalBlowsMark + traceFinalBlowsJack + traceFinalBlowsHunt + traceFinalBlowsCam + traceFinalBlowsKade
            sumGrenade += grenadeLaunchFinalBlowsCon + grenadeLaunchFinalBlowsTom + grenadeLaunchFinalBlowsDoug + grenadeLaunchFinalBlowsMark + grenadeLaunchFinalBlowsJack + grenadeLaunchFinalBlowsHunt + grenadeLaunchFinalBlowsCam + grenadeLaunchFinalBlowsKade
            sumSword += swordFinalBlowsCon + swordFinalBlowsTom + swordFinalBlowsDoug + swordFinalBlowsMark + swordFinalBlowsJack + swordFinalBlowsHunt + swordFinalBlowsCam + swordFinalBlowsKade
            sumLMG += machineGunFinalBlowsCon + machineGunFinalBlowsTom + machineGunFinalBlowsDoug + machineGunFinalBlowsMark + machineGunFinalBlowsJack + machineGunFinalBlowsHunt + machineGunFinalBlowsCam + machineGunFinalBlowsKade
            sumLinear += linearFinalBlowsCon + linearFinalBlowsTom + linearFinalBlowsDoug + linearFinalBlowsMark + linearFinalBlowsJack + linearFinalBlowsHunt + linearFinalBlowsCam + linearFinalBlowsKade
            sumRocket += rocketFinalBlowsCon + rocketFinalBlowsTom + rocketFinalBlowsDoug + rocketFinalBlowsMark + rocketFinalBlowsJack + rocketFinalBlowsHunt + rocketFinalBlowsCam + rocketFinalBlowsKade

            weaponTable = PrettyTable()
            weaponTable.field_names = ['Weapon', ' Connor', 'Thomas', 'Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron',
                                       'Kade', 'Total']
            weaponTable.add_rows(
                [
                    ['Auto Rifle', autoFinalBlowsCon, autoFinalBlowsTom, autoFinalBlowsDoug, autoFinalBlowsMark,
                     autoFinalBlowsJack, autoFinalBlowsHunt, autoFinalBlowsCam, autoFinalBlowsKade, sumAuto],
                    ['Pulse Rifle', pulseFinalBlowsCon, pulseFinalBlowsTom, pulseFinalBlowsDoug, pulseFinalBlowsMark,
                     pulseFinalBlowsJack, pulseFinalBlowsHunt, pulseFinalBlowsCam, pulseFinalBlowsKade, sumPulse],
                    ['Scout Rifle', scoutFinalBlowsCon, scoutFinalBlowsTom, scoutFinalBlowsDoug, scoutFinalBlowsMark,
                     scoutFinalBlowsJack, scoutFinalBlowsHunt, scoutFinalBlowsCam, scoutFinalBlowsKade, sumScout],
                    ['Hand Cannon', handFinalBlowsCon, handFinalBlowsTom, handFinalBlowsDoug, handFinalBlowsMark,
                     handFinalBlowsJack, handFinalBlowsHunt, handFinalBlowsCam, handFinalBlowsKade, sumHand],
                    ['Submachine Gun', submachineFinalBlowsCon, submachineFinalBlowsTom, submachineFinalBlowsDoug,
                     submachineFinalBlowsMark, submachineFinalBlowsJack, submachineFinalBlowsHunt,
                     submachineFinalBlowsCam, submachineFinalBlowsKade, sumSub],
                    ['Sidearm', sidearmFinalBlowsCon, sidearmFinalBlowsTom, sidearmFinalBlowsDoug,
                     sidearmFinalBlowsMark, sidearmFinalBlowsJack, sidearmFinalBlowsHunt, sidearmFinalBlowsCam,
                     sidearmFinalBlowsKade, sumSide],
                    ['Combat Bow', bowFinalBlowsCon, bowFinalBlowsTom, bowFinalBlowsDoug, bowFinalBlowsMark,
                     bowFinalBlowsJack, bowFinalBlowsHunt, bowFinalBlowsCam, bowFinalBlowsKade, sumBow],
                    ['Trace Rifle', traceFinalBlowsCon, traceFinalBlowsTom, traceFinalBlowsDoug, traceFinalBlowsMark,
                     traceFinalBlowsJack, traceFinalBlowsHunt, traceFinalBlowsCam, traceFinalBlowsKade, sumTrace],
                    ['Fusion Rifle', fusionFinalBlowsCon, fusionFinalBlowsTom, fusionFinalBlowsDoug,
                     fusionFinalBlowsMark, fusionFinalBlowsJack, fusionFinalBlowsHunt, fusionFinalBlowsCam,
                     fusionFinalBlowsKade, sumFusion],
                    ['Shotgun', shotgunFinalBlowsCon, shotgunFinalBlowsTom, shotgunFinalBlowsDoug,
                     shotgunFinalBlowsMark, shotgunFinalBlowsJack, shotgunFinalBlowsHunt, shotgunFinalBlowsCam,
                     shotgunFinalBlowsKade, sumShotgun],
                    ['Sniper Rifle', sniperFinalBlowsCon, sniperFinalBlowsTom, sniperFinalBlowsDoug,
                     sniperFinalBlowsMark, sniperFinalBlowsJack, sniperFinalBlowsHunt, sniperFinalBlowsCam,
                     sniperFinalBlowsKade, sumSniper],
                    ['Grenade Launcher', grenadeLaunchFinalBlowsCon, grenadeLaunchFinalBlowsTom,
                     grenadeLaunchFinalBlowsDoug, grenadeLaunchFinalBlowsMark, grenadeLaunchFinalBlowsJack,
                     grenadeLaunchFinalBlowsHunt, grenadeLaunchFinalBlowsCam, grenadeLaunchFinalBlowsKade, sumGrenade],
                    ['Sword', swordFinalBlowsCon, swordFinalBlowsTom, swordFinalBlowsDoug, swordFinalBlowsMark,
                     swordFinalBlowsJack, swordFinalBlowsHunt, swordFinalBlowsCam, swordFinalBlowsKade, sumSword],
                    ['Linear Fusion Rifle', linearFinalBlowsCon, linearFinalBlowsTom, linearFinalBlowsDoug,
                     linearFinalBlowsMark, linearFinalBlowsJack, linearFinalBlowsHunt, linearFinalBlowsCam,
                     linearFinalBlowsKade, sumLinear],
                    ['Rocket Launcher', rocketFinalBlowsCon, rocketFinalBlowsTom, rocketFinalBlowsDoug,
                     rocketFinalBlowsMark, rocketFinalBlowsJack, rocketFinalBlowsHunt, rocketFinalBlowsCam,
                     rocketFinalBlowsKade, sumRocket],
                    ['Machine Gun', machineGunFinalBlowsCon, machineGunFinalBlowsTom, machineGunFinalBlowsDoug,
                     machineGunFinalBlowsMark, machineGunFinalBlowsJack, machineGunFinalBlowsHunt,
                     machineGunFinalBlowsCam, machineGunFinalBlowsKade, sumLMG],
                ]
            )
            weaponTable.reversesort = True
            print(weaponTable.get_string(sortby='Total'))

        elementFinalBlows()
        weaponFinalBlows()

    def strikeMetrics():
        def strikeData():
            sumStrike = 0
            sumFlawless = 0
            sumChamps = 0
            aveFinalBlowsS = 0

            strikeCompleteCon = metric_json["Response"][0]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeCon = metric_json["Response"][0]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedCon = metric_json["Response"][0]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSCon = metric_json["Response"][0]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteTom = metric_json["Response"][1]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeTom = metric_json["Response"][1]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedTom = metric_json["Response"][1]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSTom = metric_json["Response"][1]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteDoug = metric_json["Response"][2]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedDoug = metric_json["Response"][2]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteMark = metric_json["Response"][3]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeMark = metric_json["Response"][3]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedMark = metric_json["Response"][3]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSMark = metric_json["Response"][3]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteJack = metric_json["Response"][4]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeJack = metric_json["Response"][4]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedJack = metric_json["Response"][4]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSJack = metric_json["Response"][4]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteHunt = metric_json["Response"][5]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedHunt = metric_json["Response"][5]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteCam = metric_json["Response"][6]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeCam = metric_json["Response"][6]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedCam = metric_json["Response"][6]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSCam = metric_json["Response"][6]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            strikeCompleteKade = metric_json["Response"][7]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
            flawlessStrikeKade = metric_json["Response"][7]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
            champsDefeatedKade = metric_json["Response"][7]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
            finalBlowsPerSKade = metric_json["Response"][7]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']

            sumStrike += strikeCompleteCon + strikeCompleteTom + strikeCompleteDoug + strikeCompleteMark + strikeCompleteJack + strikeCompleteHunt + strikeCompleteCam + strikeCompleteKade
            sumFlawless += flawlessStrikeCon + flawlessStrikeTom + flawlessStrikeDoug + flawlessStrikeMark + flawlessStrikeJack + flawlessStrikeHunt + flawlessStrikeCam + flawlessStrikeKade
            sumChamps += champsDefeatedCon + champsDefeatedTom + champsDefeatedDoug + champsDefeatedMark + champsDefeatedJack + champsDefeatedHunt + champsDefeatedCam + champsDefeatedKade
            aveFinalBlowsS += round((finalBlowsPerSCon + finalBlowsPerSTom + finalBlowsPerSDoug + finalBlowsPerSMark + finalBlowsPerSJack + finalBlowsPerSHunt + finalBlowsPerSCam + finalBlowsPerSKade) / 8 , 2)

            strikeTable = PrettyTable()
            strikeTable.field_names = ['Player', 'Strike Completions', 'Flawless Strike Completions', 'Champions Defeated', 'Final Blows per Strike']
            strikeTable.add_rows(
                [
                    ['Connor', strikeCompleteCon, flawlessStrikeCon, champsDefeatedCon, finalBlowsPerSCon],
                    ['Thomas', strikeCompleteTom, flawlessStrikeTom, champsDefeatedTom, finalBlowsPerSTom],
                    ['Douglas', strikeCompleteDoug, flawlessStrikeDoug, champsDefeatedDoug, finalBlowsPerSDoug],
                    ['Mark', strikeCompleteMark, flawlessStrikeMark, champsDefeatedMark, finalBlowsPerSMark],
                    ['Jack', strikeCompleteJack, flawlessStrikeJack, champsDefeatedJack, finalBlowsPerSJack],
                    ['Hunter', strikeCompleteHunt, flawlessStrikeHunt, champsDefeatedHunt, finalBlowsPerSHunt],
                    ['Cameron', strikeCompleteCam, flawlessStrikeCam, champsDefeatedCam, finalBlowsPerSCam],
                    ['Kade', strikeCompleteKade, flawlessStrikeKade, champsDefeatedKade, finalBlowsPerSKade],
                    ['Total', sumStrike, sumFlawless, sumChamps, aveFinalBlowsS]
                ]
            )
            print(strikeTable)

        def nightfallData():
            armsDealerCon = metric_json["Response"][0]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermCon = metric_json["Response"][0]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireCon = metric_json["Response"][0]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongCon = metric_json["Response"][0]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionCon = metric_json["Response"][0]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashCon = metric_json["Response"][0]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldCon = metric_json["Response"][0]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityCon = metric_json["Response"][0]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainCon = metric_json["Response"][0]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingCon = metric_json["Response"][0]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdCon = metric_json["Response"][0]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepCon = metric_json["Response"][0]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsCon = metric_json["Response"][0]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedCon = metric_json["Response"][0]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreCon = metric_json["Response"][0]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedCon = metric_json["Response"][0]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayCon = metric_json["Response"][0]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsCon = metric_json["Response"][0]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairCon = metric_json["Response"][0]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERCon = metric_json["Response"][0]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairCon = metric_json["Response"][0]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeCon = metric_json["Response"][0]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileCon = metric_json["Response"][0]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerTom = metric_json["Response"][1]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermTom = metric_json["Response"][1]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireTom = metric_json["Response"][1]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongTom = metric_json["Response"][1]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionTom = metric_json["Response"][1]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashTom = metric_json["Response"][1]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldTom = metric_json["Response"][1]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityTom = metric_json["Response"][1]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainTom = metric_json["Response"][1]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingTom = metric_json["Response"][1]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdTom = metric_json["Response"][1]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepTom = metric_json["Response"][1]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsTom = metric_json["Response"][1]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedTom = metric_json["Response"][1]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreTom = metric_json["Response"][1]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedTom = metric_json["Response"][1]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayTom = metric_json["Response"][1]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsTom = metric_json["Response"][1]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairTom = metric_json["Response"][1]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERTom = metric_json["Response"][1]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairTom = metric_json["Response"][1]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeTom = metric_json["Response"][1]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileTom = metric_json["Response"][1]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashDoug = metric_json["Response"][2]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainDoug = metric_json["Response"][2]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingDoug = metric_json["Response"][2]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdDoug = metric_json["Response"][2]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepDoug = metric_json["Response"][2]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreDoug = metric_json["Response"][2]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedDoug = metric_json["Response"][2]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairDoug = metric_json["Response"][2]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERDoug = metric_json["Response"][2]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairDoug = metric_json["Response"][2]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeDoug = metric_json["Response"][2]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileDoug = metric_json["Response"][2]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerMark = metric_json["Response"][3]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermMark = metric_json["Response"][3]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireMark = metric_json["Response"][3]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongMark = metric_json["Response"][3]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionMark = metric_json["Response"][3]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashMark = metric_json["Response"][3]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldMark = metric_json["Response"][3]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityMark = metric_json["Response"][3]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainMark = metric_json["Response"][3]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingMark = metric_json["Response"][3]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdMark = metric_json["Response"][3]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepMark = metric_json["Response"][3]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsMark = metric_json["Response"][3]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedMark = metric_json["Response"][3]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreMark = metric_json["Response"][3]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedMark = metric_json["Response"][3]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayMark = metric_json["Response"][3]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsMark = metric_json["Response"][3]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairMark = metric_json["Response"][3]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERMark = metric_json["Response"][3]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairMark = metric_json["Response"][3]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeMark = metric_json["Response"][3]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileMark = metric_json["Response"][3]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerJack = metric_json["Response"][4]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermJack = metric_json["Response"][4]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireJack = metric_json["Response"][4]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongJack = metric_json["Response"][4]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionJack = metric_json["Response"][4]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashJack = metric_json["Response"][4]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldJack = metric_json["Response"][4]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityJack = metric_json["Response"][4]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainJack = metric_json["Response"][4]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingJack = metric_json["Response"][4]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdJack = metric_json["Response"][4]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepJack = metric_json["Response"][4]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsJack = metric_json["Response"][4]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedJack = metric_json["Response"][4]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreJack = metric_json["Response"][4]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedJack = metric_json["Response"][4]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayJack = metric_json["Response"][4]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsJack = metric_json["Response"][4]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairJack = metric_json["Response"][4]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERJack = metric_json["Response"][4]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairJack = metric_json["Response"][4]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeJack = metric_json["Response"][4]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileJack = metric_json["Response"][4]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashHunt = metric_json["Response"][5]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainHunt = metric_json["Response"][5]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingHunt = metric_json["Response"][5]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdHunt = metric_json["Response"][5]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepHunt = metric_json["Response"][5]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreHunt = metric_json["Response"][5]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedHunt = metric_json["Response"][5]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairHunt = metric_json["Response"][5]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERHunt = metric_json["Response"][5]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairHunt = metric_json["Response"][5]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeHunt = metric_json["Response"][5]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileHunt = metric_json["Response"][5]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerCam = metric_json["Response"][6]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermCam = metric_json["Response"][6]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireCam = metric_json["Response"][6]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongCam = metric_json["Response"][6]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionCam = metric_json["Response"][6]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashCam = metric_json["Response"][6]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldCam = metric_json["Response"][6]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityCam = metric_json["Response"][6]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainCam = metric_json["Response"][6]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingCam = metric_json["Response"][6]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdCam = metric_json["Response"][6]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepCam = metric_json["Response"][6]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsCam = metric_json["Response"][6]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedCam = metric_json["Response"][6]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreCam = metric_json["Response"][6]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedCam = metric_json["Response"][6]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayCam = metric_json["Response"][6]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsCam = metric_json["Response"][6]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairCam = metric_json["Response"][6]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERCam = metric_json["Response"][6]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairCam = metric_json["Response"][6]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeCam = metric_json["Response"][6]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileCam = metric_json["Response"][6]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            armsDealerKade = metric_json["Response"][7]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
            insightTermKade = metric_json["Response"][7]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
            invertedSpireKade = metric_json["Response"][7]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
            savaSongKade = metric_json["Response"][7]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
            pyramidionKade = metric_json["Response"][7]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
            exodusCrashKade = metric_json["Response"][7]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
            gardenWorldKade = metric_json["Response"][7]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
            treeOfPossibilityKade = metric_json["Response"][7]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
            strangeTerrainKade = metric_json["Response"][7]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
            wardenOfNothingKade = metric_json["Response"][7]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
            broodholdKade = metric_json["Response"][7]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
            scarletKeepKade = metric_json["Response"][7]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
            lakeOfShadowsKade = metric_json["Response"][7]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
            theCorruptedKade = metric_json["Response"][7]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
            festeringCoreKade = metric_json["Response"][7]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
            theDisgracedKade = metric_json["Response"][7]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
            theGlasswayKade = metric_json["Response"][7]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
            provingGroundsKade = metric_json["Response"][7]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
            devilsLairKade = metric_json["Response"][7]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
            fallenSABERKade = metric_json["Response"][7]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
            hollowedLairKade = metric_json["Response"][7]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
            theLightbladeKade = metric_json["Response"][7]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
            birthplaceOTVileKade = metric_json["Response"][7]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']

            nightfallTable = PrettyTable()
            nightfallTable.field_names = ['Nightfall', 'Connor', 'Thomas', 'Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron', 'Kade']
            nightfallTable.add_rows(
                [
                    ['Arms Dealer', armsDealerCon, armsDealerTom, armsDealerDoug, armsDealerMark, armsDealerJack, armsDealerHunt, armsDealerCam, armsDealerKade],
                    ['Insight Terminus', insightTermCon, insightTermTom, insightTermDoug, insightTermMark, insightTermJack, insightTermHunt, insightTermCam, insightTermKade],
                    ['The Inverted Spire', invertedSpireCon, invertedSpireTom, invertedSpireDoug, invertedSpireMark, invertedSpireJack, invertedSpireHunt, invertedSpireCam, invertedSpireKade],
                    ["Savathûn's Song", savaSongCon, savaSongTom, savaSongDoug, savaSongMark, savaSongJack, savaSongHunt, savaSongCam, savaSongKade],
                    ['The Pyramidion', pyramidionCon, pyramidionTom, pyramidionDoug, pyramidionMark, pyramidionJack, pyramidionHunt, pyramidionCam, pyramidionKade],
                    ['Exodus Crash', exodusCrashCon, exodusCrashTom, exodusCrashDoug, exodusCrashMark, exodusCrashJack, exodusCrashHunt, exodusCrashCam, exodusCrashKade],
                    ['A Garden World', gardenWorldCon, gardenWorldTom, gardenWorldDoug, gardenWorldMark, gardenWorldJack, gardenWorldHunt, gardenWorldCam, gardenWorldKade],
                    ['Tree of Possibilities', treeOfPossibilityCon, treeOfPossibilityTom, treeOfPossibilityDoug, treeOfPossibilityMark, treeOfPossibilityJack, treeOfPossibilityHunt, treeOfPossibilityCam, treeOfPossibilityKade],
                    ['Strange Terrain', strangeTerrainCon, strangeTerrainTom, strangeTerrainDoug, strangeTerrainMark, strangeTerrainJack, strangeTerrainHunt, strangeTerrainCam, strangeTerrainKade],
                    ['Warden of Nothing', wardenOfNothingCon, wardenOfNothingTom, wardenOfNothingDoug, wardenOfNothingMark, wardenOfNothingJack, wardenOfNothingHunt, wardenOfNothingCam, wardenOfNothingKade],
                    ['Broodhold', broodholdCon, broodholdTom, broodholdDoug, broodholdMark, broodholdJack, broodholdHunt, broodholdCam, broodholdKade],
                    ['The Scarlet Keep', scarletKeepCon, scarletKeepTom, scarletKeepDoug, scarletKeepMark, scarletKeepJack, scarletKeepHunt, scarletKeepCam, scarletKeepKade],
                    ['Lake of Shadows', lakeOfShadowsCon, lakeOfShadowsTom, lakeOfShadowsDoug, lakeOfShadowsMark, lakeOfShadowsJack, lakeOfShadowsHunt, lakeOfShadowsCam, lakeOfShadowsKade],
                    ['The Corrupted', theCorruptedCon, theCorruptedTom, theCorruptedDoug, theCorruptedMark, theCorruptedJack, theCorruptedHunt, theCorruptedCam, theCorruptedKade],
                    ['The Festering Core', festeringCoreCon, festeringCoreTom, festeringCoreDoug, festeringCoreMark, festeringCoreJack, festeringCoreHunt, festeringCoreCam, festeringCoreKade],
                    ['The Disgraced', theDisgracedCon, theDisgracedTom, theDisgracedDoug, theDisgracedMark, theDisgracedJack, theDisgracedHunt, theDisgracedCam, theDisgracedKade],
                    ['The Glassway', theGlasswayCon, theGlasswayTom, theGlasswayDoug, theGlasswayMark, theGlasswayJack, theGlasswayHunt, theGlasswayCam, theGlasswayKade],
                    ['Proving Grounds', provingGroundsCon, provingGroundsTom, provingGroundsDoug, provingGroundsMark, provingGroundsJack, provingGroundsHunt, provingGroundsCam, provingGroundsKade],
                    ["The Devil's Lair", devilsLairCon, devilsLairTom, devilsLairDoug, devilsLairMark, devilsLairJack, devilsLairHunt, devilsLairCam, devilsLairKade],
                    ['Fallen S.A.B.E.R.', fallenSABERCon, fallenSABERTom, fallenSABERDoug, fallenSABERMark, fallenSABERJack, fallenSABERHunt, fallenSABERCam, fallenSABERKade],
                    ['The Hollowed Lair', hollowedLairCon, hollowedLairTom, hollowedLairDoug, hollowedLairMark, hollowedLairJack, hollowedLairHunt, hollowedLairCam, hollowedLairKade],
                    ['The Lightblade', theLightbladeCon, theLightbladeTom, theLightbladeDoug, theLightbladeMark, theLightbladeJack, theLightbladeHunt, theLightbladeCam, theLightbladeKade],
                    ['Birthplace of the Vile', birthplaceOTVileCon, birthplaceOTVileTom, birthplaceOTVileDoug, birthplaceOTVileMark, birthplaceOTVileJack, birthplaceOTVileHunt, birthplaceOTVileCam, birthplaceOTVileKade]
                ]
            )
            print(nightfallTable)

        strikeData()
        nightfallData()

    seasonalMetrics()
    accountMetrics()
    strikeMetrics()