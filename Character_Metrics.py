# Connor Downs
# Started: 7-31-2023
# Last Updated: 8-7-2023
# This program needs metricGenerator.py and JOTUNN.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program asks the user which player (or all) they wish to investigate several statistics that can be measured.
# This program specifically looks to three areas of interest, character data, triumph data, and metric data

def Character_Metrics():
    from metricGenerator import metricGenerator
    from profileData import profileData
    from recordsData import recordsData
    from metricsData import metricsData
    from commendationData import commendationData
    import json
    import requests

    def API_URL(membershipType, destinyMembershipId):
        url = f"https://www.bungie.net/Platform/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200," \
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

    print("Players: Connor, Thomas, Douglas, Hunter, Mark, Jack, Cameron, Kade")
    print("Player Name: Man in the Moon, The Chrome Leaf, Piepuns, Lachlan, TheZefraOracle, HeavyChevy, SlayWarsV, "
          "Gargoyle Goose")
    USER = input("Please type a player or player name from the above lists to analyse: ")

    if USER == "Man in the Moon" or USER == "Connor":
        Man_in_the_Moon()
    elif USER == "The Chrome Leaf" or USER == "Thomas":
        The_Chrome_Leaf()
    elif USER == "Piepuns" or USER == "Douglas":
        Piepuns()
    elif USER == "TheZefraOracle" or USER == "Mark":
        TheZefraOracle()
    elif USER == "HeavyChevy" or USER == "Jack":
        HeavyChevy()
    elif USER == "Lachlan" or USER == "Hunter":
        Lachlan()
    elif USER == "SlayWarsV" or USER == "Cameron":
        SlayWarsV()
    elif USER == "Gargoyle Goose" or USER == "Kade":
        Gargoyle_Goose()
    else:
        print("She be Rhulking on my Disciple til I Strand.")

    print('Triumph Data (1), Title Data (2), Metric Data (3), Commendation Score (4), All (5)')
    typeData = input("Please indicate which data group to be reported: ")

    if typeData == "1":
        profileData()
    elif typeData == "2":
        recordsData()
    elif typeData == '3':
        metricsData()
    elif typeData == '4':
        commendationData()
    elif typeData == '5':
        metricGenerator()
    else:
        print("She be Rhulking on my Disciple til I Strand.")
