# Thomas McGinley
# Started 1/1/2024
# Last Updated 1/1/2024

# Gathers weapon type kills information about each desired player, cleans the data, and generates HTML files with relevant information


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


def weaponDictionary():
    dictionary = {
        "Auto Rifle": 0,
        "Pulse Rifle": 0,
        "Scout Rifle": 0,
        "Hand Cannon": 0,
        "Sidearm": 0,
        "Submachine Gun": 0,
        "Bow": 0,
        "Trace Rifle": 0,
        "Fusion Rifle": 0,
        "Shotgun": 0,
        "Sniper Rifle": 0,
        "Grenade Launcher": 0,
        "Rocket Launcher": 0,
        "Sword": 0,
        "Linear Fusion Rifle": 0,
        "Machine Gun": 0
    }
    return dictionary


def cleanWeaponData(metricData):
    weaponDict = weaponDictionary()
    
    weaponDict["Auto Rifle"] = metricData["Response"]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
    weaponDict["Pulse Rifle"] = metricData["Response"]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
    weaponDict["Scout Rifle"] = metricData["Response"]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
    weaponDict["Hand Cannon"] = metricData["Response"]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
    weaponDict["Sidearm"] = metricData["Response"]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
    weaponDict["Submachine Gun"] = metricData["Response"]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
    weaponDict["Bow"] = metricData["Response"]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
    weaponDict["Trace Rifle"] = metricData["Response"]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
    weaponDict["Fusion Rifle"] = metricData["Response"]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
    weaponDict["Shotgun"] = metricData["Response"]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
    weaponDict["Sniper Rifle"] = metricData["Response"]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
    weaponDict["Grenade Launcher"] = metricData["Response"]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
    weaponDict["Rocket Launcher"] = metricData["Response"]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
    weaponDict["Sword"] = metricData["Response"]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
    weaponDict["Linear Fusion Rifle"] = metricData["Response"]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
    weaponDict["Machine Gun"] = metricData["Response"]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']
    
    return weaponDict


def generateHTML(weaponData):
    table = PrettyTable()
    table.field_names = ["Weapon Type", "Kills"]
    for weaponType in weaponData:
        table.add_row([weaponType,weaponData[weaponType]])
    table.sortby = "Kills"
    table.reversesort = True
    return table.get_html_string()


def writeToDirectory(data,name):
    f = open(f'./data/{name}Weapons.html', 'w')
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
</style>
<h1>WEAPONS</h1>
    ''')
    f.write(data)
    f.close()
    print(f"{name} weapon data written!")
    
    
def processPlayer(name, memType, memId):
    rawData = getMetricData(memType, memId)
    cleanData = cleanWeaponData(rawData)
    htmlString = generateHTML(cleanData)
    writeToDirectory(htmlString,name)
    return cleanData


def processClan(playerDataList):
    weaponDict = weaponDictionary()
    for player in playerDataList:
        weaponDict["Auto Rifle"] += player["Auto Rifle"]
        weaponDict["Pulse Rifle"] += player["Pulse Rifle"]
        weaponDict["Scout Rifle"] += player["Scout Rifle"]
        weaponDict["Hand Cannon"] += player["Hand Cannon"]
        weaponDict["Sidearm"] += player["Sidearm"]
        weaponDict["Submachine Gun"] += player["Submachine Gun"]
        weaponDict["Bow"] += player["Bow"]
        weaponDict["Trace Rifle"] += player["Trace Rifle"]
        weaponDict["Fusion Rifle"] += player["Fusion Rifle"]
        weaponDict["Shotgun"] += player["Shotgun"]
        weaponDict["Sniper Rifle"] += player["Sniper Rifle"]
        weaponDict["Grenade Launcher"] += player["Grenade Launcher"]
        weaponDict["Rocket Launcher"] += player["Rocket Launcher"]
        weaponDict["Sword"] += player["Sword"]
        weaponDict["Linear Fusion Rifle"] += player["Linear Fusion Rifle"]
        weaponDict["Machine Gun"] += player["Machine Gun"]
    return generateHTML(weaponDict)


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