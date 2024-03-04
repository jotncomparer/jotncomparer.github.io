# Thomas McGinley
# Started 1/14/2024
# Last Updated 3/3/2024

# Gathers basic commendation information about each desired player, cleans the data, and generates HTML files with relevant information

from APIKEY import API_KEY
import requests
import json
from prettytable import PrettyTable


def get_commendation_data(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=1400"
    payload = {}
    headers = API_KEY
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()
    metricData = json.loads(response.content)
    return metricData


def commendation_dictionary():
    dictionary = {
        "Total": 0,
        "Ally": {"Score": 0, "Percent": 0},
        "Indispensable": 0,
        "Selfless": 0,
        "Thoughtful": 0,
        "Patient And Considerate": 0,
        "Fun": {"Score": 0, "Percent": 0},
        "Joy Bringer": 0,
        "Level-Headed": 0,
        "Saint's Favorite": 0,
        "Best Dressed": 0,
        "Mastery": {"Score": 0, "Percent": 0},
        "Playmaker": 0,
        "Primeval Instinct": 0,
        "Heroic": 0,
        "Pacesetter": 0,
        "Leadership": {"Score": 0, "Percent": 0},
        "Perceptive": 0,
        "Knowledgeable": 0,
    }
    return dictionary


def clean_data(comm_data):
    comm_dict = commendation_dictionary()
    comm_dict["Total"] = comm_data["Response"]["profileCommendations"]["data"][
        "totalScore"
    ]

    comm_dict["Ally"]["Score"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationNodeScoresByHash"
    ]["154475713"]
    comm_dict["Ally"]["Percent"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationNodePercentagesByHash"]["154475713"]
    comm_dict["Indispensable"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["2019871317"]
    comm_dict["Selfless"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["354527503"]
    comm_dict["Thoughtful"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["3513056018"]
    comm_dict["Patient And Considerate"] = comm_data["Response"][
        "profileCommendations"
    ]["data"]["commendationScoresByHash"]["2506835299"]

    comm_dict["Fun"]["Score"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationNodeScoresByHash"
    ]["1341823550"]
    comm_dict["Fun"]["Percent"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationNodePercentagesByHash"
    ]["1341823550"]
    comm_dict["Joy Bringer"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["3377580220"]
    comm_dict["Level-Headed"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["3037314846"]
    comm_dict["Saint's Favorite"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationScoresByHash"]["3030493827"]
    comm_dict["Best Dressed"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["357212819"]

    comm_dict["Mastery"]["Score"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationNodeScoresByHash"]["4180748446"]
    comm_dict["Mastery"]["Percent"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationNodePercentagesByHash"]["1390663518"]
    comm_dict["Playmaker"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["4209356036"]
    comm_dict["Primeval Instinct"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationScoresByHash"]["363818544"]
    comm_dict["Heroic"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["3575743922"]
    comm_dict["Pacesetter"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["2205006002"]

    comm_dict["Leadership"]["Score"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationNodeScoresByHash"]["1390663518"]
    comm_dict["Leadership"]["Percent"] = comm_data["Response"]["profileCommendations"][
        "data"
    ]["commendationNodePercentagesByHash"]["4180748446"]
    comm_dict["Perceptive"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["3872064891"]
    comm_dict["Knowledgeable"] = comm_data["Response"]["profileCommendations"]["data"][
        "commendationScoresByHash"
    ]["3970150545"]

    return comm_dict


def generate_table(clean_data):
    table = PrettyTable()
    table.add_column(
        "Ally",
        [
            clean_data["Ally"]["Score"],
            "Indispensable",
            "Selfless",
            "Thoughtful",
            "Patient And Considerate",
        ],
    )
    table.add_column(
        " ",
        [
            str(clean_data["Ally"]["Percent"]) + "%",
            clean_data["Indispensable"],
            clean_data["Selfless"],
            clean_data["Thoughtful"],
            clean_data["Patient And Considerate"],
        ],
    )

    table.add_column(
        "Fun",
        [
            clean_data["Fun"]["Score"],
            "Joy Bringer",
            "Level-Headed",
            "Saint's Favorite",
            "Best Dressed",
        ],
    )
    table.add_column(
        "  ",
        [
            str(clean_data["Fun"]["Percent"]) + "%",
            clean_data["Joy Bringer"],
            clean_data["Level-Headed"],
            clean_data["Saint's Favorite"],
            clean_data["Best Dressed"],
        ],
    )

    table.add_column(
        "Mastery",
        [
            clean_data["Mastery"]["Score"],
            "Playmaker",
            "Primeval Instinct",
            "Heroic",
            "Pacesetter",
        ],
    )
    table.add_column(
        "   ",
        [
            str(clean_data["Mastery"]["Percent"]) + "%",
            clean_data["Playmaker"],
            clean_data["Primeval Instinct"],
            clean_data["Heroic"],
            clean_data["Pacesetter"],
        ],
    )

    table.add_column(
        "Leadership",
        [clean_data["Leadership"]["Score"], "Perceptive", "Knowledgeable", " ", " "],
    )
    table.add_column(
        "    ",
        [
            str(clean_data["Leadership"]["Percent"]) + "%",
            clean_data["Perceptive"],
            clean_data["Knowledgeable"],
            " ",
            " ",
        ],
    )
    # table.add_row(["Total Commendation Score", cleanData["Total"], "", "", "", "", "", ""])
    return table.get_html_string()


def write_to_directory(data, name, dictionary):
    try:
        f = open(f"./data/{name}Commendation.html", "w")
    except:
        print("Write file did not open properly")
        quit()
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
        font-size: medium
    }

    table {
        color: white;
        width: 100%;
        text-align: left;
        font-family: 'Courier New', Courier, monospace
    }

    th,
    td {
        border-bottom: 1px solid white
    }

    thead>tr>th:nth-of-type(1),
    thead>tr>th:nth-of-type(2) {
        background-color: mediumspringgreen;
        color: black
    }

    thead>tr>th:nth-of-type(3),
    thead>tr>th:nth-of-type(4) {
        background-color: palevioletred;
        color: black
    }

    thead>tr>th:nth-of-type(5),
    thead>tr>th:nth-of-type(6) {
        background-color: orange;
        color: black
    }

    thead>tr>th:nth-of-type(7),
    thead>tr>th:nth-of-type(8) {
        background-color: cornflowerblue;
        color: black
    }

    tbody>tr:nth-child(2n)>td:nth-of-type(1),
    tbody>tr:nth-child(2n)>td:nth-of-type(2) {
        background-color: rgba(0, 240, 154, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(1),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(2) {
        background-color: rgba(0, 240, 154, .25)
    }

    tbody>tr:nth-child(2n)>td:nth-of-type(3),
    tbody>tr:nth-child(2n)>td:nth-of-type(4) {
        background-color: rgba(219, 112, 147, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(3),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(4) {
        background-color: rgba(219, 112, 147, .25)
    }

    tbody>tr:nth-child(2n)>td:nth-of-type(5),
    tbody>tr:nth-child(2n)>td:nth-of-type(6) {
        background-color: rgba(255, 165, 0, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(5),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(6) {
        background-color: rgba(255, 165, 0, .25)
    }
    
    tbody>tr:nth-child(2n)>td:nth-of-type(7),
    tbody>tr:nth-child(2n)>td:nth-of-type(8) {
        background-color: rgba(100, 149, 237, .5)
    }

    tbody>tr:nth-child(2n-1)>td:nth-of-type(7),
    tbody>tr:nth-child(2n-1)>td:nth-of-type(8) {
        background-color: rgba(100, 149, 237, .25)
    }
</style>
    """
    )
    f.write(
        f"""
<h1>Commendations - Total: {dictionary["Total"]}</h1>
<h2>Resets every season</h2>
    """
    )
    f.write(data)
    f.close()
    print(f"{name} commendation data written!")


def process_player(name, mem_type, mem_id):
    raw_data = get_commendation_data(mem_type, mem_id)
    cleaned_data = clean_data(raw_data)
    htmlString = generate_table(cleaned_data)
    write_to_directory(htmlString, name, cleaned_data)
    return cleaned_data


def process_clan(player_data_list):
    comm_dict = commendation_dictionary()
    for player in player_data_list:
        comm_dict["Total"] += player["Total"]

        comm_dict["Ally"]["Score"] += player["Ally"]["Score"]
        # commDict["Ally"]["Percent"] += player["Ally"]["Percent"]
        comm_dict["Indispensable"] += player["Indispensable"]
        comm_dict["Selfless"] += player["Selfless"]
        comm_dict["Thoughtful"] += player["Thoughtful"]
        comm_dict["Patient And Considerate"] += player["Patient And Considerate"]

        comm_dict["Fun"]["Score"] += player["Fun"]["Score"]
        # commDict["Fun"]["Percent"] += player["Fun"]["Percent"]
        comm_dict["Joy Bringer"] += player["Joy Bringer"]
        comm_dict["Level-Headed"] += player["Level-Headed"]
        comm_dict["Saint's Favorite"] += player["Saint's Favorite"]
        comm_dict["Best Dressed"] += player["Best Dressed"]

        comm_dict["Mastery"]["Score"] += player["Mastery"]["Score"]
        # commDict["Mastery"]["Percent"] += player["Mastery"]["Percent"]
        comm_dict["Playmaker"] += player["Playmaker"]
        comm_dict["Primeval Instinct"] += player["Primeval Instinct"]
        comm_dict["Heroic"] += player["Heroic"]
        comm_dict["Pacesetter"] += player["Pacesetter"]

        comm_dict["Leadership"]["Score"] += player["Leadership"]["Score"]
        # commDict["Leadership"]["Percent"] += player["Leadership"]["Percent"]
        comm_dict["Perceptive"] += player["Perceptive"]
        comm_dict["Knowledgeable"] += player["Knowledgeable"]

    return generate_table(comm_dict)


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
    total = 0
    for player in player_data_list:
        total += player["Total"]
    write_to_directory(name="Clan", data=clan_html, dictionary={"Total": total})
