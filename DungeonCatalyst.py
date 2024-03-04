# Thomas McGinley
# Started 2/19/2024
# Last Updated 3/3/2024

# Expanded data on a player's raid info

from APIKEY import API_KEY
import json
import requests
from Time_Converter import Time_Converter
from MillisecondTimeConverter import convert


def get_dungeon_data(mem_type, mem_id, char_id_1, char_id_2, char_id_3):
    char_ids = [char_id_1, char_id_2, char_id_3]
    data_package = []
    for char_id in char_ids:
        # i range subject to change, 10 just seemed like a reasonable number to start with
        for i in range(0, 10):
            url = f"https://www.bungie.net/Platform/Destiny2/{mem_type}/Account/{mem_id}/Character/{char_id}/Stats/Activities/?count=250&mode=82&page={i}"
            payload = {}
            header = API_KEY
            response = requests.request("GET", url, headers=header, data=payload)
            if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()

            data = json.loads(response.content)

            if len(data["Response"]) > 0:
                data_package.append(data["Response"])
                print(f"page printed: {i}")
                continue
            break

    return data_package


def dungeon_dictionary():
    dictionary = {
        "Total": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
        },
        # INSERT NEW DUNGEONS HERE
        "Warlord's Ruin": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "warlordsruin",
        },
        "Ghosts of the Deep": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "ghostsofthedeep",
        },
        "Spire of the Watcher": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "spireofthewatcher",
        },
        "Duality": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "duality",
        },
        "Grasp of Avarice": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "graspofavarice",
        },
        "Prophecy": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "prophecy",
        },
        "Pit of Heresy": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "pitofheresy",
        },
        "The Shattered Throne": {
            "Clears": 0,
            "Launches": 0,
            "Time": 0,
            "Solo": 0,
            "Solo Flawless": 0,
            "Kills": 0,
            "Deaths": 0,
            "KD": 0,
            "Image": "shatteredthrone",
        },
    }
    return dictionary


def clean_data(data_list):
    dun_dict = dungeon_dictionary()
    dungeon_name = ""
    for page in data_list:
        instances = page["activities"]
        for instance in instances:
            reference_id = instance["activityDetails"]["referenceId"]
            if reference_id == 2032534090:
                dungeon_name = "The Shattered Throne"
            elif reference_id == 2582501063 or reference_id == 1375089621:
                dungeon_name = "Pit of Heresy"
            elif reference_id == 4148187374 or reference_id == 1077850348:
                dungeon_name = "Prophecy"
            elif reference_id == 4078656646 or reference_id == 3774021532:
                dungeon_name = "Grasp of Avarice"
            elif reference_id == 2823159265 or reference_id == 1668217731 or reference_id == 3012587626:
                dungeon_name = "Duality"
            elif reference_id == 1262462921 or reference_id == 1801496203 or reference_id == 2296818662:
                dungeon_name = "Spire of the Watcher"
            elif reference_id == 313828469 or reference_id == 2716998124:
                dungeon_name = "Ghosts of the Deep"
            elif reference_id == 2004855007 or reference_id == 2534833093:
                dungeon_name = "Warlord's Ruin"
            else:
                print(f"Unrecognized reference id: {reference_id}")
                print("DROWNDROWNDROWN")
                continue
            dun_dict[dungeon_name]["Launches"] += 1
            dun_dict[dungeon_name]["Kills"] += instance["values"]["kills"]["basic"]["value"]
            dun_dict[dungeon_name]["Deaths"] += instance["values"]["deaths"]["basic"]["value"]
            dun_dict[dungeon_name]["Clears"] += instance["values"]["completed"]["basic"]["value"]
            dun_dict[dungeon_name]["Time"] += instance["values"]["activityDurationSeconds"]["basic"]["value"]
            dun_dict["Total"]["Launches"] += 1
            dun_dict["Total"]["Kills"] += instance["values"]["kills"]["basic"]["value"]
            dun_dict["Total"]["Deaths"] += instance["values"]["deaths"]["basic"]["value"]
            dun_dict["Total"]["Clears"] += instance["values"]["completed"]["basic"]["value"]
            dun_dict["Total"]["Time"] += instance["values"]["activityDurationSeconds"]["basic"]["value"]
            
            #Need to check for fresh start?
            if instance["values"]["completed"]["basic"]["value"] == 1 and instance["values"]["playerCount"]["basic"]["value"] <= 1:
                dun_dict[dungeon_name]["Solo"] += 1
                dun_dict["Total"]["Solo"] += 1
                if instance["values"]["deaths"]["basic"]["value"] == 0:
                    dun_dict[dungeon_name]["Solo Flawless"] += 1
                    dun_dict["Total"]["Solo Flawless"] += 1
                    

    for dungeon in dun_dict:
        if dun_dict[dungeon]["Deaths"] > 0:
            dun_dict[dungeon]["KD"] = round(dun_dict[dungeon]["Kills"]/dun_dict[dungeon]["Deaths"], 2)
    return dun_dict
            
            
            
def generate_html(dun_data):

    html_string = "<div class=flexContainer>"
    for dungeon in dun_data:
        if dungeon == "Total":
            html_string += f"""
            <div class="dungeonBox">
                <h1>{dungeon}</h1>
                <h2>Clears: {int(dun_data[dungeon]["Clears"])}</h2>
                <p>Launches: {int(dun_data[dungeon]["Launches"])}</p>
                <p>Solos: {int(dun_data[dungeon]["Solo"])}</p>
                <p>Solo Flawless: {int(dun_data[dungeon]["Solo Flawless"])}</p>
                <p>Kills: {int(dun_data[dungeon]["Kills"])}</p>
                <p>Deaths: {int(dun_data[dungeon]["Deaths"])}</p>
                <p>K/D: {dun_data[dungeon]["KD"]}</p>
                <p>Time played: {Time_Converter(dun_data[dungeon]["Time"])}</p>
            </div>
            """
        else:
            html_string += f"""
            <div class="dungeonBox">
                <img src="../images/{dun_data[dungeon]["Image"]}.jpg">
            """
            if dun_data[dungeon]["Solo"] >= 1 and dun_data[dungeon]["Solo Flawless"] == 0:
                html_string += '<p class="soloTag">Solo</p>'
            
            if dun_data[dungeon]["Solo Flawless"] >= 1:
                html_string += '<p class="soloFlawlessTag">Solo Flawless</p>'
            
            html_string += f"""
                <h1>{dungeon}</h1>
                <h2>Clears: {int(dun_data[dungeon]["Clears"])}</h2>
                <p>Launches: {int(dun_data[dungeon]["Launches"])}</p>
                <p>Solos: {int(dun_data[dungeon]["Solo"])}</p>
                <p>Solo Flawless: {int(dun_data[dungeon]["Solo Flawless"])}</p>
                <p>Kills: {int(dun_data[dungeon]["Kills"])}</p>
                <p>Deaths: {int(dun_data[dungeon]["Deaths"])}</p>
                <p>K/D: {dun_data[dungeon]["KD"]}</p>
                <p>Time played: {Time_Converter(dun_data[dungeon]["Time"])}</p>
            </div>
            """
    html_string += "</div>"
    return html_string
            
def write_to_directory(data, name):
    f = open(f"./data/{name}DungeonReport.html", "w")
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

    .dungeonBox {
        border-radius: 10px;
        background-color: rgb(75, 75, 75);
        margin: 15px;
        flex: 25%;
    }
    .dungeonBox h2,
    .dungeonBox p {
        padding: 0 15px;
    }
    .dungeonBox>div {
        height: 10em;
        background-size:contain;
        background-repeat: no-repeat;
        margin:0 40px;
    }
    h1 {
        text-align: center;
    }
    .dungeonBox>img {
        border-radius: 10px 10px 0 0;
        width:100%;
    }
    .soloTag,
    .soloFlawlessTag {
        background-color: goldenrod;
        border-radius: 2px;
        width:fit-content;
        margin-left: 10px;
    }
</style>
    """
    )
    f.write(data)
    f.close()
    print(f"{name} dungeon report data written!")
                 
def process_player(name, mem_type, mem_id, char_id_1, char_id_2, char_id_3):

    raw_data_list = get_dungeon_data(
        mem_type=mem_type,
        mem_id=mem_id,
        char_id_1=char_id_1,
        char_id_2=char_id_2,
        char_id_3=char_id_3,
    )
    clean_data_dict = clean_data(raw_data_list)
    html_string = generate_html(clean_data_dict)
    write_to_directory(data=html_string, name=name)
    return clean_data_dict

def compile_clan(player_data_list):
    dun_dict = dungeon_dictionary() 
    for player in player_data_list:
        for dungeon in dun_dict:
            dun_dict[dungeon]["Time"] += player[dungeon]["Time"]
            dun_dict[dungeon]["Launches"] += player[dungeon]["Launches"]
            dun_dict[dungeon]["Clears"] += player[dungeon]["Clears"]
            dun_dict[dungeon]["Kills"] += player[dungeon]["Kills"]
            dun_dict[dungeon]["Deaths"] += player[dungeon]["Deaths"]
            dun_dict[dungeon]["Solo"] += player[dungeon]["Solo"]
            dun_dict[dungeon]["Solo Flawless"] += player[dungeon]["Solo Flawless"]
            
            
    for dungeon in dun_dict:
        if dun_dict[dungeon]["Deaths"] > 0:
            dun_dict[dungeon]["KD"] = round(dun_dict[dungeon]["Kills"]/dun_dict[dungeon]["Deaths"], 2)

    html_string = "<div class=flexContainer>"
    for dungeon in dun_dict:
        if dungeon == "Total":
            html_string += f"""
            <div class="dungeonBox">
                <h1>{dungeon}</h1>
                <h2>Clears: {int(dun_dict[dungeon]["Clears"])}</h2>
                <p>Launches: {int(dun_dict[dungeon]["Launches"])}</p>
                <p>Solos: {int(dun_dict[dungeon]["Solo"])}</p>
                <p>Solo Flawless: {int(dun_dict[dungeon]["Solo Flawless"])}</p>
                <p>Kills: {int(dun_dict[dungeon]["Kills"])}</p>
                <p>Deaths: {int(dun_dict[dungeon]["Deaths"])}</p>
                <p>K/D: {dun_dict[dungeon]["KD"]}</p>
                <p>Time played: {Time_Converter(dun_dict[dungeon]["Time"])}</p>
            </div>
            """
        else:
            html_string += f"""
            <div class="dungeonBox">
                <img src="../images/{dun_dict[dungeon]["Image"]}.jpg">
            """
            if dun_dict[dungeon]["Solo"] >= 1 and dun_dict[dungeon]["Solo Flawless"] == 0:
                html_string += '<p class="soloTag">Solo</p>'
            
            if dun_dict[dungeon]["Solo Flawless"] >= 1:
                html_string += '<p class="soloFlawlessTag">Solo Flawless</p>'
            
            html_string += f"""
                <h1>{dungeon}</h1>
                <h2>Clears: {int(dun_dict[dungeon]["Clears"])}</h2>
                <p>Launches: {int(dun_dict[dungeon]["Launches"])}</p>
                <p>Solos: {int(dun_dict[dungeon]["Solo"])}</p>
                <p>Solo Flawless: {int(dun_dict[dungeon]["Solo Flawless"])}</p>
                <p>Kills: {int(dun_dict[dungeon]["Kills"])}</p>
                <p>Deaths: {int(dun_dict[dungeon]["Deaths"])}</p>
                <p>K/D: {dun_dict[dungeon]["KD"]}</p>
                <p>Time played: {Time_Converter(dun_dict[dungeon]["Time"])}</p>
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
    
run()
