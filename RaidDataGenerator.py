# Thomas McGinley
# Started 1/8/2024
# Last Updated 2/9/2024

# Gathers basic Raid stat information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
from prettytable import PrettyTable
from MillisecondTimeConverter import convert

def get_metric_data(mem_type, mem_id):
    url = f"https://www.bungie.net/Platform/Destiny2/{mem_type}/Profile/{mem_id}/?components=1100"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }
    response = requests.request("GET",url, headers=headers, data=payload)
    if response != 200:
            print("Error occurred in request:", response)
            print("She be Rhulking on my Disciple til I Strand")
    data = json.loads(response.content)
    return data


def raid_dictionary():
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


def clean_raid_data(metric_data):
    raid_dict = raid_dictionary()
    
    raid_dict["Crota's End"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['2552956848']["objectiveProgress"]['progress']
    raid_dict["Crota's End"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['510466839']["objectiveProgress"]['progress'])
    
    raid_dict["Root of Nightmares"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['321051454']["objectiveProgress"]['progress']
    raid_dict["Root of Nightmares"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['58319253']["objectiveProgress"]['progress'])
    
    raid_dict["King's Fall"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['1624029217']["objectiveProgress"]['progress']
    raid_dict["King's Fall"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['399420098']["objectiveProgress"]['progress'])
    
    raid_dict["Vow of the Disciple"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['3585185883']["objectiveProgress"]['progress']
    raid_dict["Vow of the Disciple"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['3775579868']["objectiveProgress"]['progress'])
    
    raid_dict["Vault of Glass"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['2506886274']["objectiveProgress"]['progress']
    raid_dict["Vault of Glass"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['905219689']["objectiveProgress"]['progress'])
    
    raid_dict["Deep Stone Crypt"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['954805812']["objectiveProgress"]['progress']
    raid_dict["Deep Stone Crypt"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['3679202587']["objectiveProgress"]['progress'])
    
    raid_dict["Garden of Salvation"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['1168279855']["objectiveProgress"]['progress']
    raid_dict["Garden of Salvation"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['1835852368']["objectiveProgress"]['progress'])
    
    raid_dict["Last Wish"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['905240985']["objectiveProgress"]['progress']
    raid_dict["Last Wish"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['4164362538']["objectiveProgress"]['progress'])
    
    raid_dict["Crown of Sorrow"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['1815425870']["objectiveProgress"]['progress']
    raid_dict["Crown of Sorrow"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['996516677']["objectiveProgress"]['progress'])
    
    raid_dict["Scourge of the Past"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['1201631538']["objectiveProgress"]['progress']
    raid_dict["Scourge of the Past"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['1245368441']["objectiveProgress"]['progress'])
    
    raid_dict["Spire of Stars"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['700051716']["objectiveProgress"]['progress']
    raid_dict["Spire of Stars"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['2842037131']["objectiveProgress"]['progress'])
    raid_dict["Spire of Stars"]["Prestige"] = metric_data["Response"]['metrics']['data']['metrics']['3070318724']["objectiveProgress"]['progress']
    
    raid_dict["Eater of Worlds"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['2659534585']["objectiveProgress"]['progress']
    raid_dict["Eater of Worlds"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['1275208010']["objectiveProgress"]['progress'])
    raid_dict["Eater of Worlds"]["Prestige"] = metric_data["Response"]['metrics']['data']['metrics']['3284024615']["objectiveProgress"]['progress']
    
    raid_dict["Leviathan"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['2486745106']["objectiveProgress"]['progress']
    raid_dict["Leviathan"]["Fastest"] = convert(metric_data["Response"]['metrics']['data']['metrics']['3434325913']["objectiveProgress"]['progress'])
    raid_dict["Leviathan"]["Prestige"] = metric_data["Response"]['metrics']['data']['metrics']['1130423918']["objectiveProgress"]['progress']
    
    return raid_dict


def generate_html(raid_data):
    table = PrettyTable()
    table.field_names = ["Stat","Value"]
    table.add_row(["Current Raids", " "])
    table.add_row(["Crota's End", " "])
    table.add_row(["Clears", raid_data["Crota's End"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Crota's End"]["Fastest"]])
    
    table.add_row(["Root of Nightmares", " "])
    table.add_row(["Clears", raid_data["Root of Nightmares"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Root of Nightmares"]["Fastest"]])
    
    table.add_row(["King's Fall", " "])
    table.add_row(["Clears", raid_data["King's Fall"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["King's Fall"]["Fastest"]])
    
    table.add_row(["Vow of the Disciple", " "])
    table.add_row(["Clears", raid_data["Vow of the Disciple"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Vow of the Disciple"]["Fastest"]])
    
    table.add_row(["Vault of Glass", " "])
    table.add_row(["Clears", raid_data["Vault of Glass"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Vault of Glass"]["Fastest"]])
    
    table.add_row(["Deep Stone Crypt", " "])
    table.add_row(["Clears", raid_data["Deep Stone Crypt"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Deep Stone Crypt"]["Fastest"]])
    
    table.add_row(["Garden of Salvation", " "])
    table.add_row(["Clears", raid_data["Garden of Salvation"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Garden of Salvation"]["Fastest"]])
    
    table.add_row(["Last Wish", " "])
    table.add_row(["Clears", raid_data["Last Wish"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Last Wish"]["Fastest"]])
    
    table.add_row(["Legacy Raids", " "])
    
    table.add_row(["Crown of Sorrow", " "])
    table.add_row(["Clears", raid_data["Crown of Sorrow"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Crown of Sorrow"]["Fastest"]])
    
    table.add_row(["Scourge of the Past", " "])
    table.add_row(["Clears", raid_data["Scourge of the Past"]["Clears"]])
    table.add_row(["Fastest Time", raid_data["Scourge of the Past"]["Fastest"]])
    
    table.add_row(["Spire of Stars", " "])
    table.add_row(["Clears", raid_data["Spire of Stars"]["Clears"]])
    table.add_row(["Prestige Clears", raid_data["Spire of Stars"]["Prestige"]])
    table.add_row(["Fastest Time", raid_data["Spire of Stars"]["Fastest"]])
    
    table.add_row(["Eater of Worlds", " "])
    table.add_row(["Clears", raid_data["Eater of Worlds"]["Clears"]])
    table.add_row(["Prestige Clears", raid_data["Eater of Worlds"]["Prestige"]])
    table.add_row(["Fastest Time", raid_data["Eater of Worlds"]["Fastest"]])
    
    table.add_row(["Leviathan", " "])
    table.add_row(["Clears", raid_data["Leviathan"]["Clears"]])
    table.add_row(["Prestige Clears", raid_data["Leviathan"]["Prestige"]])
    table.add_row(["Fastest Time", raid_data["Leviathan"]["Fastest"]])
    
    return table.get_html_string()


def write_to_directory(data,name):
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
    
    
def process_player(name, mem_type, mem_id):
    raw_data = get_metric_data(mem_type, mem_id)
    clean_data = clean_raid_data(raw_data)
    html_string = generate_html(clean_data)
    write_to_directory(html_string,name)
    return clean_data
    
     
def process_clan(player_data_list):
    raid_dict = raid_dictionary()
    for player in player_data_list:
        raid_dict["Crota's End"]["Clears"]  +=  player["Crota's End"]["Clears"]
        
        raid_dict["Root of Nightmares"]["Clears"] += player["Root of Nightmares"]["Clears"]
        
        raid_dict["King's Fall"]["Clears"]  += player["King's Fall"]["Clears"]
        
        raid_dict["Vow of the Disciple"]["Clears"]  += player["Vow of the Disciple"]["Clears"]
        
        raid_dict["Vault of Glass"]["Clears"]  += player["Vault of Glass"]["Clears"]
        
        raid_dict["Deep Stone Crypt"]["Clears"] += player["Deep Stone Crypt"]["Clears"]
        
        raid_dict["Garden of Salvation"]["Clears"]  += player["Garden of Salvation"]["Clears"]
        
        raid_dict["Last Wish"]["Clears"] += player["Last Wish"]["Clears"]
        
        raid_dict["Crown of Sorrow"]["Clears"]  += player["Crown of Sorrow"]["Clears"]
        
        raid_dict["Scourge of the Past"]["Clears"]  += player["Scourge of the Past"]["Clears"]
        
        raid_dict["Spire of Stars"]["Clears"] += player["Spire of Stars"]["Clears"]
        raid_dict["Spire of Stars"]["Prestige"] += player["Spire of Stars"]["Prestige"]
        
        raid_dict["Eater of Worlds"]["Clears"] += player["Eater of Worlds"]["Clears"]
        raid_dict["Eater of Worlds"]["Prestige"] +=player["Eater of Worlds"]["Prestige"]
        
        raid_dict["Leviathan"]["Clears"] += player["Leviathan"]["Clears"]
        raid_dict["Leviathan"]["Prestige"] += player["Leviathan"]["Prestige"]
        
    return generate_clan_html(raid_dict)
    
def generate_clan_html(raidData):    
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
    
def write_to_clan_directory(data,name):
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

def run():    
    thomasData = process_player("Thomas", 1,4611686018444441571 )
    douglasData = process_player("Douglas", 1,4611686018434621591)
    markData = process_player("Mark",1,4611686018432221111)
    connorData = process_player("Connor",1,4611686018450697084)
    jackData = process_player("Jack",2,4611686018469231992)
    hunterData = process_player("Hunter",3,4611686018476416864)
    cameronData = process_player("Cameron",3,4611686018501646188)
    kadeData = process_player("Kade",1,4611686018451886498)
    xavierData = process_player("Xavier", 3, 4611686018471574419)
    playerDataList = [thomasData,douglasData,markData,connorData,jackData,hunterData,cameronData,kadeData, xavierData]
    
def compile_clan(player_data_list):
    ClanHTML = process_clan(player_data_list) 
    write_to_clan_directory(name="Clan",data=ClanHTML)