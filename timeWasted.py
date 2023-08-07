# Connor Downs
# Started: 8-7-2023
# Last Updated: 8-7-2023
# This program needs metricGenerator.py and JOTUNN.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program asks the user which player they wish to investigate time most recently played as well as amount of total
# time played.

def timeWasted(player):
    import json
    from Time_Converter import Time_Converter

    with open('Metrics.json') as f:
        data1 = json.load(f)

    items1 = data1["Response"]
    metric_json = {"Response": []}
    metric_json['Response'].append(items1)

    with open('Metrics.json', "w") as f:
        f.write(json.dumps(metric_json, indent=2))

    if player == 1:
        minutesPlayedTotal = 0
        # Connor - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009644414176']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009644414176'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009663894341']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009663894341'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843009703275457']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009703275457'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 2:
        minutesPlayedTotal = 0
        # Thomas - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009283965144']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009283965144'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009265786295']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009265786295'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843009569534739']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009569534739'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 3:
        minutesPlayedTotal = 0
        # Douglas - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009293915719']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009293915719'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009301374530']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009301374530'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843010083874501']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843010083874501'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 4:
        minutesPlayedTotal = 0
        # Mark - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009668854600']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009668854600'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009802904121']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009802904121'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843009348154555']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009348154555'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 5:
        minutesPlayedTotal = 0
        # Jack - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009890274343']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009890274343'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009891864023']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009891864023'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843009268771475']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009268771475'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 6:
        minutesPlayedTotal = 0
        # Hunter - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009756404411']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009756404411'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009359365362']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009359365362'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843009359734078']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009359734078'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 7:
        minutesPlayedTotal = 0
        # Cameron - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009624174508']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009624174508'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009683284493']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009683284493'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843009683284492']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009683284492'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
    if player == 8:
        minutesPlayedTotal = 0
        # Kade - Titan
        dateLastPlayedTitan = metric_json["Response"][0]["characters"]['data']['2305843009264637527']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009264637527'][
                                      'minutesPlayedTotal'])
        # Warlock
        dateLastPlayedWar = metric_json["Response"][0]["characters"]['data']['2305843009264637524']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843009264637524'][
                                      'minutesPlayedTotal'])
        # Hunter
        dateLastPlayedHunter = metric_json["Response"][0]["characters"]['data']['2305843010322954573']['dateLastPlayed']
        minutesPlayedTotal += int(metric_json["Response"][0]["characters"]['data']['2305843010322954573'][
                                      'minutesPlayedTotal'])
        secondsPlayedTotal = minutesPlayedTotal * 60
        print(Time_Converter(secondsPlayedTotal))
        compareOne = dateLastPlayedTitan > dateLastPlayedWar
        compareTwo = dateLastPlayedWar > dateLastPlayedHunter
        if compareOne == True and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == True and compareTwo == False:
            print(f'Date Last Played: {dateLastPlayedTitan}')
        elif compareOne == False and compareTwo == True:
            print(f'Date Last Played: {dateLastPlayedWar}')
        else:
            print(f'Date Last Played: {dateLastPlayedHunter}')
