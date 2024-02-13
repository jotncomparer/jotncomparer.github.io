# Thomas McGinley
# Started 12/28/2023
# Last Updated 2/9/2024

# Gathers fishing stat and good boy protocol information about each desired player, cleans the data, and generates JSON files with relevant information


import requests
import json
from prettytable import PrettyTable


def get_metric_data(mem_type, mem_id):
    url = f"https://www.bungie.net/Platform/Destiny2/{mem_type}/Profile/{mem_id}/?components=1100"
    payload = {}
    headers = {
        "x-api-key": "654dad1171c44eb688f2fb5ca11e7c3b",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()
    metric_data = json.loads(response.content)
    return metric_data


def fish_dict():
    dictionary = {
        "Total": 0,
        "Heaviest": 0,
        "Pets": 0,
        "Snowballs": 0,
        "Cookies": 0,
        "Name": "",
    }
    return dictionary


def clean_fishing_data(metric_data):
    fishing_dictionary = fish_dict()
    fishing_dictionary["Total"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "24768693"
    ]["objectiveProgress"]["progress"]
    fishing_dictionary["Heaviest"] = (
        metric_data["Response"]["metrics"]["data"]["metrics"]["2691615711"][
            "objectiveProgress"
        ]["progress"]
        / 100
    )
    fishing_dictionary["Pets"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "3131994725"
    ]["objectiveProgress"]["progress"]
    fishing_dictionary["Snowballs"] = metric_data["Response"]["metrics"]["data"][
        "metrics"
    ]["857713621"]["objectiveProgress"]["progress"]
    fishing_dictionary["Cookies"] = metric_data["Response"]["metrics"]["data"]["metrics"][
        "3597861791"
    ]["objectiveProgress"]["progress"]

    return fishing_dictionary


def generate_html(fishing_data, is_clan=False):
    table = PrettyTable()
    table.field_names = ["Stat", "Value"]
    table.add_row(["Total fish caught", int(fishing_data["Total"])])
    table.add_row(["Heaviest fish caught", str(fishing_data["Heaviest"]) + " kg"])
    if is_clan:
        table.add_row(["Biggest fish caught by", fishing_data["Name"]])
    table.add_row(["Good Boy Protocol activations", int(fishing_data["Pets"])])
    table.add_row(["Snowball kills", int(fishing_data["Snowballs"])])
    table.add_row(["Cookies baked", int(fishing_data["Cookies"])])
    return table.get_html_string()


def write_to_directory(data, name):
    
    f = open(f"./data/{name}Fish.html", "w")
    
    f.write(
        """
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
</style>
<h1>SILLY CORNER</h1>
    """
    )
    f.write(data)
    f.close()
    print(f"{name} fishing data written!")


def process_player(name, mem_type, mem_id):
    raw_data = get_metric_data(mem_type, mem_id)
    fishing_data = clean_fishing_data(raw_data)
    html_string = generate_html(fishing_data)
    write_to_directory(html_string, name)
    fishing_data["Name"] = name
    return fishing_data


def process_clan(player_data_list):
    fishing_dictionary = fish_dict()
    heaviest = 0.0
    for player in player_data_list:
        fishing_dictionary["Total"] += player["Total"]
        if player["Heaviest"] > heaviest:
            heaviest = player["Heaviest"]
            fishing_dictionary["Heaviest"] = player["Heaviest"]
            fishing_dictionary["Name"] = player["Name"]
        fishing_dictionary["Pets"] += player["Pets"]
        fishing_dictionary["Snowballs"] += player["Snowballs"]
        fishing_dictionary["Cookies"] += player["Cookies"]
    return generate_html(fishing_dictionary, True)

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
