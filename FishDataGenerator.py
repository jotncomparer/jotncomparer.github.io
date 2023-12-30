# Thomas McGinley
# Started 12/28/2023
# Last Updated 12/28/2023

# Gathers fishing stat and good boy protocol information about each desired player, cleans the data, and generates JSON files with relevant information


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


def fishDict():
    dictionary = {
        "Total": 0,
        "Heaviest": 0,
        "Pets": 0,
        "Snowballs":0,
        "Cookies":0,
        "Name": ""
    }
    return dictionary


def cleanFishingData(metricData):
    fishingDictionary = fishDict()
    fishingDictionary["Total"] = metricData["Response"]['metrics']['data']['metrics']['24768693']["objectiveProgress"]['progress']
    fishingDictionary["Heaviest"] = metricData["Response"]['metrics']['data']['metrics']['2691615711']["objectiveProgress"]['progress'] / 100
    fishingDictionary["Pets"] = metricData["Response"]['metrics']['data']['metrics']['3131994725']["objectiveProgress"]['progress']
    fishingDictionary["Snowballs"] = metricData["Response"]['metrics']['data']['metrics']['857713621']["objectiveProgress"]['progress']
    fishingDictionary["Cookies"] = metricData["Response"]['metrics']['data']['metrics']['3597861791']["objectiveProgress"]['progress']

    
    return fishingDictionary


def generateHTML(fishingData, isClan = False):
    table = PrettyTable()
    table.field_names = ["Stat","Value"]
    table.add_row(["Total fish caught", int(fishingData["Total"])])
    table.add_row(["Heaviest fish caught", str(fishingData["Heaviest"])+ " kg" ])
    if isClan:
        table.add_row(["Biggest fish caught by", fishingData["Name"]])
    table.add_row(["Good Boy Protocol activations", int(fishingData["Pets"])])
    table.add_row(["Snowball kills", int(fishingData["Snowballs"])])
    table.add_row(["Cookies baked", int(fishingData["Cookies"])])
    return table.get_html_string()


def writeToDirectory(data,name):
    f = open(f'./data/{name}Fish.html', 'w')
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
</style>
<h1>SILLY CORNER</h1>
    ''')
    f.write(data)
    f.close()
    print(f"{name} fishing data written!")

    
def processPlayer(name, memType, memId):
    rawData = getMetricData(memType, memId)
    fishingData = cleanFishingData(rawData)
    htmlString = generateHTML(fishingData)
    writeToDirectory(htmlString,name)
    fishingData["Name"] = name
    return fishingData
    

def processClan(playerDataList):
    fishingDictionary = fishDict()
    heaviest = 0.0
    for player in playerDataList:
        fishingDictionary["Total"] += player["Total"]
        if player["Heaviest"] > heaviest:
            heaviest = player["Heaviest"]
            fishingDictionary["Heaviest"] = player["Heaviest"]
            fishingDictionary["Name"] = player["Name"]
        fishingDictionary["Pets"] += player["Pets"]
        fishingDictionary["Snowballs"] += player["Snowballs"]
        fishingDictionary["Cookies"] += player["Cookies"]
    return generateHTML(fishingDictionary, True)


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