# Thomas McGinley
# Started 1/1/2024
# Last Updated 2/9/2024

# Gathers weapon type kills information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
from prettytable import PrettyTable


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


def weapon_dictionary():
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


def clean_weapon_data(metric_data):
    weapon_dict = weapon_dictionary()
    
    weapon_dict["Auto Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['2094013181']["objectiveProgress"]['progress']
    weapon_dict["Pulse Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['982406257']["objectiveProgress"]['progress']
    weapon_dict["Scout Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['2599646044']["objectiveProgress"]['progress']
    weapon_dict["Hand Cannon"] = metric_data["Response"]['metrics']['data']['metrics']['2117204340']["objectiveProgress"]['progress']
    weapon_dict["Sidearm"] = metric_data["Response"]['metrics']['data']['metrics']['2012993124']["objectiveProgress"]['progress']
    weapon_dict["Submachine Gun"] = metric_data["Response"]['metrics']['data']['metrics']['1165153680']["objectiveProgress"]['progress']
    weapon_dict["Bow"] = metric_data["Response"]['metrics']['data']['metrics']['3522276357']["objectiveProgress"]['progress']
    weapon_dict["Trace Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['3124958797']["objectiveProgress"]['progress']
    weapon_dict["Fusion Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['105734892']["objectiveProgress"]['progress']
    weapon_dict["Shotgun"] = metric_data["Response"]['metrics']['data']['metrics']['139320435']["objectiveProgress"]['progress']
    weapon_dict["Sniper Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['633604541']["objectiveProgress"]['progress']
    weapon_dict["Grenade Launcher"] = metric_data["Response"]['metrics']['data']['metrics']['1681554390']["objectiveProgress"]['progress']
    weapon_dict["Rocket Launcher"] = metric_data["Response"]['metrics']['data']['metrics']['1200426430']["objectiveProgress"]['progress']
    weapon_dict["Sword"] = metric_data["Response"]['metrics']['data']['metrics']['1619269474']["objectiveProgress"]['progress']
    weapon_dict["Linear Fusion Rifle"] = metric_data["Response"]['metrics']['data']['metrics']['2707112071']["objectiveProgress"]['progress']
    weapon_dict["Machine Gun"] = metric_data["Response"]['metrics']['data']['metrics']['401742412']["objectiveProgress"]['progress']
    
    return weapon_dict


def generate_html(weapon_data):
    table = PrettyTable()
    table.field_names = ["Weapon Type", "Kills"]
    for weapon_type in weapon_data:
        table.add_row([weapon_type,weapon_data[weapon_type]])
    table.sortby = "Kills"
    table.reversesort = True
    return table.get_html_string()


def write_to_directory(data,name):
    f = open(f'./data/{name}Weapons.html', 'w')
    f.write('''
    <style>
    @font-face {
    font-family: JetBrains Mono;
    src: url("../fonts/JetBrainsMono-Regular.ttf");
    }
    
    h1,
    h2 {
        color: white;
        font-family: "JetBrains Mono", 'Courier New', Courier, monospace
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
    
    
def process_player(name, mem_type, mem_id):
    raw_data = get_metric_data(mem_type, mem_id)
    clean_data = clean_weapon_data(raw_data)
    html_string = generate_html(clean_data)
    write_to_directory(html_string,name)
    return clean_data


def process_clan(player_data_list):
    weapon_dict = weapon_dictionary()
    for player in player_data_list:
        weapon_dict["Auto Rifle"] += player["Auto Rifle"]
        weapon_dict["Pulse Rifle"] += player["Pulse Rifle"]
        weapon_dict["Scout Rifle"] += player["Scout Rifle"]
        weapon_dict["Hand Cannon"] += player["Hand Cannon"]
        weapon_dict["Sidearm"] += player["Sidearm"]
        weapon_dict["Submachine Gun"] += player["Submachine Gun"]
        weapon_dict["Bow"] += player["Bow"]
        weapon_dict["Trace Rifle"] += player["Trace Rifle"]
        weapon_dict["Fusion Rifle"] += player["Fusion Rifle"]
        weapon_dict["Shotgun"] += player["Shotgun"]
        weapon_dict["Sniper Rifle"] += player["Sniper Rifle"]
        weapon_dict["Grenade Launcher"] += player["Grenade Launcher"]
        weapon_dict["Rocket Launcher"] += player["Rocket Launcher"]
        weapon_dict["Sword"] += player["Sword"]
        weapon_dict["Linear Fusion Rifle"] += player["Linear Fusion Rifle"]
        weapon_dict["Machine Gun"] += player["Machine Gun"]
    return generate_html(weapon_dict)

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
    Clan_html = process_clan(player_data_list) 
    write_to_directory(Clan_html,"Clan")