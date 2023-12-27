import requests
import json
import prettytable
from prettytable import PrettyTable

def elementData():
    dictionary = {
        "Total":0,
        "Solar": 0,
        "Arc": 0,
        "Void": 0,
        "Stasis": 0,
        "Strand": 0
    }
    return dictionary

def cleanElementData(metricData):
    elementDictionary = elementData()
    elementDictionary["Total"]=metricData["Response"]['metrics']['data']['metrics']['2537844000']['objectiveProgress']['progress']
    elementDictionary["Solar"]=metricData["Response"]['metrics']['data']['metrics']['2187143539']['objectiveProgress']['progress']
    elementDictionary["Arc"]=metricData["Response"]['metrics']['data']['metrics']['1513312460']['objectiveProgress']['progress']
    elementDictionary["Void"]=metricData["Response"]['metrics']['data']['metrics']['2327589890']['objectiveProgress']['progress']
    elementDictionary["Stasis"]=metricData["Response"]['metrics']['data']['metrics']['2464463405']['objectiveProgress']['progress']
    elementDictionary["Strand"]=metricData["Response"]['metrics']['data']['metrics']['2889561660']['objectiveProgress']['progress']
    return elementDictionary

def getMetricData(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1100"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }
    response = requests.request("GET",url, headers=headers, data=payload)
    metricData = json.loads(response.content)
    return metricData

def generateHTML(elementData):
    table = PrettyTable()
    table.field_names = ["Element", "Kills"]
    for element in elementData:
        kills = int(elementData[element])
        table.add_row([element,kills])
    return table.get_html_string()
    
    
def writeToDirectory(data,name):
    f = open(f'./data/{name}Elements.html', 'w')
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
    tbody>tr:nth-of-type(2) {
        background-color: orange;
        color:black 
    }
    tbody>tr:nth-of-type(3) {
       background-color: skyblue;
       color:black
    }
    tbody>tr:nth-of-type(4) {
        background-color: blueviolet;
    }
    tbody>tr:nth-of-type(5) {
        background-color: blue;
    }
    tbody>tr:nth-of-type(6) {
        background-color: lime;
        color:black
    }
</style>
<h1>FINAL BLOWS</h1>
<h2>Total final blows: Career</h2>
<h2>Elemental final blows: This season</h2>    
    ''')
    f.write(data)
    f.close()
    print(f"{name} elemental data written!")

def processPlayer(name, memType, memId):
    rawData = getMetricData(memType, memId)
    elementData = cleanElementData(rawData)
    htmlString = generateHTML(elementData)
    writeToDirectory(htmlString,name)
    return elementData

def processClan(playerDataList):
    elementDictionary = elementData()
    for player in playerDataList:
        elementDictionary["Total"] += player["Total"]
        elementDictionary["Solar"] += player["Solar"]
        elementDictionary["Arc"] += player["Arc"]
        elementDictionary["Void"] += player["Void"]
        elementDictionary["Stasis"] += player["Stasis"]
        elementDictionary["Strand"] += player["Strand"]
    return generateHTML(elementDictionary)

ThomasData = processPlayer("Thomas", 1,4611686018444441571 )
douglasData = processPlayer("Douglas", 1,4611686018434621591)
MarkData = processPlayer("Mark",1,4611686018432221111)
ConnorData = processPlayer("Connor",1,4611686018450697084)
JackData = processPlayer("Jack",2,4611686018469231992)
HunterData = processPlayer("Hunter",3,4611686018476416864)
CameronData = processPlayer("Cameron",3,4611686018501646188)
KadeData = processPlayer("Kade",1,4611686018451886498)
playerDataList = [ThomasData,douglasData,MarkData,ConnorData,JackData,HunterData,CameronData,KadeData]
ClanHTML = processClan(playerDataList)
writeToDirectory(ClanHTML,"Clan")