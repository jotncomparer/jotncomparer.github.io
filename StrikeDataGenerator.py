# Thomas McGinley
# Started 1/3/2024
# Last Updated 1/3/2024

# Gathers Strike information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
import prettytable
from prettytable import PrettyTable


def getMetricData(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1100"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }
    response = requests.request("GET",url, headers=headers, data=payload)
    metricData = json.loads(response.content)
    return metricData

def strikeDictionary():
    dictionary = {
        "Completions":0,
        "Flawless":0,
        "Champion Kills":0,
        "Strike Kills This Season":0,
        
        "The Arms Dealer":0,
        "Insight Terminus":0,
        "The Inverted Spire":0,
        "Savathun's Song":0,
        "The Pyramidion":0,
        "Exodus Crash":0,
        "A Garden World":0,
        "Tree of Probabilities":0,
        "Strange Terrain":0,
        "Warden of Nothing":0,
        "Broodhold":0,
        "The Scarlet Keep":0,
        "Lake of Shadows":0,
        "The Corrupted":0,
        "The Festering Core":0,
        "The Disgraced":0,
        "The Glassway":0,
        "Proving Grounds":0,
        "The Devils' Lair":0,
        "Fallen S.A.B.E.R":0,
        "The Hollowed Lair":0,
        "The Lightblade":0,
        "Birthplace of the Vile":0,
    }
    return dictionary


def cleanStrikeData(metricData):
    strikeDict = strikeDictionary()
    
    strikeDict["Completions"] = metricData["Response"]['metrics']['data']['metrics']['793155718']["objectiveProgress"]['progress']
    strikeDict["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['2326329668']["objectiveProgress"]['progress']
    strikeDict["Champion Kills"] = metricData["Response"]['metrics']['data']['metrics']['41075005']["objectiveProgress"]['progress']
    strikeDict["Strike Kills This Season"] = metricData["Response"]['metrics']['data']['metrics']['3857340681']["objectiveProgress"]['progress']
        
    strikeDict["The Arms Dealer"] = metricData["Response"]['metrics']['data']['metrics']['3036740778']["objectiveProgress"]['progress']
    strikeDict["Insight Terminus"] = metricData["Response"]['metrics']['data']['metrics']['3146366866']["objectiveProgress"]['progress']
    strikeDict["The Inverted Spire"] = metricData["Response"]['metrics']['data']['metrics']['3466351705']["objectiveProgress"]['progress']
    strikeDict["Savathun's Song"] = metricData["Response"]['metrics']['data']['metrics']['2894079898']["objectiveProgress"]['progress']
    strikeDict["The Pyramidion"] = metricData["Response"]['metrics']['data']['metrics']['2457392818']["objectiveProgress"]['progress']
    strikeDict["Exodus Crash"] = metricData["Response"]['metrics']['data']['metrics']['1118387860']["objectiveProgress"]['progress']
    strikeDict["A Garden World"] = metricData["Response"]['metrics']['data']['metrics']['3543375894']["objectiveProgress"]['progress']
    strikeDict["Tree of Probabilities"] = metricData["Response"]['metrics']['data']['metrics']['2778406657']["objectiveProgress"]['progress']
    strikeDict["Strange Terrain"] = metricData["Response"]['metrics']['data']['metrics']['40546883']["objectiveProgress"]['progress']
    strikeDict["Warden of Nothing"] = metricData["Response"]['metrics']['data']['metrics']['4140273235']["objectiveProgress"]['progress']
    strikeDict["Broodhold"] = metricData["Response"]['metrics']['data']['metrics']['356508148']["objectiveProgress"]['progress']
    strikeDict["The Scarlet Keep"] = metricData["Response"]['metrics']['data']['metrics']['1666283222']["objectiveProgress"]['progress']
    strikeDict["Lake of Shadows"] = metricData["Response"]['metrics']['data']['metrics']['3139878529']["objectiveProgress"]['progress']
    strikeDict["The Corrupted"] = metricData["Response"]['metrics']['data']['metrics']['2920064672']["objectiveProgress"]['progress']
    strikeDict["The Festering Core"] = metricData["Response"]['metrics']['data']['metrics']['326550718']["objectiveProgress"]['progress']
    strikeDict["The Disgraced"] = metricData["Response"]['metrics']['data']['metrics']['136014172']["objectiveProgress"]['progress']
    strikeDict["The Glassway"] = metricData["Response"]['metrics']['data']['metrics']['2883115929']["objectiveProgress"]['progress']
    strikeDict["Proving Grounds"] = metricData["Response"]['metrics']['data']['metrics']['3209483141']["objectiveProgress"]['progress']
    strikeDict["The Devils' Lair"] = metricData["Response"]['metrics']['data']['metrics']['103014972']["objectiveProgress"]['progress']
    strikeDict["Fallen S.A.B.E.R"] = metricData["Response"]['metrics']['data']['metrics']['2894593528']["objectiveProgress"]['progress']
    strikeDict["The Hollowed Lair"] = metricData["Response"]['metrics']['data']['metrics']['449969041']["objectiveProgress"]['progress']
    strikeDict["The Lightblade"] = metricData["Response"]['metrics']['data']['metrics']['3181525833']["objectiveProgress"]['progress']
    strikeDict["Birthplace of the Vile"] = metricData["Response"]['metrics']['data']['metrics']['1065851514']["objectiveProgress"]['progress']
    
    return strikeDict

def generateHTML(strikeData):
    table = PrettyTable()
    table.field_names = ["Stat","Value"]
    table.add_row(["General Statistics"," "])
    i = 0
    for strike in strikeData:
        table.add_row([strike,strikeData[strike]])
        if i == 3:
            table.add_row(["Strike","High Score"])
        i+=1
    return table.get_html_string()


def generateClanHTML(strikeData):
    table = PrettyTable()
    table.field_names = ["Stat", "Value"]
    table.add_row(["General Statistics"," "])
    table.add_row(["Completions",strikeData["Completions"]])
    table.add_row(["Flawless",strikeData["Flawless"]])
    table.add_row(["Champion Kills",strikeData["Champion Kills"]])
    table.add_row(["Strike Kills This Season",strikeData["Strike Kills This Season"]])
    return table.get_html_string()

    
def writeToDirectory(data,name):
    f = open(f'./data/{name}Strikes.html', 'w')
    f.write('''
    <style>
    h1,h2{
        color: white;
        font-family:'Courier New', Courier, monospace
    }
    h2 {
        font-size:medium
    }
    table {
        color: white;
        width: 100%;
        text-align: left;
        font-family:'Courier New', Courier, monospace
    }
    tbody>tr:nth-child(even) {
        background-color: rgb(50, 50, 50);
    }
    th,
    td {
        border-bottom: 1px solid white
    }
    tbody>tr>td:nth-of-type(2) {
        text-align:end;
    }
     tbody>tr:nth-of-type(1) {
        background-color: blue;
        
        font-weight:bolder;
    }
    tbody>tr:nth-of-type(6) {
        background-color: blue;
        
        font-weight:bolder;
    }
</style>
<h1>STRIKES</h1>
    ''')
    f.write(data)
    f.close()
    print(f"{name} strike data written!")
    
    
def processPlayer(name, memType, memId):
    rawData = getMetricData(memType, memId)
    cleanData = cleanStrikeData(rawData)
    htmlString = generateHTML(cleanData)
    writeToDirectory(htmlString,name)
    return cleanData

    
def processClan(playerDataList):
    strikeDict = strikeDictionary()
    for player in playerDataList:
        strikeDict["Completions"] += player["Completions"] 
        strikeDict["Flawless"] += player["Flawless"]
        strikeDict["Champion Kills"] += player["Champion Kills"]
        strikeDict["Strike Kills This Season"] += player["Strike Kills This Season"]
    return generateClanHTML(strikeDict)
        
        
        


thomasData = processPlayer("Thomas", 1,4611686018444441571 )
douglasData = processPlayer("Douglas", 1,4611686018434621591)
markData = processPlayer("Mark",1,4611686018432221111)
connorData = processPlayer("Connor",1,4611686018450697084)
jackData = processPlayer("Jack",2,4611686018469231992)
hunterData = processPlayer("Hunter",3,4611686018476416864)
cameronData = processPlayer("Cameron",3,4611686018501646188)
kadeData = processPlayer("Kade",1,4611686018451886498)
playerDataList = [thomasData,douglasData,markData,connorData,jackData,hunterData,cameronData,kadeData]
ClanHTML = processClan(playerDataList) 
writeToDirectory(ClanHTML,"Clan")
    
    
    
    