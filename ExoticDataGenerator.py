# Thomas McGinley
# Started 12/17/2023
# Last Updated 3/3/2024

# Gathers exotic information about each desired player, cleans the data, and generates JSON files with relevant information

from APIKEY import API_KEY
import json
import requests
import prettytable


def get_weapon_from_hash(hash):
    hash_dictionary = {
        1345867570: "Sweet Business",
        2907129556: "Sturm",
        3628991659: "Vigilance Wing",
        2362471601: "Rat King",
        1331482397: "MIDA Multi-Tool",
        3437746471: "Crimson",
        3844694310: "Jade Rabbit",
        2286143274: "Huckleberry",
        2856683562: "SUROS Regime",
        1541131350: "Cerberus+1",
        814876684: "Wish Ender",
        204878059: "Malfeasance",
        347366834: "Ace of Spades",
        3413860062: "The Chaperone",
        3211806999: "Izanagi's Burden",
        1364093401: "The Last Word",
        2130065553: "Arbalest",
        3973202132: "Thorn",
        400096939: "Outbreak Perfected",
        3512014804: "Lumina",
        2816212794: "Bad Juju",
        4068264807: "Monte Carlo",
        2415517654: "Bastion",
        2357297366: "Witherhoard",
        1853180924: "Traveler's Chosen",
        1594120904: "No Time to Explain",
        3654674561: "Dead Man's Tale",
        603721696: "Cryosthethesia 77K",
        1833195496: "Ager's Scepter",
        2179048386: "Forerunner",
        46524085: "Osteo Striga",
        1802135586: "Touch of Malice",
        4293613902: "Quicksilver Storm",
        1473821207: "Revision Zero",
        3121540812: "Final Warning",
        3371017761: "Conditional Finality",
        3659414143: "Verglas Curve",
        940371471: "Wicked Implement",
        1441805468: "The Navigator",
        1345867571: "Coldheart",
        4190156464: "Merciless",
        3549153978: "Fighting Lion",
        2907129557: "Sunshot",
        3628991658: "Graviton Lance",
        4255268456: "Skyburner's Oath",
        3141979347: "Borealis",
        3089417789: "Riskrunner",
        4124984448: "Hard Light",
        19024058: "Prometheus Lens",
        2208405142: "Telesto",
        3413074534: "Polaris Lance",
        814876685: "Trinity Ghoul",
        1852863732: "Wavesplitter",
        3413860063: "Lord of Wolves",
        3588934839: "Le Monarque",
        417164956: "Jotunn",
        3110698812: "Tarrabah",
        3524313097: "Eriana's Vow",
        4103414242: "Divinity",
        4017959782: "Symmetry",
        3824106094: "Devil's Ruin",
        776191470: "Tommy's Matchbook",
        1665952087: "The Fourth Horseman",
        1363238943: "Ruinous Effigy",
        3460576091: "Duality",
        2603483885: "Cloudstrike",
        3260753130: "Ticuu's Divination",
        4289226715: "Vex Mythoclast",
        3761898871: "Lorentz Driver",
        14194600: "Edge of Intent",
        2812324401: "Dead Messenger",
        3505113722: "Collective Obligation",
        374573733: "Delicate Tomb",
        1234150730: "Trespasser",
        219145368: "The Manticore",
        4174431791: "Hierarchy of Needs",
        3118061005: "Vexcalibur",
        1912669214: "Centrifuse",
        1508896098: "Wardcliff Coil",
        3580904581: "Tractor Cannon",
        3580904580: "Legend of Acrius",
        1744115122: "Legend of Acrius",
        3141979346: "D.A.R.C.I",
        3899270607: "The Colony",
        1864563948: "Worldline Zero",
        4036115577: "Sleeper Simulant",
        2069224589: "One Thousand Voices",
        2694576561: "Two-Tailed Fox",
        3766045777: "Black Talon",
        2044500762: "The Queenbreaker",
        3325463374: "Thunderlord",
        2376481550: "Anarchy",
        2591746970: "Leviathan's Breath",
        1395261499: "Xenophage",
        2232171099: "Deathbringer",
        2084878005: "Heir Apparent",
        370712896: "Salvation's Grip",
        2399110176: "Eyes of Tomorrow",
        3487253372: "Lament",
        1363886209: "Gjallarhorn",
        2812324400: "Parasite",
        1763584999: "Grand Overture",
        3664831848: "Heartshadow",
        449318888: "Deterministic Chaos",
        3118061004: "Winterbite",
        1201830623: "Truth",
        1891561814: "Whisper of the Worm",
        17096506: "Dragon's Breath",
        3561203890: "Tessellation",
        3886719505: "Buried Bloodline",
        1034055198: "Necrochasm",
        3821409356: "Ex Diris",
        3856705927: "Hawkmoon",
        3549153979: "The Prospector",
        2188764214: "Dead Man's Tale",
        2910326942: "Wish-Keeper",
    }
    return hash_dictionary.get(hash)


def weapon_data():
    dictionary = {
        "Sweet Business": {"kills": 0, "precision": 0},
        "Sturm": {"kills": 0, "precision": 0},
        "Vigilance Wing": {"kills": 0, "precision": 0},
        "Rat King": {"kills": 0, "precision": 0},
        "MIDA Multi-Tool": {"kills": 0, "precision": 0},
        "Crimson": {"kills": 0, "precision": 0},
        "Jade Rabbit": {"kills": 0, "precision": 0},
        "Huckleberry": {"kills": 0, "precision": 0},
        "SUROS Regime": {"kills": 0, "precision": 0},
        "Cerberus+1": {"kills": 0, "precision": 0},
        "Wish Ender": {"kills": 0, "precision": 0},
        "Malfeasance": {"kills": 0, "precision": 0},
        "Ace of Spades": {"kills": 0, "precision": 0},
        "The Chaperone": {"kills": 0, "precision": 0},
        "Izanagi's Burden": {"kills": 0, "precision": 0},
        "The Last Word": {"kills": 0, "precision": 0},
        "Arbalest": {"kills": 0, "precision": 0},
        "Thorn": {"kills": 0, "precision": 0},
        "Outbreak Perfected": {"kills": 0, "precision": 0},
        "Lumina": {"kills": 0, "precision": 0},
        "Bad Juju": {"kills": 0, "precision": 0},
        "Monte Carlo": {"kills": 0, "precision": 0},
        "Bastion": {"kills": 0, "precision": 0},
        "Witherhoard": {"kills": 0, "precision": 0},
        "Traveler's Chosen": {"kills": 0, "precision": 0},
        "No Time to Explain": {"kills": 0, "precision": 0},
        "Dead Man's Tale": {"kills": 0, "precision": 0},
        "Cryosthethesia 77K": {"kills": 0, "precision": 0},
        "Ager's Scepter": {"kills": 0, "precision": 0},
        "Forerunner": {"kills": 0, "precision": 0},
        "Osteo Striga": {"kills": 0, "precision": 0},
        "Touch of Malice": {"kills": 0, "precision": 0},
        "Quicksilver Storm": {"kills": 0, "precision": 0},
        "Revision Zero": {"kills": 0, "precision": 0},
        "Final Warning": {"kills": 0, "precision": 0},
        "Conditional Finality": {"kills": 0, "precision": 0},
        "Verglas Curve": {"kills": 0, "precision": 0},
        "Wicked Implement": {"kills": 0, "precision": 0},
        "The Navigator": {"kills": 0, "precision": 0},
        "Coldheart": {"kills": 0, "precision": 0},
        "Merciless": {"kills": 0, "precision": 0},
        "Fighting Lion": {"kills": 0, "precision": 0},
        "Sunshot": {"kills": 0, "precision": 0},
        "Graviton Lance": {"kills": 0, "precision": 0},
        "Skyburner's Oath": {"kills": 0, "precision": 0},
        "Borealis": {"kills": 0, "precision": 0},
        "Riskrunner": {"kills": 0, "precision": 0},
        "Hard Light": {"kills": 0, "precision": 0},
        "Prometheus Lens": {"kills": 0, "precision": 0},
        "Telesto": {"kills": 0, "precision": 0},
        "Polaris Lance": {"kills": 0, "precision": 0},
        "Trinity Ghoul": {"kills": 0, "precision": 0},
        "Wavesplitter": {"kills": 0, "precision": 0},
        "Lord of Wolves": {"kills": 0, "precision": 0},
        "Le Monarque": {"kills": 0, "precision": 0},
        "Jotunn": {"kills": 0, "precision": 0},
        "Tarrabah": {"kills": 0, "precision": 0},
        "Eriana's Vow": {"kills": 0, "precision": 0},
        "Divinity": {"kills": 0, "precision": 0},
        "Symmetry": {"kills": 0, "precision": 0},
        "Devil's Ruin": {"kills": 0, "precision": 0},
        "Tommy's Matchbook": {"kills": 0, "precision": 0},
        "The Fourth Horseman": {"kills": 0, "precision": 0},
        "Ruinous Effigy": {"kills": 0, "precision": 0},
        "Duality": {"kills": 0, "precision": 0},
        "Cloudstrike": {"kills": 0, "precision": 0},
        "Ticuu's Divination": {"kills": 0, "precision": 0},
        "Vex Mythoclast": {"kills": 0, "precision": 0},
        "Lorentz Driver": {"kills": 0, "precision": 0},
        "Edge of Intent": {"kills": 0, "precision": 0},
        "Dead Messenger": {"kills": 0, "precision": 0},
        "Collective Obligation": {"kills": 0, "precision": 0},
        "Delicate Tomb": {"kills": 0, "precision": 0},
        "Trespasser": {"kills": 0, "precision": 0},
        "The Manticore": {"kills": 0, "precision": 0},
        "Hierarchy of Needs": {"kills": 0, "precision": 0},
        "Vexcalibur": {"kills": 0, "precision": 0},
        "Centrifuse": {"kills": 0, "precision": 0},
        "Wardcliff Coil": {"kills": 0, "precision": 0},
        "Tractor Cannon": {"kills": 0, "precision": 0},
        "Legend of Acrius": {"kills": 0, "precision": 0},
        "D.A.R.C.I": {"kills": 0, "precision": 0},
        "The Colony": {"kills": 0, "precision": 0},
        "Worldline Zero": {"kills": 0, "precision": 0},
        "Sleeper Simulant": {"kills": 0, "precision": 0},
        "One Thousand Voices": {"kills": 0, "precision": 0},
        "Two-Tailed Fox": {"kills": 0, "precision": 0},
        "Black Talon": {"kills": 0, "precision": 0},
        "The Queenbreaker": {"kills": 0, "precision": 0},
        "Thunderlord": {"kills": 0, "precision": 0},
        "Anarchy": {"kills": 0, "precision": 0},
        "Leviathan's Breath": {"kills": 0, "precision": 0},
        "Xenophage": {"kills": 0, "precision": 0},
        "Deathbringer": {"kills": 0, "precision": 0},
        "Heir Apparent": {"kills": 0, "precision": 0},
        "Salvation's Grip": {"kills": 0, "precision": 0},
        "Eyes of Tomorrow": {"kills": 0, "precision": 0},
        "Lament": {"kills": 0, "precision": 0},
        "Gjallarhorn": {"kills": 0, "precision": 0},
        "Parasite": {"kills": 0, "precision": 0},
        "Grand Overture": {"kills": 0, "precision": 0},
        "Heartshadow": {"kills": 0, "precision": 0},
        "Deterministic Chaos": {"kills": 0, "precision": 0},
        "Winterbite": {"kills": 0, "precision": 0},
        "Truth": {"kills": 0, "precision": 0},
        "Whisper of the Worm": {"kills": 0, "precision": 0},
        "Dragon's Breath": {"kills": 0, "precision": 0},
        "Tessellation": {"kills": 0, "precision": 0},
        "Buried Bloodline": {"kills": 0, "precision": 0},
        "Necrochasm": {"kills": 0, "precision": 0},
        "Ex Diris": {"kills": 0, "precision": 0},
        "Hawkmoon": {"kills": 0, "precision": 0},
        "The Prospector": {"kills": 0, "precision": 0},
        "Wish-Keeper": {"kills": 0, "precision": 0},
    }
    return dictionary


def get_exotic_data(mem_type, mem_id, char_id_1, char_id_2, char_id_3):
    char_ids = [char_id_1, char_id_2, char_id_3]
    combined_exotic_data = {"Response": []}
    for char_id in char_ids:
        url = (
            f"https://www.bungie.net/Platform/Destiny2/{mem_type}/Account/{mem_id}/Character/"
            f"{char_id}/Stats/UniqueWeapons/"
        )
        payload = {}
        header = API_KEY
        response = requests.request("GET", url, headers=header, data=payload)
        if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()
        exotic_data = json.loads(response.content)

        combined_exotic_data["Response"].append(exotic_data["Response"])
    return combined_exotic_data


def compile_data(exotic_data):
    data_dictionary = weapon_data()
    # exoticData["Response"][value 0-2]["weapons"][num]["referenceId"] = reference Id
    # exoticData["Response"][charNum]["weapons"][num]["values"]["uniqueWeaponKills"]["basic"]["value"] = kills
    # exoticData["Response"][charNum]["weapons"][num]["values"]["uniqueWeaponPrecisionKills"]["basic"]["value"] = precision kills
    for char_num in range(0, 3):
        weapon_count = len(exotic_data["Response"][char_num]["weapons"])
        for num in range(0, weapon_count):
            exotic_name = get_weapon_from_hash(
                exotic_data["Response"][char_num]["weapons"][num]["referenceId"]
            )
            exotic_kills = exotic_data["Response"][char_num]["weapons"][num]["values"][
                "uniqueWeaponKills"
            ]["basic"]["value"]
            exotic_precision = exotic_data["Response"][char_num]["weapons"][num]["values"][
                "uniqueWeaponPrecisionKills"
            ]["basic"]["value"]
            # print(str(exoticName) + "\t" + str(exoticData["Response"][charNum]["weapons"][num]['referenceId']))
            # print(exoticKills)
            # print(exoticPrecision)

            data_dictionary[exotic_name]["kills"] += exotic_kills
            data_dictionary[exotic_name]["precision"] += exotic_precision
    return data_dictionary


def compile_clan_data(player_data_list):
    data_dictionary = weapon_data()

    for player in player_data_list:
        for exotic_name in player:
            exotic_kills = player[exotic_name]["kills"]
            exotic_precision = player[exotic_name]["precision"]

            data_dictionary[exotic_name]["kills"] += exotic_kills
            data_dictionary[exotic_name]["precision"] += exotic_precision
    return data_dictionary


def write_to_directory(data, name):
    f = open(f"./data/{name}Exotics.html", "w")
    f.write(
        """<style>
    @font-face {
    font-family: JetBrains Mono;
    src: url("../fonts/JetBrainsMono-Regular.ttf");
    }
    
    h1,
    h2 {
        color: white;
        font-family: "JetBrains Mono", 'Courier New', Courier, monospace
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

    tbody>tr:nth-of-type(1) {
        background-color:gold;
        color:black;
    }

    tbody>tr:nth-of-type(2) {
        background-color:silver;
        color:black;
    }

    tbody>tr:nth-of-type(3) {
        background-color:chocolate;
        color:black;
    }

    th,
    td {
        border-bottom: 1px solid white
    }
    
    tbody>tr>td:nth-of-type(n+1){
        text-align:end;
    }
</style>"""
    )
    f.write(f"<h1>{str(name).replace('10','').upper()} EXOTICS</h1>")
    f.write(data)
    f.close()


def generate_table(data):
    table = prettytable.PrettyTable()
    table.field_names = ["Weapon", "Kills", "Precision Kills"]

    for exoticName in data:
        exoticKills = int(data[exoticName]["kills"])
        exoticPrecision = int(data[exoticName]["precision"])

        table.add_row([exoticName, exoticKills, exoticPrecision])

    table.sortby = "Kills"
    table.reversesort = True

    return table.get_html_string()


def generate_top_ten(data):
    table = prettytable.PrettyTable()
    table.field_names = ["Weapon", "Kills", "Precision Kills"]
    for exoticName in data:
        exoticKills = int(data[exoticName]["kills"])
        exoticPrecision = int(data[exoticName]["precision"])

        table.add_row([exoticName, exoticKills, exoticPrecision])

    table.sortby = "Kills"
    table.reversesort = True
    return table.get_html_string(start=0, end=10)


def process_player(name, mem_type, mem_id, char_id_1, char_id_2, char_id_3):
    rawData = get_exotic_data(mem_type, mem_id, char_id_1, char_id_2, char_id_3)
    cleanData = compile_data(rawData)
    table = generate_table(cleanData)
    write_to_directory(table, name)
    ten = generate_top_ten(cleanData)
    write_to_directory(ten, str(name + "10"))
    print(name + " exotic data written!")
    return cleanData

def run():
    thomasExoticDataClean = process_player(
        "Thomas",
        1,
        4611686018444441571,
        2305843009265786295,
        2305843009283965144,
        2305843009569534739,
    )
    douglasExoticDataClean = process_player(
        "Douglas",
        1,
        4611686018434621591,
        2305843009293915719,
        2305843009301374530,
        2305843010083874501,
    )
    markExoticDataClean = process_player(
        "Mark",
        1,
        4611686018432221111,
        2305843009348154555,
        2305843009668854600,
        2305843009802904121,
    )
    connorExoticDataClean = process_player(
        "Connor",
        1,
        4611686018450697084,
        2305843009644414176,
        2305843009663894341,
        2305843009703275457,
    )
    jackExoticDataClean = process_player(
        "Jack",
        2,
        4611686018469231992,
        2305843009268771475,
        2305843009891864023,
        2305843009890274343,
    )
    hunterExoticDataClean = process_player(
        "Hunter",
        3,
        4611686018476416864,
        2305843009359734078,
        2305843009359365362,
        2305843009756404411,
    )
    cameronExoticDataClean = process_player(
        "Cameron",
        3,
        4611686018501646188,
        2305843009624174508,
        2305843009683284492,
        2305843009683284493,
    )
    kadeExoticDataClean = process_player(
        "Kade",
        1,
        4611686018451886498,
        2305843009264637524,
        2305843009264637527,
        2305843010322954573,
    )
    xavierExoticDataClean = process_player(
        "Xavier",
        3,
        4611686018471574419,
        2305843009306625517,
        2305843009309817521,
        2305843009313885640,
    )

    playerDataList = [
        thomasExoticDataClean,
        douglasExoticDataClean,
        markExoticDataClean,
        connorExoticDataClean,
        jackExoticDataClean,
        hunterExoticDataClean,
        cameronExoticDataClean,
        kadeExoticDataClean,
        xavierExoticDataClean,
    ]
    
def compile_clan(player_data_list):
    clanExoticDataClean = compile_clan_data(player_data_list)
    clanTable = generate_table(clanExoticDataClean)
    write_to_directory(clanTable, "Clan")
    indexTable = generate_top_ten(clanExoticDataClean)
    write_to_directory(indexTable, "Clan10")
    print("Clan cleared!")
