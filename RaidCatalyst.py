# Thomas McGinley
# Started 2/12/2024
# Last Updated 2/19/2024

# Expanded data on a player's raid info

import json
import requests
from Time_Converter import Time_Converter
from MillisecondTimeConverter import convert


def get_raid_data(mem_type, mem_id, char_id_1, char_id_2, char_id_3):
    char_ids = [char_id_1, char_id_2, char_id_3]
    data_package = []
    for char_id in char_ids:
        #i range subject to change, 10 just seemed like a reasonable number to start with
        for i in range(0, 10):
            url = f"https://www.bungie.net/Platform/Destiny2/{mem_type}/Account/{mem_id}/Character/{char_id}/Stats/Activities/?count=250&mode=4&page={i}"
            payload = {}
            header = {
                "x-api-key": "654dad1171c44eb688f2fb5ca11e7c3b",
            }
            response = requests.request("GET", url, headers=header, data=payload)
            if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()
            
            data = json.loads(response.content)
            
            if len(data["Response"]) > 0:
                data_package.append(data["Response"])
                print (f"page printed: {i}")
                continue
            break
            
    return data_package


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
    data = json.loads(response.content)
    return data


def raid_dictionary():
    dictionary = {
        "Total": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": "n/a",
        },
        # INSERT NEW RAIDS HERE
        "Crota's End": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "crotasend",
        },
        "Root of Nightmares": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "rootofnightmares",
        },
        "King's Fall": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "kingsfall",
        },
        "Vow of the Disciple": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "vowofthedisciple",
        },
        "Vault of Glass": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "vaultofglass",
        },
        "Deep Stone Crypt": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "deepstonecrypt",
        },
        "Garden of Salvation": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "gardenofsalvation",
        },
        "Last Wish": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "lastwish",
        },
        "Crown of Sorrow": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "crownofsorrow",
        },
        "Scourge of the Past": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "scourgeofthepast",
        },
        "Spire of Stars": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "spireofstars",
        },
        "Eater of Worlds": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "eaterofworlds",
        },
        "Leviathan": {
            "Time": 0,
            "Launches": 0,
            "Completions": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Fastest": 0,
            "Image": "leviathan",
        },
    }
    return dictionary


def clean_data(data_list):
    raid_dict = raid_dictionary()
    for page in data_list:
        instances = page["activities"]
        for instance in instances:

            reference_id = instance["activityDetails"]["referenceId"]

            if reference_id == 2122313384:
                raid_dict["Last Wish"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Last Wish"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Last Wish"]["Kills"] += instance["values"]["kills"]["basic"][
                    "value"
                ]
                raid_dict["Last Wish"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Last Wish"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif (
                reference_id == 3458480158
                or reference_id == 2659723068
                or reference_id == 1042180643
            ):
                raid_dict["Garden of Salvation"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Garden of Salvation"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Garden of Salvation"]["Kills"] += instance["values"][
                    "kills"
                ]["basic"]["value"]
                raid_dict["Garden of Salvation"]["Deaths"] += instance["values"][
                    "deaths"
                ]["basic"]["value"]
                raid_dict["Garden of Salvation"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 910380154:
                raid_dict["Deep Stone Crypt"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Deep Stone Crypt"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Deep Stone Crypt"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Deep Stone Crypt"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Deep Stone Crypt"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif (
                reference_id == 3881495763
                or reference_id == 1681562271
                or reference_id == 3022541210
                or reference_id == 1485585878
            ):
                raid_dict["Vault of Glass"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Vault of Glass"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Vault of Glass"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Vault of Glass"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Vault of Glass"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 1441982566 or reference_id == 4217492330:
                raid_dict["Vow of the Disciple"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Vow of the Disciple"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Vow of the Disciple"]["Kills"] += instance["values"][
                    "kills"
                ]["basic"]["value"]
                raid_dict["Vow of the Disciple"]["Deaths"] += instance["values"][
                    "deaths"
                ]["basic"]["value"]
                raid_dict["Vow of the Disciple"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif (
                reference_id == 1374392663
                or reference_id == 2964135793
                or reference_id == 3257594522
                or reference_id == 1063970578
            ):
                raid_dict["King's Fall"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["King's Fall"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["King's Fall"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["King's Fall"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["King's Fall"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 2381413764 or reference_id == 2918919505:
                raid_dict["Root of Nightmares"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Root of Nightmares"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Root of Nightmares"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Root of Nightmares"]["Deaths"] += instance["values"][
                    "deaths"
                ]["basic"]["value"]
                raid_dict["Root of Nightmares"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif (
                reference_id == 2693136601
                or reference_id == 2693136604
                or reference_id == 3879860661
                or reference_id == 2693136602
                or reference_id == 2693136603
                or reference_id == 2693136605
                or reference_id == 2693136600
                or reference_id == 417231112
                or reference_id == 757116822
                or reference_id == 1685065161
                or reference_id == 2449714930
                or reference_id == 3446541099
            ):
                raid_dict["Leviathan"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Leviathan"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Leviathan"]["Kills"] += instance["values"]["kills"]["basic"][
                    "value"
                ]
                raid_dict["Leviathan"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Leviathan"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 548750096:
                raid_dict["Scourge of the Past"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Scourge of the Past"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Scourge of the Past"]["Kills"] += instance["values"][
                    "kills"
                ]["basic"]["value"]
                raid_dict["Scourge of the Past"]["Deaths"] += instance["values"][
                    "deaths"
                ]["basic"]["value"]
                raid_dict["Scourge of the Past"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 3333172150:
                raid_dict["Crown of Sorrow"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Crown of Sorrow"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Crown of Sorrow"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Crown of Sorrow"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Crown of Sorrow"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 3089205900 or reference_id == 809170886:
                raid_dict["Eater of Worlds"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Eater of Worlds"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Eater of Worlds"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Eater of Worlds"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Eater of Worlds"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif reference_id == 119944200 or reference_id == 3213556450:
                raid_dict["Spire of Stars"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Spire of Stars"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Spire of Stars"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Spire of Stars"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Spire of Stars"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            elif (
                reference_id == 4179289725
                or reference_id == 1507509200
                or reference_id == 156253568
            ):
                raid_dict["Crota's End"]["Launches"] += 1
                # adds one to completions if completed (value is zero otherwise)
                raid_dict["Crota's End"]["Completions"] += instance["values"][
                    "completed"
                ]["basic"]["value"]
                raid_dict["Crota's End"]["Kills"] += instance["values"]["kills"][
                    "basic"
                ]["value"]
                raid_dict["Crota's End"]["Deaths"] += instance["values"]["deaths"][
                    "basic"
                ]["value"]
                raid_dict["Crota's End"]["Time"] += instance["values"][
                    "activityDurationSeconds"
                ]["basic"]["value"]

            else:
                print(f"Unrecognized reference id: {reference_id}")
                print("DROWNDROWNDROWN")

    for raid in raid_dict:
        if raid != "Total":
            raid_dict["Total"]["Launches"] += raid_dict[raid]["Launches"]
            raid_dict["Total"]["Completions"] += raid_dict[raid]["Completions"]
            raid_dict["Total"]["Kills"] += raid_dict[raid]["Kills"]
            raid_dict["Total"]["Deaths"] += raid_dict[raid]["Deaths"]
            raid_dict["Total"]["Time"] += raid_dict[raid]["Time"]

    # This has to be done in a separate loop after Total has been processed
    for raid in raid_dict:
        if raid_dict[raid]["Deaths"] > 0:
            raid_dict[raid]["KD"] = round(
                raid_dict[raid]["Kills"] / raid_dict[raid]["Deaths"], 2
            )

    return raid_dict


def add_speedrun(metric_data, raid_dict):
    raid_dict["Crota's End"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["510466839"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Root of Nightmares"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["58319253"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["King's Fall"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["399420098"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Vow of the Disciple"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["3775579868"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Vault of Glass"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["905219689"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Deep Stone Crypt"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["3679202587"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Garden of Salvation"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["1835852368"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Last Wish"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["4164362538"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Crown of Sorrow"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["996516677"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Scourge of the Past"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["1245368441"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Spire of Stars"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["2842037131"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Eater of Worlds"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["1275208010"][
            "objectiveProgress"
        ]["progress"]
    )
    raid_dict["Leviathan"]["Fastest"] = convert(
        metric_data["Response"]["metrics"]["data"]["metrics"]["3434325913"][
            "objectiveProgress"
        ]["progress"]
    )
    return raid_dict


def generate_html(raid_data):

    html_string = "<div class=flexContainer>"
    for raid in raid_data:
        if raid == "Total":
            html_string += f"""
            <div class="raidBox">
                <h1>{raid}</h1>
                <h2>Clears: {int(raid_data[raid]["Completions"])}</h2>
                <p>Launches: {int(raid_data[raid]["Launches"])}</p>
                <p>Kills: {int(raid_data[raid]["Kills"])}</p>
                <p>Deaths: {int(raid_data[raid]["Deaths"])}</p>
                <p>K/D: {raid_data[raid]["KD"]}</p>
                <p>Time played: {Time_Converter(raid_data[raid]["Time"])}</p>
            </div>
            """
        else:
            html_string += f"""
            <div class="raidBox">
                <img src="../images/{raid_data[raid]["Image"]}.jpg">
                <h1>{raid}</h1>
                <h2>Clears: {int(raid_data[raid]["Completions"])}</h2>
                <p>Launches: {int(raid_data[raid]["Launches"])}</p>
                <p>Kills: {int(raid_data[raid]["Kills"])}</p>
                <p>Deaths: {int(raid_data[raid]["Deaths"])}</p>
                <p>K/D: {raid_data[raid]["KD"]}</p>
                <p>Fastest time: {raid_data[raid]["Fastest"]}</p>
                <p>Time played: {Time_Converter(raid_data[raid]["Time"])}</p>
            </div>
            """
    html_string += "</div>"
    return html_string


def write_to_directory(data, name):
    f = open(f"./data/{name}RaidReport.html", "w")
    f.write(
        """
<style>
       @font-face {
        font-family: "JetBrains Mono";
        src: url(fonts/JetBrainsMono-Regular.ttf);
    }

    html {
        font-family: "JetBrains Mono", 'Courier New', Courier, monospace;
        color: white;

    }

    .flexContainer {
        display: flex;
        flex-wrap: wrap;

    }

    .raidBox {
        border-radius: 10px;
        background-color: rgb(75, 75, 75);
        margin: 15px;
        flex: 25%;
    }
    .raidBox h2,
    .raidBox p {
        padding: 0 15px;
    }
    .raidBox>div {
        height: 10em;
        background-size:contain;
        background-repeat: no-repeat;
        margin:0 40px;
    }
    h1 {
        text-align: center;
    }
    .raidBox>img {
        border-radius: 10px 10px 0 0;
        width:100%;
    }
</style>
    """
    )
    f.write(data)
    f.close()
    print(f"{name} raid report data written!")


def process_player(name, mem_type, mem_id, char_id_1, char_id_2, char_id_3):

    raw_data_list = get_raid_data(
        mem_type=mem_type,
        mem_id=mem_id,
        char_id_1=char_id_1,
        char_id_2=char_id_2,
        char_id_3=char_id_3,
    )
    speedrun_stats = get_metric_data(mem_id=mem_id, mem_type=mem_type)
    clean_data_dict = clean_data(raw_data_list)
    complete_data_dict = add_speedrun(
        metric_data=speedrun_stats, raid_dict=clean_data_dict
    )
    html_string = generate_html(complete_data_dict)
    write_to_directory(data=html_string, name=name)
    return complete_data_dict


def compile_clan(player_data_list):
    raid_dict = raid_dictionary()
    for player in player_data_list:
        for raid in raid_dict:
            raid_dict[raid]["Time"] += player[raid]["Time"]
            raid_dict[raid]["Launches"] += player[raid]["Launches"]
            raid_dict[raid]["Completions"] += player[raid]["Completions"]
            raid_dict[raid]["Kills"] += player[raid]["Kills"]
            raid_dict[raid]["Deaths"] += player[raid]["Deaths"]

    for raid in raid_dict:
        if raid_dict[raid]["Deaths"] > 0:
            raid_dict[raid]["KD"] = round(
                raid_dict[raid]["Kills"] / raid_dict[raid]["Deaths"], 2
            )

    html_string = "<div class=flexContainer>"
    for raid in raid_dict:
        if raid == "Total":
            html_string += f"""
            <div class="raidBox">
                <h1>{raid}</h1>
                <h2>Clears: {int(raid_dict[raid]["Completions"])}</h2>
                <p>Launches: {int(raid_dict[raid]["Launches"])}</p>
                <p>Kills: {int(raid_dict[raid]["Kills"])}</p>
                <p>Deaths: {int(raid_dict[raid]["Deaths"])}</p>
                <p>K/D: {raid_dict[raid]["KD"]}</p>
                <p>Time played: {Time_Converter(raid_dict[raid]["Time"])}</p>
            </div>
            """
        else:
            html_string += f"""
            <div class="raidBox">
                <img src="../images/{raid_dict[raid]["Image"]}.jpg">
                <h1>{raid}</h1>
                <h2>Clears: {int(raid_dict[raid]["Completions"])}</h2>
                <p>Launches: {int(raid_dict[raid]["Launches"])}</p>
                <p>Kills: {int(raid_dict[raid]["Kills"])}</p>
                <p>Deaths: {int(raid_dict[raid]["Deaths"])}</p>
                <p>K/D: {raid_dict[raid]["KD"]}</p>
                <p>Time played: {Time_Converter(raid_dict[raid]["Time"])}</p>
            </div>
            """
    html_string += "</div>"
    write_to_directory(data=html_string, name="Clan")


def run():
    thomasDataClean = process_player(
        "Thomas",
        1,
        4611686018444441571,
        2305843009265786295,
        2305843009283965144,
        2305843009569534739,
    )
    douglasDataClean = process_player(
        "Douglas",
        1,
        4611686018434621591,
        2305843009293915719,
        2305843009301374530,
        2305843010083874501,
    )
    markDataClean = process_player(
        "Mark",
        1,
        4611686018432221111,
        2305843009348154555,
        2305843009668854600,
        2305843009802904121,
    )
    connorDataClean = process_player(
        "Connor",
        1,
        4611686018450697084,
        2305843009644414176,
        2305843009663894341,
        2305843009703275457,
    )
    jackDataClean = process_player(
        "Jack",
        2,
        4611686018469231992,
        2305843009268771475,
        2305843009891864023,
        2305843009890274343,
    )
    hunterDataClean = process_player(
        "Hunter",
        3,
        4611686018476416864,
        2305843009359734078,
        2305843009359365362,
        2305843009756404411,
    )
    cameronDataClean = process_player(
        "Cameron",
        3,
        4611686018501646188,
        2305843009624174508,
        2305843009683284492,
        2305843009683284493,
    )
    kadeDataClean = process_player(
        "Kade",
        1,
        4611686018451886498,
        2305843009264637524,
        2305843009264637527,
        2305843010322954573,
    )
    xavierDataClean = process_player(
        "Xavier",
        3,
        4611686018471574419,
        2305843009306625517,
        2305843009309817521,
        2305843009313885640,
    )

    playerDataList = [
        thomasDataClean,
        douglasDataClean,
        markDataClean,
        connorDataClean,
        jackDataClean,
        hunterDataClean,
        cameronDataClean,
        kadeDataClean,
        xavierDataClean,
    ]

    compile_clan(playerDataList)