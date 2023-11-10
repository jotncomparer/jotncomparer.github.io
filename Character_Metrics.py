# Connor Downs
# Started: 7-31-2023
# Last Updated: 11-10-2023
# This program needs metricGenerator.py and JOTUNN.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program asks the user which player (or all) they wish to investigate several statistics that can be measured.
# This program specifically looks to three areas of interest, character data, triumph data, and metric data

def Character_Metrics():
    from profileData import profileData
    from recordsData import recordsData
    from metricsData import metricsData
    from commendationData import commendationData
    from timeWasted import timeWasted
    from allProfileData import allProfileData
    from allRecordsData import allRecordsData
    from allMetricsData import allMetricsData
    from allCommendation import allCommendationData
    from allTimeWasted import allTimeWasted
    import json
    import requests
    from random import randrange

    def API_URL(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics.json', 'w')
        writeFile.write(metric_data)

    def API_URL_ONE(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_2.json', 'w')
        writeFile.write(metric_data)

    def API_URL_TWO(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_3.json', 'w')
        writeFile.write(metric_data)

    def API_URL_THREE(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_4.json', 'w')
        writeFile.write(metric_data)

    def API_URL_FOUR(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_5.json', 'w')
        writeFile.write(metric_data)

    def API_URL_FIVE(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_6.json', 'w')
        writeFile.write(metric_data)

    def API_URL_SIX(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_7.json', 'w')
        writeFile.write(metric_data)

    def API_URL_SEVEN(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_8.json', 'w')
        writeFile.write(metric_data)

    def API_URL_EIGHT(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=100,200," \
              f"900,1100,1300,1400"
        payload = {}
        headers = {
            'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response.content.decode('utf-8')
        metric_data = json.dumps(json.loads(response.content), indent=2)
        writeFile = open('Metrics_9.json', 'w')
        writeFile.write(metric_data)

    def Man_in_the_Moon():
        membershipType = 1
        destinyMembershipId = 4611686018450697084
        API_URL(membershipType, destinyMembershipId)

    def The_Chrome_Leaf():
        membershipType = 1
        destinyMembershipId = 4611686018444441571
        API_URL(membershipType, destinyMembershipId)

    def Piepuns():
        membershipType = 1
        destinyMembershipId = 4611686018434621591
        API_URL(membershipType, destinyMembershipId)

    def TheZefraOracle():
        membershipType = 1
        destinyMembershipId = 4611686018432221111
        API_URL(membershipType, destinyMembershipId)

    def HeavyChevy():
        membershipType = 2
        destinyMembershipId = 4611686018469231992
        API_URL(membershipType, destinyMembershipId)

    def Lachlan():
        membershipType = 3
        destinyMembershipId = 4611686018476416864
        API_URL(membershipType, destinyMembershipId)

    def SlayWarsV():
        membershipType = 3
        destinyMembershipId = 4611686018501646188
        API_URL(membershipType, destinyMembershipId)

    def Gargoyle_Goose():
        membershipType = 1
        destinyMembershipId = 4611686018451886498
        API_URL(membershipType, destinyMembershipId)

    def Nozyric():
        membershipType = 1
        destinyMembershipId = 4611686018460052968
        API_URL(membershipType, destinyMembershipId)

    def ALL():
        PLAYER = 0
        while PLAYER < 9:
            # Man in the Moon
            while PLAYER == 0:
                CHAR = 0
                membershipType = 1
                destinyMembershipId = 4611686018450697084
                API_URL(membershipType, destinyMembershipId)
                PLAYER += 1
            # The Chrome Leaf
            while PLAYER == 1:
                CHAR = 0
                membershipType = 1
                destinyMembershipId = 4611686018444441571
                API_URL_ONE(membershipType, destinyMembershipId)
                PLAYER += 1
            # Piepuns
            while PLAYER == 2:
                CHAR = 0
                membershipType = 1
                destinyMembershipId = 4611686018434621591
                API_URL_TWO(membershipType, destinyMembershipId)
                PLAYER += 1
            # TheZefraOracle
            while PLAYER == 3:
                CHAR = 0
                membershipType = 1
                destinyMembershipId = 4611686018432221111
                API_URL_THREE(membershipType, destinyMembershipId)
                PLAYER += 1
            # HeavyChevy
            while PLAYER == 4:
                CHAR = 0
                membershipType = 2
                destinyMembershipId = 4611686018469231992
                API_URL_FOUR(membershipType, destinyMembershipId)
                PLAYER += 1
            # Lachlan
            while PLAYER == 5:
                CHAR = 0
                membershipType = 3
                destinyMembershipId = 4611686018476416864
                API_URL_FIVE(membershipType, destinyMembershipId)
                PLAYER += 1
            # SlayWarsV
            while PLAYER == 6:
                CHAR = 0
                membershipType = 3
                destinyMembershipId = 4611686018501646188
                API_URL_SIX(membershipType, destinyMembershipId)
                PLAYER += 1
            # Gargoyle Goose
            while PLAYER == 7:
                CHAR = 0
                membershipType = 1
                destinyMembershipId = 4611686018451886498
                API_URL_SEVEN(membershipType, destinyMembershipId)
                PLAYER += 1
            # Nozyric
            while PLAYER == 8:
                membershipType = 1
                destinyMembershipId = 4611686018460052968
                API_URL_EIGHT(membershipType, destinyMembershipId)

    print("Players: Connor, Thomas, Douglas, Hunter, Mark, Jack, Cameron, Kade, All")
    print("Player Name: Man in the Moon, The Chrome Leaf, Piepuns, Lachlan, TheZefraOracle, HeavyChevy, SlayWarsV, "
          "Gargoyle Goose, All")
    USER = input("Please type a player or player name from the above lists to analyse: ")

    if USER == "Man in the Moon" or USER == "Connor":
        player = 1
        Man_in_the_Moon()
    elif USER == "The Chrome Leaf" or USER == "Thomas":
        player = 2
        The_Chrome_Leaf()
    elif USER == "Piepuns" or USER == "Douglas":
        player = 3
        Piepuns()
    elif USER == "TheZefraOracle" or USER == "Mark":
        player = 4
        TheZefraOracle()
    elif USER == "HeavyChevy" or USER == "Jack":
        player = 5
        HeavyChevy()
    elif USER == "Lachlan" or USER == "Hunter":
        player = 6
        Lachlan()
    elif USER == "SlayWarsV" or USER == "Cameron":
        player = 7
        SlayWarsV()
    elif USER == "Gargoyle Goose" or USER == "Kade":
        player = 8
        Gargoyle_Goose()
    elif USER == 'Nozyric':
        player = 9
        Nozyric()
    elif USER == 'All':
        ALL()
    else:
        errorNumb = randrange(1, 5)
        if errorNumb == 1:
            print("She be Rhulking on my Disciple til I Strand.")
        elif errorNumb == 2:
            print("The Wish Wall accepts your wish, O' Gooner Mine.")
        elif errorNumb == 3:
            print("Nice try, Shitass.")
        elif errorNumb == 4:
            print("That Savathussy got me acting lightless.")

    print('Triumph Data (1), Title Data (2), Metric Data (3), Commendation Score (4), Time Wasted (5)')
    typeData = input("Please indicate which data group to be reported: ")

    if typeData == "1":
        if USER == 'All':
            allProfileData()
        else:
            profileData()
    elif typeData == "2":
        if USER == 'All':
            allRecordsData()
        else:
            recordsData()
    elif typeData == '3':
        if USER == 'All':
            allMetricsData()
        else:
            metricsData()
    elif typeData == '4':
        if USER == 'All':
            allCommendationData()
        else:
            commendationData()
    elif typeData == '5':
        if USER == 'All':
            allTimeWasted()
        else:
            timeWasted(player)
    else:
        errorNumb = randrange(1, 5)
        if errorNumb == 1:
            print("She be Rhulking on my Disciple til I Strand.")
        elif errorNumb == 2:
            print("The Wish Wall accepts your wish, O' Gooner Mine.")
        elif errorNumb == 3:
            print("Nice try, Shitass.")
        elif errorNumb == 4:
            print("That Savathussy got me acting lightless.")
