# Thomas McGinley
# Started 1/14/2024
# Last Updated 1/14/2024

# Gathers basic commendation information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
from prettytable import PrettyTable


def getCommendationData(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1400"
    payload = {}
    headers = {
        "x-api-key": "654dad1171c44eb688f2fb5ca11e7c3b",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    metricData = json.loads(response.content)
    return metricData


def commendationDictionary():
    dictionary = {
        "Total": 0,
        
        "Ally": {"Score": 0, "Percent": 0},
        "Indispensable": 0,
        "Selfless": 0,
        "Thoughtful": 0,
        "Patient And Considerate": 0,
        
        "Fun": {"Score": 0, "Percent": 0},
        "Joy Bringer": 0,
        "Level-Headed": 0,
        "Saint's Favorite": 0,
        "Best Dressed": 0,
        
        "Mastery": {"Score": 0, "Percent": 0},
        "Playmaker": 0,
        "Primeval Instinct": 0,
        "Heroic": 0,
        "Pacesetter": 0,
        
        "Leadership": {"Score": 0, "Percent": 0},
        "Perceptive": 0,
        "Knowledgeable": 0
    }
    return dictionary


def cleanData(commData):
    commDict = commendationDictionary()
    commDict["Total"] = commData["Response"]['profileCommendations']['data']['totalScore']
    
    commDict["Ally"]["Score"] = commData["Response"]['profileCommendations']['data']['commendationNodeScoresByHash']['154475713']
    commDict["Ally"]["Percent"] = commData["Response"]['profileCommendations']['data']['commendationNodePercentagesByHash']['154475713']
    commDict["Indispensable"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['2019871317']
    commDict["Selfless"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['354527503']
    commDict["Thoughtful"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3513056018']
    commDict["Patient And Considerate"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['2506835299']

    commDict["Fun"]["Score"] = commData["Response"]['profileCommendations']['data']['commendationNodeScoresByHash']['1341823550']
    commDict["Fun"]["Percent"] = commData["Response"]['profileCommendations']['data']['commendationNodePercentagesByHash']['1341823550']
    commDict["Joy Bringer"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3377580220']
    commDict["Level-Headed"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3037314846']
    commDict["Saint's Favorite"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3030493827']
    commDict["Best Dressed"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['357212819']

    commDict["Mastery"]["Score"] = commData["Response"]['profileCommendations']['data']['commendationNodeScoresByHash']['4180748446']
    commDict["Mastery"]["Percent"] = commData["Response"]['profileCommendations']['data']['commendationNodePercentagesByHash']['1390663518']
    commDict["Playmaker"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['4209356036']
    commDict["Primeval Instinct"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['363818544']
    commDict["Heroic"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3575743922']
    commDict["Pacesetter"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['2205006002']


    commDict["Leadership"]["Score"] = commData["Response"]['profileCommendations']['data']['commendationNodeScoresByHash']['1390663518']
    commDict["Leadership"]["Percent"] = commData["Response"]['profileCommendations']['data']['commendationNodePercentagesByHash']['4180748446']
    commDict["Perceptive"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3872064891']
    commDict["Knowledgeable"] = commData["Response"]['profileCommendations']['data']['commendationScoresByHash']['3970150545']

    return commDict


def generateTable(cleanData):
    table = PrettyTable()
    table.add_column("Ally", [cleanData["Ally"]["Score"], "Indispensable", "Selfless", "Thoughtful", "Patient And Considerate"])
    table.add_column(" ", [str(cleanData["Ally"]["Percent"]) + "%", cleanData["Indispensable"], cleanData["Selfless"], cleanData["Thoughtful"], cleanData["Patient And Considerate"]])
    
    table.add_column("Fun", [cleanData["Fun"]["Score"], "Joy Bringer", "Level-Headed", "Saint's Favorite", "Best Dressed"])
    table.add_column("  ", [str(cleanData["Fun"]["Percent"]) + "%", cleanData["Joy Bringer"], cleanData["Level-Headed"], cleanData["Saint's Favorite"], cleanData["Best Dressed"]])

    table.add_column("Mastery", [cleanData["Mastery"]["Score"], "Playmaker", "Primeval Instinct", "Heroic", "Pacesetter"])
    table.add_column("   ", [str(cleanData["Mastery"]["Percent"]) + "%", cleanData["Playmaker"], cleanData["Primeval Instinct"], cleanData["Heroic"], cleanData["Pacesetter"]])

    table.add_column("Leadership", [cleanData["Leadership"]["Score"], "Perceptive", "Knowledgeable", " ", " "])
    table.add_column("    ", [str(cleanData["Leadership"]["Percent"]) + "%", cleanData["Perceptive"], cleanData["Knowledgeable"], " ", " "])
    # table.add_row(["Total Commendation Score", cleanData["Total"], "", "", "", "", "", ""])
    return table.get_html_string()
    

def writeToDirectory(data, name, dictionary):
    f = open(f'./data/{name}Commendation.html', 'w')
    f.write('''
    <style>
    h1,
    h2 {
        color: white;
        font-family: 'Courier New', Courier, monospace
    }

    h2 {
        font-size: medium
    }

    table {
        color: white;
        width: 100%;
        text-align: left;
        font-family: 'Courier New', Courier, monospace
    }

    th,
    td {
        border-bottom: 1px solid white
    }

    thead>tr>th:nth-of-type(1),
    thead>tr>th:nth-of-type(2) {
        background-color: mediumspringgreen;
        color: black
    }

    thead>tr>th:nth-of-type(3),
    thead>tr>th:nth-of-type(4) {
        background-color: palevioletred;
        color: black
    }

    thead>tr>th:nth-of-type(5),
    thead>tr>th:nth-of-type(6) {
        background-color: orange;
        color: black
    }

    thead>tr>th:nth-of-type(7),
    thead>tr>th:nth-of-type(8) {
        background-color: cornflowerblue;
        color: black
    }

    tbody>tr:nth-child(2n)>td:nth-of-type(1),
    tbody>tr:nth-child(2n)>td:nth-of-type(2) {
        background-color: rgba(0, 240, 154, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(1),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(2) {
        background-color: rgba(0, 240, 154, .25)
    }

    tbody>tr:nth-child(2n)>td:nth-of-type(3),
    tbody>tr:nth-child(2n)>td:nth-of-type(4) {
        background-color: rgba(219, 112, 147, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(3),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(4) {
        background-color: rgba(219, 112, 147, .25)
    }

    tbody>tr:nth-child(2n)>td:nth-of-type(5),
    tbody>tr:nth-child(2n)>td:nth-of-type(6) {
        background-color: rgba(255, 165, 0, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(5),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(6) {
        background-color: rgba(255, 165, 0, .25)
    }
    
    tbody>tr:nth-child(2n)>td:nth-of-type(7),
    tbody>tr:nth-child(2n)>td:nth-of-type(8) {
        background-color: rgba(100, 149, 237, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(7),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(8) {
        background-color: rgba(100, 149, 237, .25)
    }
</style>
    ''')
    f.write(f'''
<h1>Commendations - Total: {dictionary["Total"]}</h1>
<h2>Resets every season</h2>
    ''')
    f.write(data)
    f.close()
    print(f"{name} commendation data written!")


def processPlayer(name, memType, memId):
    rawData = getCommendationData(memType, memId)
    cleanedData = cleanData(rawData)
    htmlString = generateTable(cleanedData)
    writeToDirectory(htmlString, name, cleanedData)
    return cleanedData


def processClan(playerDataList):
    commDict = commendationDictionary()
    for player in playerDataList:
        commDict["Total"] += player["Total"]
    
        commDict["Ally"]["Score"] += player["Ally"]["Score"]
        #commDict["Ally"]["Percent"] += player["Ally"]["Percent"]
        commDict["Indispensable"] += player["Indispensable"]
        commDict["Selfless"] += player["Selfless"]
        commDict["Thoughtful"] += player["Thoughtful"]
        commDict["Patient And Considerate"] += player["Patient And Considerate"]

        commDict["Fun"]["Score"] += player["Fun"]["Score"]
       #commDict["Fun"]["Percent"] += player["Fun"]["Percent"]
        commDict["Joy Bringer"] += player["Joy Bringer"]
        commDict["Level-Headed"] += player["Level-Headed"]
        commDict["Saint's Favorite"] += player["Saint's Favorite"]
        commDict["Best Dressed"] += player["Best Dressed"]

        commDict["Mastery"]["Score"] += player["Mastery"]["Score"]
        #commDict["Mastery"]["Percent"] += player["Mastery"]["Percent"]
        commDict["Playmaker"] += player["Playmaker"]
        commDict["Primeval Instinct"] += player["Primeval Instinct"]
        commDict["Heroic"] += player["Heroic"]
        commDict["Pacesetter"] += player["Pacesetter"]


        commDict["Leadership"]["Score"] += player["Leadership"]["Score"]
        #commDict["Leadership"]["Percent"] += player["Leadership"]["Percent"]
        commDict["Perceptive"] += player["Perceptive"]
        commDict["Knowledgeable"] += player["Knowledgeable"]
    
    return generateTable(commDict)


thomasData = processPlayer("Thomas", 1, 4611686018444441571)
douglasData = processPlayer("Douglas", 1, 4611686018434621591)
markData = processPlayer("Mark", 1, 4611686018432221111)
connorData = processPlayer("Connor", 1, 4611686018450697084)
jackData = processPlayer("Jack", 2, 4611686018469231992)
hunterData = processPlayer("Hunter", 3, 4611686018476416864)
cameronData = processPlayer("Cameron", 3, 4611686018501646188)
kadeData = processPlayer("Kade", 1, 4611686018451886498)
playerDataList = [thomasData, douglasData, markData, connorData, jackData, hunterData, cameronData, kadeData]
ClanHTML = processClan(playerDataList)
total = 0
for player in playerDataList:
    total += player["Total"]
writeToDirectory(name="Clan", data=ClanHTML, dictionary={"Total":total})
