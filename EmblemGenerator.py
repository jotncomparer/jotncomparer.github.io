# Thomas McGinley
# Started 2/1/2024
# Last Updated 2/1/2024

# Gets character emblems


import json
import requests

def get_character_data(memType, memId):
    url = f"https://www.bungie.net/Platform/Destiny2/{memType}/Profile/{memId}/?components=200"
    payload = {}
    headers = {
        'x-api-key': '654dad1171c44eb688f2fb5ca11e7c3b',
    }
    response = requests.request("GET",url, headers=headers, data=payload)
    characterData = json.loads(response.content)
    return characterData

def process_player(name, memType, memId, charId1, charId2, charId3):
    data = get_character_data(memType=memType, memId=memId)
    
    emblem_path_1 = data["Response"]["characters"]["data"][str(charId1)]["emblemPath"]
    emblem_img_1 = requests.get(url=f"https://www.bungie.net{emblem_path_1}").content
    emblem_file_1 = open(file=f"./images/{name}Emblem1.jpg",mode='wb')
    emblem_file_1.write(emblem_img_1)
    emblem_file_1.close()
    
    emblem_path_2 = data["Response"]["characters"]["data"][str(charId2)]["emblemPath"]
    emblem_img_2 = requests.get(url=f"https://www.bungie.net{emblem_path_2}").content
    emblem_file_2 = open(file=f"./images/{name}Emblem2.jpg",mode='wb')
    emblem_file_2.write(emblem_img_2)
    emblem_file_2.close()
    
    emblem_path_3 = data["Response"]["characters"]["data"][str(charId3)]["emblemPath"]
    emblem_img_3 = requests.get(url=f"https://www.bungie.net{emblem_path_3}").content
    emblem_file_3 = open(file=f"./images/{name}Emblem3.jpg",mode='wb')
    emblem_file_3.write(emblem_img_3)
    emblem_file_3.close()
    
process_player("Thomas",1,4611686018444441571,2305843009265786295,2305843009283965144,2305843009569534739) 
process_player("Douglas",1,4611686018434621591,2305843009293915719,2305843009301374530,2305843010083874501)
process_player("Mark",1,4611686018432221111,2305843009348154555,2305843009668854600,2305843009802904121)
process_player("Connor",1,4611686018450697084,2305843009644414176,2305843009663894341,2305843009703275457)
process_player("Jack",2,4611686018469231992,2305843009268771475,2305843009891864023,2305843009890274343)
process_player("Hunter",3,4611686018476416864,2305843009359734078,2305843009359365362,2305843009756404411)
process_player("Cameron",3,4611686018501646188,2305843009624174508,2305843009683284492,2305843009683284493)
process_player("Kade",1,4611686018451886498,2305843009264637524,2305843009264637527,2305843010322954573)