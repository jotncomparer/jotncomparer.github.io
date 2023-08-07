# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-7-2023
# This program needs Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program takes the generated .json file made in Character Metrics to build the table of values to sort through.
# This program specifically looks at triumph score for all players.

import json
from Time_Converter import Time_Converter
from prettytable import PrettyTable

def allTimeWasted():
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

    minutesPlayedTotal = 0
    minutesPlayedTotalCon = 0
    minutesPlayedTotalTom = 0
    minutesPlayedTotalDoug = 0
    minutesPlayedTotalMark = 0
    minutesPlayedTotalJack = 0
    minutesPlayedTotalHunt = 0
    minutesPlayedTotalCam = 0
    minutesPlayedTotalKade = 0

    # Connor - Titan
    dateLastPlayedTitanCon = metric_json["Response"][0]["characters"]['data']['2305843009644414176']['dateLastPlayed']
    minutesPlayedTotalCon += int(metric_json["Response"][0]["characters"]['data']['2305843009644414176']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009644414176']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarCon = metric_json["Response"][0]["characters"]['data']['2305843009663894341']['dateLastPlayed']
    minutesPlayedTotalCon += int(metric_json["Response"][0]["characters"]['data']['2305843009663894341']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009663894341']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterCon = metric_json["Response"][0]["characters"]['data']['2305843009703275457']['dateLastPlayed']
    minutesPlayedTotalCon += int(metric_json["Response"][0]["characters"]['data']['2305843009703275457']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009703275457']['minutesPlayedTotal'])

    secondsPlayedTotalCon = minutesPlayedTotalCon * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneCon = dateLastPlayedTitanCon > dateLastPlayedWarCon
    compareTwoCon = dateLastPlayedWarCon > dateLastPlayedHunterCon

    if compareOneCon == True and compareTwoCon == True:
        lastLoggedCon = dateLastPlayedTitanCon
    elif compareOneCon == True and compareTwoCon == False:
        lastLoggedCon = dateLastPlayedTitanCon
    elif compareOneCon == False and compareTwoCon == True:
        lastLoggedCon = dateLastPlayedWarCon
    else:
        lastLoggedCon = dateLastPlayedHunterCon

    # Thomas - Titan
    dateLastPlayedTitanTom = metric_json["Response"][1]["characters"]['data']['2305843009283965144']['dateLastPlayed']
    minutesPlayedTotal += int(metric_json["Response"][1]["characters"]['data']['2305843009283965144']['minutesPlayedTotal'])
    minutesPlayedTotalTom += int(metric_json["Response"][1]["characters"]['data']['2305843009283965144']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarTom = metric_json["Response"][1]["characters"]['data']['2305843009265786295']['dateLastPlayed']
    minutesPlayedTotal += int(metric_json["Response"][1]["characters"]['data']['2305843009265786295'][ 'minutesPlayedTotal'])
    minutesPlayedTotalTom += int(metric_json["Response"][1]["characters"]['data']['2305843009265786295'][ 'minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterTom = metric_json["Response"][1]["characters"]['data']['2305843009569534739']['dateLastPlayed']
    minutesPlayedTotal += int(metric_json["Response"][1]["characters"]['data']['2305843009569534739']['minutesPlayedTotal'])
    minutesPlayedTotalTom += int(metric_json["Response"][1]["characters"]['data']['2305843009569534739']['minutesPlayedTotal'])

    secondsPlayedTotalTom = minutesPlayedTotalTom * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneTom = dateLastPlayedTitanTom > dateLastPlayedWarTom
    compareTwoTom = dateLastPlayedWarTom > dateLastPlayedHunterTom

    if compareOneTom == True and compareTwoTom == True:
        lastLoggedTom = dateLastPlayedTitanTom
    elif compareOneTom == True and compareTwoTom == False:
        lastLoggedTom = dateLastPlayedTitanTom
    elif compareOneTom == False and compareTwoTom == True:
        lastLoggedTom = dateLastPlayedWarTom
    else:
        lastLoggedTom = dateLastPlayedHunterTom

    # Douglas - Titan
    dateLastPlayedTitanDoug = metric_json["Response"][2]["characters"]['data']['2305843009293915719']['dateLastPlayed']
    minutesPlayedTotal += int(metric_json["Response"][2]["characters"]['data']['2305843009293915719']['minutesPlayedTotal'])
    minutesPlayedTotalDoug += int(metric_json["Response"][2]["characters"]['data']['2305843009293915719']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarDoug = metric_json["Response"][2]["characters"]['data']['2305843009301374530']['dateLastPlayed']
    minutesPlayedTotal += int(metric_json["Response"][2]["characters"]['data']['2305843009301374530']['minutesPlayedTotal'])
    minutesPlayedTotalDoug += int(metric_json["Response"][2]["characters"]['data']['2305843009301374530']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterDoug = metric_json["Response"][2]["characters"]['data']['2305843010083874501']['dateLastPlayed']
    minutesPlayedTotal += int(metric_json["Response"][2]["characters"]['data']['2305843010083874501']['minutesPlayedTotal'])
    minutesPlayedTotalDoug += int(metric_json["Response"][2]["characters"]['data']['2305843010083874501']['minutesPlayedTotal'])

    secondsPlayedTotalDoug = minutesPlayedTotalDoug * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneDoug = dateLastPlayedTitanDoug > dateLastPlayedWarDoug
    compareTwoDoug = dateLastPlayedWarDoug > dateLastPlayedHunterDoug

    if compareOneDoug == True and compareTwoDoug == True:
        lastLoggedDoug = dateLastPlayedTitanDoug
    elif compareOneDoug == True and compareTwoDoug == False:
        lastLoggedDoug = dateLastPlayedTitanDoug
    elif compareOneDoug == False and compareTwoDoug == True:
        lastLoggedDoug = dateLastPlayedWarDoug
    else:
        lastLoggedDoug = dateLastPlayedHunterDoug

    # Mark - Titan
    dateLastPlayedTitanMark = metric_json["Response"][3]["characters"]['data']['2305843009668854600']['dateLastPlayed']
    minutesPlayedTotalMark += int(metric_json["Response"][3]["characters"]['data']['2305843009668854600']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][3]["characters"]['data']['2305843009668854600']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarMark = metric_json["Response"][3]["characters"]['data']['2305843009802904121']['dateLastPlayed']
    minutesPlayedTotalMark += int(metric_json["Response"][3]["characters"]['data']['2305843009802904121']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][3]["characters"]['data']['2305843009802904121']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterMark = metric_json["Response"][3]["characters"]['data']['2305843009348154555']['dateLastPlayed']
    minutesPlayedTotalMark += int(metric_json["Response"][3]["characters"]['data']['2305843009348154555']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][3]["characters"]['data']['2305843009348154555']['minutesPlayedTotal'])

    secondsPlayedTotalMark = minutesPlayedTotalMark * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneMark = dateLastPlayedTitanMark > dateLastPlayedWarMark
    compareTwoMark = dateLastPlayedWarMark > dateLastPlayedHunterMark

    if compareOneMark == True and compareTwoMark == True:
        lastLoggedMark = dateLastPlayedTitanMark
    elif compareOneMark == True and compareTwoMark == False:
        lastLoggedMark = dateLastPlayedTitanMark
    elif compareOneMark == False and compareTwoMark == True:
        lastLoggedMark = dateLastPlayedWarMark
    else:
        lastLoggedMark = dateLastPlayedHunterMark

    # Jack - Titan
    dateLastPlayedTitanJack = metric_json["Response"][4]["characters"]['data']['2305843009890274343']['dateLastPlayed']
    minutesPlayedTotalJack += int(metric_json["Response"][4]["characters"]['data']['2305843009890274343']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][4]["characters"]['data']['2305843009890274343']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarJack = metric_json["Response"][4]["characters"]['data']['2305843009891864023']['dateLastPlayed']
    minutesPlayedTotalJack += int(metric_json["Response"][4]["characters"]['data']['2305843009891864023']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][4]["characters"]['data']['2305843009891864023']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterJack = metric_json["Response"][4]["characters"]['data']['2305843009268771475']['dateLastPlayed']
    minutesPlayedTotalJack += int(metric_json["Response"][4]["characters"]['data']['2305843009268771475']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][4]["characters"]['data']['2305843009268771475']['minutesPlayedTotal'])

    secondsPlayedTotalJack = minutesPlayedTotalJack * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneJack = dateLastPlayedTitanJack > dateLastPlayedWarJack
    compareTwoJack = dateLastPlayedWarJack > dateLastPlayedHunterJack

    if compareOneJack == True and compareTwoJack == True:
        lastLoggedJack = dateLastPlayedTitanJack
    elif compareOneJack == True and compareTwoJack == False:
        lastLoggedJack = dateLastPlayedTitanJack
    elif compareOneJack == False and compareTwoJack == True:
        lastLoggedJack = dateLastPlayedWarJack
    else:
        lastLoggedJack = dateLastPlayedHunterJack

    # Hunter - Titan
    dateLastPlayedTitanHunt = metric_json["Response"][5]["characters"]['data']['2305843009756404411']['dateLastPlayed']
    minutesPlayedTotalHunt += int(metric_json["Response"][5]["characters"]['data']['2305843009756404411']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][5]["characters"]['data']['2305843009756404411']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarHunt = metric_json["Response"][5]["characters"]['data']['2305843009359365362']['dateLastPlayed']
    minutesPlayedTotalHunt += int(metric_json["Response"][5]["characters"]['data']['2305843009359365362']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][5]["characters"]['data']['2305843009359365362']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterHunt = metric_json["Response"][5]["characters"]['data']['2305843009359734078']['dateLastPlayed']
    minutesPlayedTotalHunt += int(metric_json["Response"][5]["characters"]['data']['2305843009359734078']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][5]["characters"]['data']['2305843009359734078']['minutesPlayedTotal'])

    secondsPlayedTotalHunt = minutesPlayedTotalHunt * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneHunt = dateLastPlayedTitanHunt > dateLastPlayedWarHunt
    compareTwoHunt = dateLastPlayedWarHunt > dateLastPlayedHunterHunt

    if compareOneHunt == True and compareTwoHunt == True:
        lastLoggedHunt = dateLastPlayedTitanHunt
    elif compareOneHunt == True and compareTwoHunt == False:
        lastLoggedHunt = dateLastPlayedTitanHunt
    elif compareOneHunt == False and compareTwoHunt == True:
        lastLoggedHunt = dateLastPlayedWarHunt
    else:
        lastLoggedHunt = dateLastPlayedHunterHunt

    # Cameron - Titan
    dateLastPlayedTitanCam = metric_json["Response"][6]["characters"]['data']['2305843009624174508']['dateLastPlayed']
    minutesPlayedTotalCam += int(metric_json["Response"][6]["characters"]['data']['2305843009624174508']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][6]["characters"]['data']['2305843009624174508']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarCam = metric_json["Response"][6]["characters"]['data']['2305843009683284493']['dateLastPlayed']
    minutesPlayedTotalCam += int(metric_json["Response"][6]["characters"]['data']['2305843009683284493']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][6]["characters"]['data']['2305843009683284493']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterCam = metric_json["Response"][6]["characters"]['data']['2305843009683284492']['dateLastPlayed']
    minutesPlayedTotalCam += int(metric_json["Response"][6]["characters"]['data']['2305843009683284492']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][6]["characters"]['data']['2305843009683284492']['minutesPlayedTotal'])

    secondsPlayedTotalCam = minutesPlayedTotalCam * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneCam = dateLastPlayedTitanCam > dateLastPlayedWarCam
    compareTwoCam = dateLastPlayedWarCam > dateLastPlayedHunterCam

    if compareOneCam == True and compareTwoCam == True:
        lastLoggedCam = dateLastPlayedTitanCam
    elif compareOneCam == True and compareTwoCam == False:
        lastLoggedCam = dateLastPlayedTitanCam
    elif compareOneCam == False and compareTwoCam == True:
        lastLoggedCam = dateLastPlayedWarCam
    else:
        lastLoggedCam = dateLastPlayedHunterCam

    # Kade - Titan
    dateLastPlayedTitanKade = metric_json["Response"][7]["characters"]['data']['2305843009264637527']['dateLastPlayed']
    minutesPlayedTotalKade += int(metric_json["Response"][7]["characters"]['data']['2305843009264637527']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][7]["characters"]['data']['2305843009264637527']['minutesPlayedTotal'])
    # Warlock
    dateLastPlayedWarKade = metric_json["Response"][7]["characters"]['data']['2305843009264637524']['dateLastPlayed']
    minutesPlayedTotalKade += int(metric_json["Response"][7]["characters"]['data']['2305843009264637524']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][7]["characters"]['data']['2305843009264637524']['minutesPlayedTotal'])
    # Hunter
    dateLastPlayedHunterKade = metric_json["Response"][7]["characters"]['data']['2305843010322954573']['dateLastPlayed']
    minutesPlayedTotalKade += int(metric_json["Response"][7]["characters"]['data']['2305843010322954573']['minutesPlayedTotal'])
    minutesPlayedTotal += int(metric_json["Response"][7]["characters"]['data']['2305843010322954573']['minutesPlayedTotal'])

    secondsPlayedTotalKade = minutesPlayedTotalKade * 60
    secondsPlayedTotal = minutesPlayedTotal * 60
    compareOneKade = dateLastPlayedTitanKade > dateLastPlayedWarKade
    compareTwoKade = dateLastPlayedWarKade > dateLastPlayedHunterKade

    if compareOneKade == True and compareTwoKade == True:
        lastLoggedKade = dateLastPlayedTitanKade
    elif compareOneKade == True and compareTwoKade == False:
        lastLoggedKade = dateLastPlayedTitanKade
    elif compareOneKade == False and compareTwoKade == True:
        lastLoggedKade = dateLastPlayedWarKade
    else:
        lastLoggedKade = dateLastPlayedHunterKade

    timeWasted = PrettyTable()
    timeWasted.field_names = ['Time', 'Connor', 'Thomas',' Douglas', 'Mark', 'Jack', 'Hunter', 'Cameron', 'Kade']
    timeWasted.add_rows(
        [
            ['Last Logged Time', lastLoggedCon, lastLoggedTom, lastLoggedDoug, lastLoggedMark, lastLoggedJack, lastLoggedHunt, lastLoggedCam, lastLoggedKade],
            ['Time Wasted', Time_Converter(secondsPlayedTotalCon), Time_Converter(secondsPlayedTotalTom),
             Time_Converter(secondsPlayedTotalDoug), Time_Converter(secondsPlayedTotalMark),
             Time_Converter(secondsPlayedTotalJack), Time_Converter(secondsPlayedTotalHunt),
             Time_Converter(secondsPlayedTotalCam), Time_Converter(secondsPlayedTotalKade)]
        ]
    )
    print(timeWasted)