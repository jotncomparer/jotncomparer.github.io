# Thomas McGinley
# Started 1/3/2024
# Last Updated 2/9/2024

# Gathers Strike information about each desired player, cleans the data, and generates HTML files with relevant information


import requests
import json
from prettytable import PrettyTable


def get_metric_data(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1100"
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


def strike_dictionary():
    dictionary = {
        "Completions": 0,
        "Flawless": 0,
        "Champion Kills": 0,
        "Strike Kills This Season": 0,
        "The Arms Dealer": 0,
        "Insight Terminus": 0,
        "The Inverted Spire": 0,
        "Savathun's Song": 0,
        "The Pyramidion": 0,
        "Exodus Crash": 0,
        "A Garden World": 0,
        "Tree of Probabilities": 0,
        "Strange Terrain": 0,
        "Warden of Nothing": 0,
        "Broodhold": 0,
        "The Scarlet Keep": 0,
        "Lake of Shadows": 0,
        "The Corrupted": 0,
        "The Festering Core": 0,
        "The Disgraced": 0,
        "The Glassway": 0,
        "Proving Grounds": 0,
        "The Devils' Lair": 0,
        "Fallen S.A.B.E.R": 0,
        "The Hollowed Lair": 0,
        "The Lightblade": 0,
        "Birthplace of the Vile": 0,
    }
    return dictionary


def clean_strike_data(metric_data):
    strike_dict = strike_dictionary()

    strike_dict["Completions"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "793155718"
    ]["objectiveProgress"]["progress"]
    strike_dict["Flawless"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "2326329668"
    ]["objectiveProgress"]["progress"]
    strike_dict["Champion Kills"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["41075005"]["objectiveProgress"]["progress"]
    strike_dict["Strike Kills This Season"] = metric_data["Response"]["metrics"][
        "data"
    ]["metrics"]["3857340681"]["objectiveProgress"]["progress"]

    strike_dict["The Arms Dealer"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3036740778"]["objectiveProgress"]["progress"]
    strike_dict["Insight Terminus"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3146366866"]["objectiveProgress"]["progress"]
    strike_dict["The Inverted Spire"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3466351705"]["objectiveProgress"]["progress"]
    strike_dict["Savathun's Song"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2894079898"]["objectiveProgress"]["progress"]
    strike_dict["The Pyramidion"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2457392818"]["objectiveProgress"]["progress"]
    strike_dict["Exodus Crash"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "1118387860"
    ]["objectiveProgress"]["progress"]
    strike_dict["A Garden World"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3543375894"]["objectiveProgress"]["progress"]
    strike_dict["Tree of Probabilities"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2778406657"]["objectiveProgress"]["progress"]
    strike_dict["Strange Terrain"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["40546883"]["objectiveProgress"]["progress"]
    strike_dict["Warden of Nothing"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["4140273235"]["objectiveProgress"]["progress"]
    strike_dict["Broodhold"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "356508148"
    ]["objectiveProgress"]["progress"]
    strike_dict["The Scarlet Keep"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["1666283222"]["objectiveProgress"]["progress"]
    strike_dict["Lake of Shadows"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3139878529"]["objectiveProgress"]["progress"]
    strike_dict["The Corrupted"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2920064672"]["objectiveProgress"]["progress"]
    strike_dict["The Festering Core"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["326550718"]["objectiveProgress"]["progress"]
    strike_dict["The Disgraced"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["136014172"]["objectiveProgress"]["progress"]
    strike_dict["The Glassway"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "2883115929"
    ]["objectiveProgress"]["progress"]
    strike_dict["Proving Grounds"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3209483141"]["objectiveProgress"]["progress"]
    strike_dict["The Devils' Lair"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["103014972"]["objectiveProgress"]["progress"]
    strike_dict["Fallen S.A.B.E.R"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["2894593528"]["objectiveProgress"]["progress"]
    strike_dict["The Hollowed Lair"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["449969041"]["objectiveProgress"]["progress"]
    strike_dict["The Lightblade"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["3181525833"]["objectiveProgress"]["progress"]
    strike_dict["Birthplace of the Vile"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["1065851514"]["objectiveProgress"]["progress"]

    return strike_dict


def generate_html(strike_data):
    table = PrettyTable()
    table.field_names = ["Stat", "Value"]
    table.add_row(["General Statistics", " "])
    i = 0
    for strike in strike_data:
        table.add_row([strike, strike_data[strike]])
        if i == 3:
            table.add_row(["Strike", "High Score"])
        i += 1
    return table.get_html_string()


def generate_clan_html(strike_data):
    table = PrettyTable()
    table.field_names = ["Stat", "Value"]
    table.add_row(["General Statistics", " "])
    table.add_row(["Completions", strike_data["Completions"]])
    table.add_row(["Flawless", strike_data["Flawless"]])
    table.add_row(["Champion Kills", strike_data["Champion Kills"]])
    table.add_row(["Strike Kills This Season", strike_data["Strike Kills This Season"]])
    return table.get_html_string()


def write_to_directory(data, name):
    f = open(f"./data/{name}Strikes.html", "w")
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
    """
    )
    f.write(data)
    f.close()
    print(f"{name} strike data written!")


def process_player(name, mem_type, mem_id):
    raw_data = get_metric_data(mem_type, mem_id)
    clean_data = clean_strike_data(raw_data)
    html_string = generate_html(clean_data)
    write_to_directory(html_string, name)
    return clean_data


def process_clan(player_data_list):
    strike_dict = strike_dictionary()
    for player in player_data_list:
        strike_dict["Completions"] += player["Completions"]
        strike_dict["Flawless"] += player["Flawless"]
        strike_dict["Champion Kills"] += player["Champion Kills"]
        strike_dict["Strike Kills This Season"] += player["Strike Kills This Season"]
    return generate_clan_html(strike_dict)


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
        xavier_data,
    ]
    
def compile_clan(player_data_list):
    clan_html = process_clan(player_data_list)
    write_to_directory(clan_html, "Clan")
