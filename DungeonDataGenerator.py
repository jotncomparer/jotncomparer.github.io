# Thomas McGinley
# Started 12/29/2023
# Last Updated 12/29/2023

# Gathers basic Dungeon stat information about each desired player, cleans the data, and generates HTML files with relevant information


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

#Add new Dungeons to the front of the dictionary so it displays in reverse chronological order
def dungeonDictionary():
    dictionary = {
        "Warlord's Ruin":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "Ghosts of the Deep":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "Spire of the Watcher":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "Duality":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "Grasp of Avarice":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "Prophecy":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "Pit of Heresy":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
        "The Shattered Throne":{"Clears":0,"Solos":0,"Flawless":0,"Solo Flawless":0},
    }
    return dictionary
    
    
def cleanDungeonData(metricData):
    dungeonDict = dungeonDictionary()
    
    dungeonDict["Warlord's Ruin"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['3932004679']["objectiveProgress"]['progress']
    dungeonDict["Warlord's Ruin"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['3808047795']["objectiveProgress"]['progress']
    dungeonDict["Warlord's Ruin"]["Solo Flawless"] = metricData["Response"]['metrics']['data']['metrics']['3253584750']["objectiveProgress"]['progress']
    
    dungeonDict["Ghosts of the Deep"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['3846201365']["objectiveProgress"]['progress']
    dungeonDict["Ghosts of the Deep"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['3251969937']["objectiveProgress"]['progress']
    dungeonDict["Ghosts of the Deep"]["Solo Flawless"] = metricData["Response"]['metrics']['data']['metrics']['2521923488']["objectiveProgress"]['progress']

    dungeonDict["Spire of the Watcher"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['3702217360']["objectiveProgress"]['progress']
    dungeonDict["Spire of the Watcher"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['4002846192']["objectiveProgress"]['progress']
    dungeonDict["Spire of the Watcher"]["Solo Flawless"] = metricData["Response"]['metrics']['data']['metrics']['411086447']["objectiveProgress"]['progress']

    dungeonDict["Duality"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['3862075762']["objectiveProgress"]['progress']
    dungeonDict["Duality"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['1034442994']["objectiveProgress"]['progress']
    dungeonDict["Duality"]["Solo Flawless"] = metricData["Response"]['metrics']['data']['metrics']['1084707005']["objectiveProgress"]['progress']

    dungeonDict["Grasp of Avarice"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['451157118']["objectiveProgress"]['progress']
    dungeonDict["Grasp of Avarice"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['2269915270']["objectiveProgress"]['progress']
    dungeonDict["Grasp of Avarice"]["Solo Flawless"] = metricData["Response"]['metrics']['data']['metrics']['3765286137']["objectiveProgress"]['progress']

    dungeonDict["Prophecy"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['352659556']["objectiveProgress"]['progress']
    dungeonDict["Prophecy"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['1099614108']["objectiveProgress"]['progress']
    #^^^ not working? ^^^
    dungeonDict["Prophecy"]["Solo Flawless"] =  0#metricData["Response"]['metrics']['data']['metrics']['']["objectiveProgress"]['progress']

    dungeonDict["Pit of Heresy"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['1451729471']["objectiveProgress"]['progress']
    dungeonDict["Pit of Heresy"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['310888283']["objectiveProgress"]['progress']
    dungeonDict["Pit of Heresy"]["Solo Flawless"] = metricData["Response"]['metrics']['data']['metrics']['3741172422']["objectiveProgress"]['progress']

    dungeonDict["The Shattered Throne"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['1339818929']["objectiveProgress"]['progress']
    dungeonDict["The Shattered Throne"]["Flawless"] = metricData["Response"]['metrics']['data']['metrics']['761318885']["objectiveProgress"]['progress']
    dungeonDict["The Shattered Throne"]["Solo Flawless"] = 0 #metricData["Response"]['metrics']['data']['metrics']['']["objectiveProgress"]['progress']
    return dungeonDict
    
    
def generateHTML(dungeonData):
    table = PrettyTable()
    table.field_names = ["Stat", "Value"]
    for dungeon in dungeonData:
        table.add_row([dungeon," "])
        table.add_row(["Clears",dungeonData[dungeon]["Clears"]])
        table.add_row(["Flawless Clears",dungeonData[dungeon]["Flawless"]])
        table.add_row(["Solo Flawless Clears",dungeonData[dungeon]["Solo Flawless"]])
        table.add_row(["---------------------"," "])
        table.add_row([" "," "])
    return table.get_html_string()
    
    
def writeToDirectory(data,name):
    f = open(f'./data/{name}Dungeon.html', 'w')
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
    tbody>tr:nth-child(6n-5) {
        font-weight:bold;
        font-size:larger;
        background-color:orange;
        color:black;
    }
</style>
<h1>DUNGEONS</h1>
<h2>Solo Flawless stats for Prophecy and The Shattered Throne not working yet</h2>
    ''')
    f.write(data)
    f.close()
    print(f"{name} dungeon data written!")
    
    
def processPlayer(name, memType, memId):
    rawData = getMetricData(memType, memId)
    cleanData = cleanDungeonData(rawData)
    htmlString = generateHTML(cleanData)
    writeToDirectory(htmlString,name)
    return cleanData
    
def processClan(playerDataList):
    dungeonDict=dungeonDictionary()
    for player in playerDataList:
        dungeonDict["Warlord's Ruin"]["Clears"] += player["Warlord's Ruin"]["Clears"]
        dungeonDict["Warlord's Ruin"]["Flawless"] += player["Warlord's Ruin"]["Flawless"]
        dungeonDict["Warlord's Ruin"]["Solo Flawless"] += player["Warlord's Ruin"]["Solo Flawless"]
    
        dungeonDict["Ghosts of the Deep"]["Clears"] += player["Ghosts of the Deep"]["Clears"]
        dungeonDict["Ghosts of the Deep"]["Flawless"] += player["Ghosts of the Deep"]["Flawless"]
        dungeonDict["Ghosts of the Deep"]["Solo Flawless"] += player["Ghosts of the Deep"]["Solo Flawless"]
        
        dungeonDict["Spire of the Watcher"]["Clears"] += player["Spire of the Watcher"]["Clears"]
        dungeonDict["Spire of the Watcher"]["Flawless"] += player["Spire of the Watcher"]["Flawless"]
        dungeonDict["Spire of the Watcher"]["Solo Flawless"] += player["Spire of the Watcher"]["Solo Flawless"]
        
        dungeonDict["Duality"]["Clears"] += player["Duality"]["Clears"]
        dungeonDict["Duality"]["Flawless"] += player["Duality"]["Flawless"]
        dungeonDict["Duality"]["Solo Flawless"] += player["Duality"]["Solo Flawless"]
        
        dungeonDict["Grasp of Avarice"]["Clears"] += player["Grasp of Avarice"]["Clears"]
        dungeonDict["Grasp of Avarice"]["Flawless"] += player["Grasp of Avarice"]["Flawless"]
        dungeonDict["Grasp of Avarice"]["Solo Flawless"] += player["Grasp of Avarice"]["Solo Flawless"]
        
        dungeonDict["Prophecy"]["Clears"] += player["Prophecy"]["Clears"]
        dungeonDict["Prophecy"]["Flawless"] += player["Prophecy"]["Flawless"]
        dungeonDict["Prophecy"]["Solo Flawless"] += player["Prophecy"]["Solo Flawless"]
        
        dungeonDict["Pit of Heresy"]["Clears"] += player["Pit of Heresy"]["Clears"]
        dungeonDict["Pit of Heresy"]["Flawless"] += player["Pit of Heresy"]["Flawless"]
        dungeonDict["Pit of Heresy"]["Solo Flawless"] += player["Pit of Heresy"]["Solo Flawless"]
        
        dungeonDict["The Shattered Throne"]["Clears"] += player["The Shattered Throne"]["Clears"]
        dungeonDict["The Shattered Throne"]["Flawless"] += player["The Shattered Throne"]["Flawless"]
        dungeonDict["The Shattered Throne"]["Solo Flawless"] += player["The Shattered Throne"]["Solo Flawless"]
    return generateHTML(dungeonDict)
    
    
    
    
    
    
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
    
    
    
    
    
    
    
    
    
    
    
    