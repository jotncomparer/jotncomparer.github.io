# Thomas McGinley
# Started 12/27/2023
# Last Updated 2/9/2024

# Gathers elemental final blows information about each desired player, cleans the data, and generates JSON files with relevant information


import requests
import json
from prettytable import PrettyTable


def element_data():
    dictionary = {"Total": 0, "Solar": 0, "Arc": 0, "Void": 0, "Stasis": 0, "Strand": 0}
    return dictionary


def clean_element_data(metric_data):
    element_dictionary = element_data()
    element_dictionary["Total"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "2537844000"
    ]["objectiveProgress"]["progress"]
    element_dictionary["Solar"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "2187143539"
    ]["objectiveProgress"]["progress"]
    element_dictionary["Arc"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "1513312460"
    ]["objectiveProgress"]["progress"]
    element_dictionary["Void"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "2327589890"
    ]["objectiveProgress"]["progress"]
    element_dictionary["Stasis"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2464463405"]["objectiveProgress"]["progress"]
    element_dictionary["Strand"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2889561660"]["objectiveProgress"]["progress"]
    return element_dictionary


def get_metric_data(mem_type, mem_id):
    url = f"https://www.bungie.net/Platform/Destiny2/{mem_type}/Profile/{mem_id}/?components=1100"
    payload = {}
    headers = {
        "x-api-key": "654dad1171c44eb688f2fb5ca11e7c3b",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response != 200:
            print("Error occurred in request:", response)
            print("She be Rhulking on my Disciple til I Strand")
    data = json.loads(response.content)
    return data


def generate_html(element_data):
    table = PrettyTable()
    table.field_names = ["Element", "Kills"]
    for element in element_data:
        kills = int(element_data[element])
        table.add_row([element, kills])
    return table.get_html_string()


def write_to_directory(data, name):
    f = open(f"./data/{name}Elements.html", "w")
    f.write(
        """
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
    """
    )
    f.write(data)
    f.close()
    print(f"{name} elemental data written!")


def process_player(name, mem_type, mem_id):
    raw_data = get_metric_data(mem_type, mem_id)
    element_data = clean_element_data(raw_data)
    html_string = generate_html(element_data)
    write_to_directory(html_string, name)
    return element_data


def process_clan(player_data_list):
    element_dictionary = element_data()
    for player in player_data_list:
        element_dictionary["Total"] += player["Total"]
        element_dictionary["Solar"] += player["Solar"]
        element_dictionary["Arc"] += player["Arc"]
        element_dictionary["Void"] += player["Void"]
        element_dictionary["Stasis"] += player["Stasis"]
        element_dictionary["Strand"] += player["Strand"]
    return generate_html(element_dictionary)


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
