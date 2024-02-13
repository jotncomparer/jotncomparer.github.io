# Thomas McGinley
# Started 2/1/2024
# Last Updated 2/9/2024

# Gets character emblems


import json
import requests


def get_character_data(membership_type, member_id):
    url = f"https://www.bungie.net/Platform/Destiny2/{membership_type}/Profile/{member_id}/?components=200"
    payload = {}
    headers = {
        "x-api-key": "654dad1171c44eb688f2fb5ca11e7c3b",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()
    characterData = json.loads(response.content)
    return characterData

def get_emblem_data(emblem_hash):
    url = f"https://www.bungie.net/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/{emblem_hash}/"
    payload = {}
    headers = {
        "x-api-key": "654dad1171c44eb688f2fb5ca11e7c3b",
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code not in range(200, 300):
                print("Error occurred in request:", response.status_code)
                print("She be Rhulking on my Disciple til I Strand")
                quit()
    emblem_data = json.loads(response.content)
    return emblem_data

def process_player(name, membership_type, member_id, character_id):
    data = get_character_data(membership_type=membership_type, member_id=member_id)
    emblem_hash = data["Response"]["characters"]["data"][str(character_id)]["emblemHash"]
    emblem_data = get_emblem_data(emblem_hash=emblem_hash)
    
    emblem_overlay_url = emblem_data["Response"]["secondaryOverlay"]
    emblem_overlay = requests.get(url=f"https://www.bungie.net{emblem_overlay_url}").content
    emblem_overlay_file_hand = open(file=f"./images/{name}EmblemOverlay.png", mode="wb")
    emblem_overlay_file_hand.write(emblem_overlay)
    emblem_overlay_file_hand.close()
    
    emblem_background_url = emblem_data["Response"]["secondarySpecial"]
    emblem_background = requests.get(url=f"http://www.bungie.net{emblem_background_url}").content
    emblem_background_file_hand = open(file=f"./images/{name}Emblem.jpg", mode="wb")
    emblem_background_file_hand.write(emblem_background)
    emblem_background_file_hand.close()
    print(f"{name} emblems processed!")

def run():    
    process_player("Thomas", 1, 4611686018444441571, 2305843009265786295)
    process_player("Douglas", 1, 4611686018434621591, 2305843010083874501)
    process_player("Mark", 1, 4611686018432221111, 2305843009668854600)
    process_player("Connor", 1, 4611686018450697084, 2305843009644414176)
    process_player("Jack", 2, 4611686018469231992, 2305843009268771475)
    process_player("Hunter", 3, 4611686018476416864, 2305843009359734078)
    process_player("Cameron", 3, 4611686018501646188, 2305843009683284493)
    process_player("Kade", 1, 4611686018451886498, 2305843009264637524)
    process_player("Xavier", 3, 4611686018471574419, 2305843009306625517)
