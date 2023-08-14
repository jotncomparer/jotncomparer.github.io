# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-14-2023
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

    minutesPlayedTotalCon = 0
    minutesPlayedTotalTom = 0
    minutesPlayedTotalDoug = 0
    minutesPlayedTotalMark = 0
    minutesPlayedTotalJack = 0
    minutesPlayedTotalHunt = 0
    minutesPlayedTotalCam = 0
    minutesPlayedTotalKade = 0
    secondsPlayedTotal = 0

    # Connor - Titan
    dateLastPlayedCon = metric_json['Response'][0]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalCon += int(
        metric_json["Response"][0]["characters"]['data']['2305843009644414176']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalCon += int(
        metric_json["Response"][0]["characters"]['data']['2305843009663894341']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalCon += int(
        metric_json["Response"][0]["characters"]['data']['2305843009703275457']['minutesPlayedTotal'])

    secondsPlayedTotalCon = minutesPlayedTotalCon * 60
    secondsPlayedTotal += minutesPlayedTotalCon * 60

    # Thomas - Titan
    dateLastPlayedTom = metric_json['Response'][1]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalTom += int(
        metric_json["Response"][1]["characters"]['data']['2305843009283965144']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalTom += int(
        metric_json["Response"][1]["characters"]['data']['2305843009265786295']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalTom += int(
        metric_json["Response"][1]["characters"]['data']['2305843009569534739']['minutesPlayedTotal'])

    secondsPlayedTotalTom = minutesPlayedTotalTom * 60
    secondsPlayedTotal += minutesPlayedTotalTom * 60

    # Douglas - Titan
    dateLastPlayedDoug = metric_json['Response'][2]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalDoug += int(
        metric_json["Response"][2]["characters"]['data']['2305843009293915719']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalDoug += int(
        metric_json["Response"][2]["characters"]['data']['2305843009301374530']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalDoug += int(
        metric_json["Response"][2]["characters"]['data']['2305843010083874501']['minutesPlayedTotal'])

    secondsPlayedTotalDoug = minutesPlayedTotalDoug * 60
    secondsPlayedTotal += minutesPlayedTotalDoug * 60

    # Mark - Titan
    dateLastPlayedMark = metric_json['Response'][3]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalMark += int(
        metric_json["Response"][3]["characters"]['data']['2305843009668854600']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalMark += int(
        metric_json["Response"][3]["characters"]['data']['2305843009802904121']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalMark += int(
        metric_json["Response"][3]["characters"]['data']['2305843009348154555']['minutesPlayedTotal'])

    secondsPlayedTotalMark = minutesPlayedTotalMark * 60
    secondsPlayedTotal += minutesPlayedTotalMark * 60

    # Jack - Titan
    dateLastPlayedJack = metric_json['Response'][4]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalJack += int(
        metric_json["Response"][4]["characters"]['data']['2305843009890274343']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalJack += int(
        metric_json["Response"][4]["characters"]['data']['2305843009891864023']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalJack += int(
        metric_json["Response"][4]["characters"]['data']['2305843009268771475']['minutesPlayedTotal'])

    secondsPlayedTotalJack = minutesPlayedTotalJack * 60
    secondsPlayedTotal += minutesPlayedTotalJack * 60

    # Hunter - Titan
    dateLastPlayedHunt = metric_json['Response'][5]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalHunt += int(
        metric_json["Response"][5]["characters"]['data']['2305843009756404411']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalHunt += int(
        metric_json["Response"][5]["characters"]['data']['2305843009359365362']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalHunt += int(
        metric_json["Response"][5]["characters"]['data']['2305843009359734078']['minutesPlayedTotal'])

    secondsPlayedTotalHunt = minutesPlayedTotalHunt * 60
    secondsPlayedTotal += minutesPlayedTotalHunt * 60

    # Cameron - Titan
    dateLastPlayedCam = metric_json['Response'][6]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalCam += int(
        metric_json["Response"][6]["characters"]['data']['2305843009624174508']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalCam += int(
        metric_json["Response"][6]["characters"]['data']['2305843009683284493']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalCam += int(
        metric_json["Response"][6]["characters"]['data']['2305843009683284492']['minutesPlayedTotal'])

    secondsPlayedTotalCam = minutesPlayedTotalCam * 60
    secondsPlayedTotal += minutesPlayedTotalCam * 60

    # Kade - Titan
    dateLastPlayedKade = metric_json['Response'][7]['profile']['data']['dateLastPlayed']
    minutesPlayedTotalKade += int(
        metric_json["Response"][7]["characters"]['data']['2305843009264637527']['minutesPlayedTotal'])
    # Warlock
    minutesPlayedTotalKade += int(
        metric_json["Response"][7]["characters"]['data']['2305843009264637524']['minutesPlayedTotal'])
    # Hunter
    minutesPlayedTotalKade += int(
        metric_json["Response"][7]["characters"]['data']['2305843010322954573']['minutesPlayedTotal'])

    secondsPlayedTotalKade = minutesPlayedTotalKade * 60
    secondsPlayedTotal += minutesPlayedTotalKade * 60

    timeWasted = PrettyTable()
    timeWasted.field_names = ['Player', 'Last Logged In', 'Time Wasted']
    timeWasted.add_rows(
        [
            ['Connor', dateLastPlayedCon, Time_Converter(secondsPlayedTotalCon)],
            ['Thomas', dateLastPlayedTom, Time_Converter(secondsPlayedTotalTom)],
            ['Douglas', dateLastPlayedDoug, Time_Converter(secondsPlayedTotalDoug)],
            ['Mark', dateLastPlayedMark, Time_Converter(secondsPlayedTotalMark)],
            ['Jack', dateLastPlayedJack, Time_Converter(secondsPlayedTotalJack)],
            ['Hunter', dateLastPlayedHunt, Time_Converter(secondsPlayedTotalHunt)],
            ['Cameron', dateLastPlayedCam, Time_Converter(secondsPlayedTotalCam)],
            ['Kade', dateLastPlayedKade, Time_Converter(secondsPlayedTotalKade)],
            ['Total', 'Last Logged In', Time_Converter(secondsPlayedTotal)]
        ]
    )
    timeWasted.reversesort = True
    print(timeWasted.get_string(sortby='Last Logged In'))
