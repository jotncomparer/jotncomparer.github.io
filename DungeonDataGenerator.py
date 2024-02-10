# Thomas McGinley
# Started 12/29/2023
# Last Updated 2/9/2024

# Gathers basic Dungeon stat information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
from prettytable import PrettyTable


def get_metric_data(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1100"
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


#Add new Dungeons to the front of the dictionary so it displays in reverse chronological order
def dungeon_dictionary():
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
    
    
def clean_dungeon_data(metric_data):
    dungeon_dict = dungeon_dictionary()
    
    dungeon_dict["Warlord's Ruin"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['3932004679']["objectiveProgress"]['progress']
    dungeon_dict["Warlord's Ruin"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['3808047795']["objectiveProgress"]['progress']
    dungeon_dict["Warlord's Ruin"]["Solo Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['3253584750']["objectiveProgress"]['progress']
    
    dungeon_dict["Ghosts of the Deep"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['3846201365']["objectiveProgress"]['progress']
    dungeon_dict["Ghosts of the Deep"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['3251969937']["objectiveProgress"]['progress']
    dungeon_dict["Ghosts of the Deep"]["Solo Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['2521923488']["objectiveProgress"]['progress']

    dungeon_dict["Spire of the Watcher"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['3702217360']["objectiveProgress"]['progress']
    dungeon_dict["Spire of the Watcher"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['4002846192']["objectiveProgress"]['progress']
    dungeon_dict["Spire of the Watcher"]["Solo Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['411086447']["objectiveProgress"]['progress']

    dungeon_dict["Duality"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['3862075762']["objectiveProgress"]['progress']
    dungeon_dict["Duality"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['1034442994']["objectiveProgress"]['progress']
    dungeon_dict["Duality"]["Solo Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['1084707005']["objectiveProgress"]['progress']

    dungeon_dict["Grasp of Avarice"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['451157118']["objectiveProgress"]['progress']
    dungeon_dict["Grasp of Avarice"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['2269915270']["objectiveProgress"]['progress']
    dungeon_dict["Grasp of Avarice"]["Solo Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['3765286137']["objectiveProgress"]['progress']

    dungeon_dict["Prophecy"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['352659556']["objectiveProgress"]['progress']
    dungeon_dict["Prophecy"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['1099614108']["objectiveProgress"]['progress']
    #^^^ not working on Bungie's end ^^^
    dungeon_dict["Prophecy"]["Solo Flawless"] =  0#metricData["Response"]['metrics']['data']['metrics']['']["objectiveProgress"]['progress']

    dungeon_dict["Pit of Heresy"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['1451729471']["objectiveProgress"]['progress']
    dungeon_dict["Pit of Heresy"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['310888283']["objectiveProgress"]['progress']
    dungeon_dict["Pit of Heresy"]["Solo Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['3741172422']["objectiveProgress"]['progress']

    dungeon_dict["The Shattered Throne"]["Clears"] = metric_data["Response"]['metrics']['data']['metrics']['1339818929']["objectiveProgress"]['progress']
    dungeon_dict["The Shattered Throne"]["Flawless"] = metric_data["Response"]['metrics']['data']['metrics']['761318885']["objectiveProgress"]['progress']
    dungeon_dict["The Shattered Throne"]["Solo Flawless"] = 0 #metricData["Response"]['metrics']['data']['metrics']['']["objectiveProgress"]['progress']
    return dungeon_dict
    
    
def generate_html(dungeon_data):
    table = PrettyTable()
    table.field_names = ["Stat", "Value"]
    for dungeon in dungeon_data:
        table.add_row([dungeon," "])
        table.add_row(["Clears",dungeon_data[dungeon]["Clears"]])
        table.add_row(["Flawless Clears",dungeon_data[dungeon]["Flawless"]])
        table.add_row(["Solo Flawless Clears",dungeon_data[dungeon]["Solo Flawless"]])
    return table.get_html_string()
    
    
def write_to_directory(data,name):
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
    tbody>tr:nth-child(4n-3) {
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
    
    
def process_player(name, mem_type, mem_id):
    raw_data = get_metric_data(mem_type, mem_id)
    clean_data = clean_dungeon_data(raw_data)
    html_string = generate_html(clean_data)
    write_to_directory(html_string,name)
    return clean_data
   
    
def process_clan(player_data_list):
    dungeon_dict=dungeon_dictionary()
    for player in player_data_list:
        dungeon_dict["Warlord's Ruin"]["Clears"] += player["Warlord's Ruin"]["Clears"]
        dungeon_dict["Warlord's Ruin"]["Flawless"] += player["Warlord's Ruin"]["Flawless"]
        dungeon_dict["Warlord's Ruin"]["Solo Flawless"] += player["Warlord's Ruin"]["Solo Flawless"]
    
        dungeon_dict["Ghosts of the Deep"]["Clears"] += player["Ghosts of the Deep"]["Clears"]
        dungeon_dict["Ghosts of the Deep"]["Flawless"] += player["Ghosts of the Deep"]["Flawless"]
        dungeon_dict["Ghosts of the Deep"]["Solo Flawless"] += player["Ghosts of the Deep"]["Solo Flawless"]
        
        dungeon_dict["Spire of the Watcher"]["Clears"] += player["Spire of the Watcher"]["Clears"]
        dungeon_dict["Spire of the Watcher"]["Flawless"] += player["Spire of the Watcher"]["Flawless"]
        dungeon_dict["Spire of the Watcher"]["Solo Flawless"] += player["Spire of the Watcher"]["Solo Flawless"]
        
        dungeon_dict["Duality"]["Clears"] += player["Duality"]["Clears"]
        dungeon_dict["Duality"]["Flawless"] += player["Duality"]["Flawless"]
        dungeon_dict["Duality"]["Solo Flawless"] += player["Duality"]["Solo Flawless"]
        
        dungeon_dict["Grasp of Avarice"]["Clears"] += player["Grasp of Avarice"]["Clears"]
        dungeon_dict["Grasp of Avarice"]["Flawless"] += player["Grasp of Avarice"]["Flawless"]
        dungeon_dict["Grasp of Avarice"]["Solo Flawless"] += player["Grasp of Avarice"]["Solo Flawless"]
        
        dungeon_dict["Prophecy"]["Clears"] += player["Prophecy"]["Clears"]
        dungeon_dict["Prophecy"]["Flawless"] += player["Prophecy"]["Flawless"]
        dungeon_dict["Prophecy"]["Solo Flawless"] += player["Prophecy"]["Solo Flawless"]
        
        dungeon_dict["Pit of Heresy"]["Clears"] += player["Pit of Heresy"]["Clears"]
        dungeon_dict["Pit of Heresy"]["Flawless"] += player["Pit of Heresy"]["Flawless"]
        dungeon_dict["Pit of Heresy"]["Solo Flawless"] += player["Pit of Heresy"]["Solo Flawless"]
        
        dungeon_dict["The Shattered Throne"]["Clears"] += player["The Shattered Throne"]["Clears"]
        dungeon_dict["The Shattered Throne"]["Flawless"] += player["The Shattered Throne"]["Flawless"]
        dungeon_dict["The Shattered Throne"]["Solo Flawless"] += player["The Shattered Throne"]["Solo Flawless"]
    return generate_html(dungeon_dict)
    

def run():
    thomas_data = process_player("Thomas", 1, 4611686018444441571)
    douglas_data = process_player("Douglas", 1, 4611686018434621591)
    mark_data = process_player("Mark", 1, 4611686018432221111)
    connor_data = process_player("Connor", 1, 4611686018450697084)
    jack_data = process_player("Jack", 2, 4611686018469231992)
    hunter_data = process_player("Hunter", 3, 4611686018476416864)
    cameron_data = process_player("Cameron", 3, 4611686018501646188)
    kade_data = process_player("Kade", 1, 4611686018451886498)
    xavier_data = process_player("Xavier", 3, 4611686018471574419)
    player_data_list = [
        thomas_data,
        douglas_data,
        mark_data,
        connor_data,
        jack_data,
        hunter_data,
        cameron_data,
        kade_data,
        xavier_data
    ]
    
def compile_clan(player_data_list):
    clan_html = process_clan(player_data_list)
    write_to_directory(clan_html, "Clan")