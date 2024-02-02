# Thomas McGinley
# Started 1/8/2024
# Last Updated 2/2/2024

# Gathers basic Raid stat information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
import prettytable
from prettytable import PrettyTable
from MillisecondTimeConverter import convert

def getMetricData(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1100"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }
    response = requests.request("GET",url, headers=headers, data=payload)
    metricData = json.loads(response.content)
    return metricData


def raidDictionary():
    dictionary = {
        "Crota's End":{"Clears":0, "Fastest":0},
        "Root of Nightmares":{"Clears":0, "Fastest":0},
        "King's Fall":{"Clears":0, "Fastest":0},
        "Vow of the Disciple":{"Clears":0, "Fastest":0},
        "Vault of Glass":{"Clears":0, "Fastest":0},
        "Deep Stone Crypt":{"Clears":0, "Fastest":0},
        "Garden of Salvation":{"Clears":0, "Fastest":0},
        "Last Wish":{"Clears":0, "Fastest":0},
        "Crown of Sorrow":{"Clears":0, "Fastest":0},
        "Scourge of the Past":{"Clears":0, "Fastest":0},
        "Spire of Stars":{"Clears":0, "Fastest":0, "Prestige":0},
        "Eater of Worlds":{"Clears":0, "Fastest":0, "Prestige":0},
        "Leviathan":{"Clears":0, "Fastest":0, "Prestige":0}  
    }
    return dictionary


def cleanRaidData(metricData):
    raidDict = raidDictionary()
    
    raidDict["Crota's End"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['2552956848']["objectiveProgress"]['progress']
    raidDict["Crota's End"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['510466839']["objectiveProgress"]['progress'])
    
    raidDict["Root of Nightmares"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['321051454']["objectiveProgress"]['progress']
    raidDict["Root of Nightmares"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['58319253']["objectiveProgress"]['progress'])
    
    raidDict["King's Fall"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['1624029217']["objectiveProgress"]['progress']
    raidDict["King's Fall"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['399420098']["objectiveProgress"]['progress'])
    
    raidDict["Vow of the Disciple"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['3585185883']["objectiveProgress"]['progress']
    raidDict["Vow of the Disciple"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['3775579868']["objectiveProgress"]['progress'])
    
    raidDict["Vault of Glass"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['2506886274']["objectiveProgress"]['progress']
    raidDict["Vault of Glass"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['905219689']["objectiveProgress"]['progress'])
    
    raidDict["Deep Stone Crypt"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['954805812']["objectiveProgress"]['progress']
    raidDict["Deep Stone Crypt"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['3679202587']["objectiveProgress"]['progress'])
    
    raidDict["Garden of Salvation"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['1168279855']["objectiveProgress"]['progress']
    raidDict["Garden of Salvation"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['1835852368']["objectiveProgress"]['progress'])
    
    raidDict["Last Wish"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['905240985']["objectiveProgress"]['progress']
    raidDict["Last Wish"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['4164362538']["objectiveProgress"]['progress'])
    
    raidDict["Crown of Sorrow"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['1815425870']["objectiveProgress"]['progress']
    raidDict["Crown of Sorrow"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['996516677']["objectiveProgress"]['progress'])
    
    raidDict["Scourge of the Past"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['1201631538']["objectiveProgress"]['progress']
    raidDict["Scourge of the Past"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['1245368441']["objectiveProgress"]['progress'])
    
    raidDict["Spire of Stars"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['700051716']["objectiveProgress"]['progress']
    raidDict["Spire of Stars"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['2842037131']["objectiveProgress"]['progress'])
    raidDict["Spire of Stars"]["Prestige"] = metricData["Response"]['metrics']['data']['metrics']['3070318724']["objectiveProgress"]['progress']
    
    raidDict["Eater of Worlds"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['2659534585']["objectiveProgress"]['progress']
    raidDict["Eater of Worlds"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['1275208010']["objectiveProgress"]['progress'])
    raidDict["Eater of Worlds"]["Prestige"] = metricData["Response"]['metrics']['data']['metrics']['3284024615']["objectiveProgress"]['progress']
    
    raidDict["Leviathan"]["Clears"] = metricData["Response"]['metrics']['data']['metrics']['2486745106']["objectiveProgress"]['progress']
    raidDict["Leviathan"]["Fastest"] = convert(metricData["Response"]['metrics']['data']['metrics']['3434325913']["objectiveProgress"]['progress'])
    raidDict["Leviathan"]["Prestige"] = metricData["Response"]['metrics']['data']['metrics']['1130423918']["objectiveProgress"]['progress']
    
    return raidDict


def generateHTML(raidData):
    table = PrettyTable()
    table.field_names = ["Stat","Value"]
    table.add_row(["Current Raids", " "])
    table.add_row(["Crota's End", " "])
    table.add_row(["Clears", raidData["Crota's End"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Crota's End"]["Fastest"]])
    
    table.add_row(["Root of Nightmares", " "])
    table.add_row(["Clears", raidData["Root of Nightmares"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Root of Nightmares"]["Fastest"]])
    
    table.add_row(["King's Fall", " "])
    table.add_row(["Clears", raidData["King's Fall"]["Clears"]])
    table.add_row(["Fastest Time", raidData["King's Fall"]["Fastest"]])
    
    table.add_row(["Vow of the Disciple", " "])
    table.add_row(["Clears", raidData["Vow of the Disciple"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Vow of the Disciple"]["Fastest"]])
    
    table.add_row(["Vault of Glass", " "])
    table.add_row(["Clears", raidData["Vault of Glass"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Vault of Glass"]["Fastest"]])
    
    table.add_row(["Deep Stone Crypt", " "])
    table.add_row(["Clears", raidData["Deep Stone Crypt"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Deep Stone Crypt"]["Fastest"]])
    
    table.add_row(["Garden of Salvation", " "])
    table.add_row(["Clears", raidData["Garden of Salvation"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Garden of Salvation"]["Fastest"]])
    
    table.add_row(["Last Wish", " "])
    table.add_row(["Clears", raidData["Last Wish"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Last Wish"]["Fastest"]])
    
    table.add_row(["Legacy Raids", " "])
    
    table.add_row(["Crown of Sorrow", " "])
    table.add_row(["Clears", raidData["Crown of Sorrow"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Crown of Sorrow"]["Fastest"]])
    
    table.add_row(["Scourge of the Past", " "])
    table.add_row(["Clears", raidData["Scourge of the Past"]["Clears"]])
    table.add_row(["Fastest Time", raidData["Scourge of the Past"]["Fastest"]])
    
    table.add_row(["Spire of Stars", " "])
    table.add_row(["Clears", raidData["Spire of Stars"]["Clears"]])
    table.add_row(["Prestige Clears", raidData["Spire of Stars"]["Prestige"]])
    table.add_row(["Fastest Time", raidData["Spire of Stars"]["Fastest"]])
    
    table.add_row(["Eater of Worlds", " "])
    table.add_row(["Clears", raidData["Eater of Worlds"]["Clears"]])
    table.add_row(["Prestige Clears", raidData["Eater of Worlds"]["Prestige"]])
    table.add_row(["Fastest Time", raidData["Eater of Worlds"]["Fastest"]])
    
    table.add_row(["Leviathan", " "])
    table.add_row(["Clears", raidData["Leviathan"]["Clears"]])
    table.add_row(["Prestige Clears", raidData["Leviathan"]["Prestige"]])
    table.add_row(["Fastest Time", raidData["Leviathan"]["Fastest"]])
    
    return table.get_html_string()


def writeToDirectory(data,name):
    f = open(f'./data/{name}Raid.html', 'w')
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
    tbody>tr:nth-child(2),
    tbody>tr:nth-child(5),
    tbody>tr:nth-child(8),
    tbody>tr:nth-child(11),
    tbody>tr:nth-child(14),
    tbody>tr:nth-child(17),
    tbody>tr:nth-child(20),
    tbody>tr:nth-child(23),
    tbody>tr:nth-child(27),
    tbody>tr:nth-child(30),
    tbody>tr:nth-child(33),
    tbody>tr:nth-child(37),
    tbody>tr:nth-child(41) {
        font-weight:bold;
        font-size:larger;
        background-color:mediumpurple;
        color:white;
    }
    tbody>tr:nth-child(1),
    tbody>tr:nth-child(26) {
        font-weight:bold;
        font-size:larger;
        background-color: steelblue;
        color:white;
    }
</style>
<h1>RAIDS</h1>
    ''')
    f.write(data)
    f.close()
    print(f"{name} raid data written!")
    
    
def processPlayer(name, memType, memId):
    rawData = getMetricData(memType, memId)
    cleanData = cleanRaidData(rawData)
    htmlString = generateHTML(cleanData)
    writeToDirectory(htmlString,name)
    return cleanData
    
     
def processClan(playerDataList):
    raidDict = raidDictionary()
    for player in playerDataList:
        raidDict["Crota's End"]["Clears"]  +=  player["Crota's End"]["Clears"]
        
        raidDict["Root of Nightmares"]["Clears"] += player["Root of Nightmares"]["Clears"]
        
        raidDict["King's Fall"]["Clears"]  += player["King's Fall"]["Clears"]
        
        raidDict["Vow of the Disciple"]["Clears"]  += player["Vow of the Disciple"]["Clears"]
        
        raidDict["Vault of Glass"]["Clears"]  += player["Vault of Glass"]["Clears"]
        
        raidDict["Deep Stone Crypt"]["Clears"] += player["Deep Stone Crypt"]["Clears"]
        
        raidDict["Garden of Salvation"]["Clears"]  += player["Garden of Salvation"]["Clears"]
        
        raidDict["Last Wish"]["Clears"] += player["Last Wish"]["Clears"]
        
        raidDict["Crown of Sorrow"]["Clears"]  += player["Crown of Sorrow"]["Clears"]
        
        raidDict["Scourge of the Past"]["Clears"]  += player["Scourge of the Past"]["Clears"]
        
        raidDict["Spire of Stars"]["Clears"] += player["Spire of Stars"]["Clears"]
        raidDict["Spire of Stars"]["Prestige"] += player["Spire of Stars"]["Prestige"]
        
        raidDict["Eater of Worlds"]["Clears"] += player["Eater of Worlds"]["Clears"]
        raidDict["Eater of Worlds"]["Prestige"] +=player["Eater of Worlds"]["Prestige"]
        
        raidDict["Leviathan"]["Clears"] += player["Leviathan"]["Clears"]
        raidDict["Leviathan"]["Prestige"] += player["Leviathan"]["Prestige"]
        
    return generateClanHTML(raidDict)
    
def generateClanHTML(raidData):    
    table = PrettyTable()
    table.field_names = ["Stat","Value"]
    table.add_row(["Current Raids", " "])
    table.add_row(["Crota's End", " "])
    table.add_row(["Clears", raidData["Crota's End"]["Clears"]])
    
    table.add_row(["Root of Nightmares", " "])
    table.add_row(["Clears", raidData["Root of Nightmares"]["Clears"]])
    
    table.add_row(["King's Fall", " "])
    table.add_row(["Clears", raidData["King's Fall"]["Clears"]])
    
    table.add_row(["Vow of the Disciple", " "])
    table.add_row(["Clears", raidData["Vow of the Disciple"]["Clears"]])
    
    table.add_row(["Vault of Glass", " "])
    table.add_row(["Clears", raidData["Vault of Glass"]["Clears"]])
    
    table.add_row(["Deep Stone Crypt", " "])
    table.add_row(["Clears", raidData["Deep Stone Crypt"]["Clears"]])
    
    table.add_row(["Garden of Salvation", " "])
    table.add_row(["Clears", raidData["Garden of Salvation"]["Clears"]])
    
    table.add_row(["Last Wish", " "])
    table.add_row(["Clears", raidData["Last Wish"]["Clears"]])
    
    table.add_row(["Legacy Raids", " "])
    
    table.add_row(["Crown of Sorrow", " "])
    table.add_row(["Clears", raidData["Crown of Sorrow"]["Clears"]])
    
    table.add_row(["Scourge of the Past", " "])
    table.add_row(["Clears", raidData["Scourge of the Past"]["Clears"]])
    
    table.add_row(["Spire of Stars", " "])
    table.add_row(["Clears", raidData["Spire of Stars"]["Clears"]])
    table.add_row(["Prestige Clears", raidData["Spire of Stars"]["Prestige"]])
    
    table.add_row(["Eater of Worlds", " "])
    table.add_row(["Clears", raidData["Eater of Worlds"]["Clears"]])
    table.add_row(["Prestige Clears", raidData["Eater of Worlds"]["Prestige"]])
    
    table.add_row(["Leviathan", " "])
    table.add_row(["Clears", raidData["Leviathan"]["Clears"]])
    table.add_row(["Prestige Clears", raidData["Leviathan"]["Prestige"]])
    
    return table.get_html_string()
    
def writeToClanDirectory(data,name):
    f = open(f'./data/{name}Raid.html', 'w')
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
    tbody>tr:nth-child(2),
    tbody>tr:nth-child(4),
    tbody>tr:nth-child(6),
    tbody>tr:nth-child(8),
    tbody>tr:nth-child(10),
    tbody>tr:nth-child(12),
    tbody>tr:nth-child(14),
    tbody>tr:nth-child(16),
    tbody>tr:nth-child(19),
    tbody>tr:nth-child(21),
    tbody>tr:nth-child(23),
    tbody>tr:nth-child(26),
    tbody>tr:nth-child(29) {
        font-weight:bold;
        font-size:larger;
        background-color:mediumpurple;
        color:white;
    }
    tbody>tr:nth-child(1),
    tbody>tr:nth-child(18) {
        font-weight:bold;
        font-size:larger;
        background-color: steelblue;
        color:white;
    }
</style>
<h1>RAIDS</h1>
    ''')
    f.write(data)
    f.close()
    print(f"{name} raid data written!")
    
thomasData = processPlayer("Thomas", 1,4611686018444441571 )
douglasData = processPlayer("Douglas", 1,4611686018434621591)
markData = processPlayer("Mark",1,4611686018432221111)
connorData = processPlayer("Connor",1,4611686018450697084)
jackData = processPlayer("Jack",2,4611686018469231992)
hunterData = processPlayer("Hunter",3,4611686018476416864)
cameronData = processPlayer("Cameron",3,4611686018501646188)
kadeData = processPlayer("Kade",1,4611686018451886498)
xavierData = processPlayer("Xavier", 3, 4611686018471574419)
playerDataList = [thomasData,douglasData,markData,connorData,jackData,hunterData,cameronData,kadeData, xavierData]
ClanHTML = processClan(playerDataList) 
writeToClanDirectory(name="Clan",data=ClanHTML)