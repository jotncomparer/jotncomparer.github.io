# Thomas McGinley
# Started 2/6/2024
# Last updated 2/9/2024

# Acts as central access point to run the scripts
import CommendationDataGenerator
import DungeonDataGenerator
import ElementalDataGenerator
import EmblemGenerator
import ExoticDataGenerator
import FishDataGenerator
import RaidDataGenerator
import RaidCatalyst
import StrikeDataGenerator
import WeaponDataGenerator
from time import sleep

class Player:
    def __init__(
        self,
        name,
        member_type,
        member_id,
        character_id_main,
        character_id_2,
        character_id_3,
    ):
        self.name = name
        self.member_type = member_type
        self.member_id = member_id
        self.character_id_main = character_id_main
        self.character_id_2 = character_id_2
        self.character_id_3 = character_id_3

    def process(self):
        player_data = {
            "Commendations": None,
            "Fishing": None,
            "Weapons": None,
            "Elements": None,
            "Strikes": None,
            "Dungeons": None,
            "Raids": None,
            "Exotics": None,
            "RaidReport":None,
        }
        EmblemGenerator.process_player(
            name=self.name,
            membership_type=self.member_type,
            member_id=self.member_id,
            character_id=self.character_id_main,
        )

        player_data["Commendations"] = CommendationDataGenerator.process_player(
            name=self.name, mem_type=self.member_type, mem_id=self.member_id
        )

        player_data["Fishing"] = FishDataGenerator.process_player(
            name=self.name, mem_id=self.member_id, mem_type=self.member_type
        )

        player_data["Weapons"] = WeaponDataGenerator.process_player(
            name=self.name, mem_id=self.member_id, mem_type=self.member_type
        )

        player_data["Elements"] = ElementalDataGenerator.process_player(
            name=self.name, mem_id=self.member_id, mem_type=self.member_type
        )

        player_data["Strikes"] = StrikeDataGenerator.process_player(
            name=self.name, mem_id=self.member_id, mem_type=self.member_type
        )

        player_data["Dungeons"] = DungeonDataGenerator.process_player(
            name=self.name, mem_id=self.member_id, mem_type=self.member_type
        )

        player_data["Raids"] = RaidDataGenerator.process_player(
            name=self.name, mem_id=self.member_id, mem_type=self.member_type
        )

        player_data["Exotics"] = ExoticDataGenerator.process_player(
            name=self.name,
            mem_id=self.member_id,
            mem_type=self.member_type,
            char_id_1=self.character_id_main,
            char_id_2=self.character_id_2,
            char_id_3=self.character_id_3,
        )

        player_data["RaidReport"] = RaidCatalyst.process_player(
            name=self.name,
            mem_id=self.member_id,
            mem_type=self.member_type,
            char_id_1=self.character_id_main,
            char_id_2=self.character_id_2,
            char_id_3=self.character_id_3,
        )
        
        return player_data


def process_players():
    player_data_list = []
    
    Thomas = Player(
        name="Thomas",
        member_type=1,
        member_id=4611686018444441571,
        character_id_main=2305843009265786295,
        character_id_2=2305843009283965144,
        character_id_3=2305843009569534739,
    )
    player_data_list.append(Thomas.process())
    sleep(15)
    
    Douglas = Player(
        name="Douglas",
        member_type=1,
        member_id=4611686018434621591,
        character_id_main=2305843010083874501,
        character_id_2=2305843009293915719,
        character_id_3=2305843009301374530,
    )
    player_data_list.append(Douglas.process())
    sleep(15)

    Mark = Player(
        name="Mark",
        member_type=1,
        member_id=4611686018432221111,
        character_id_main=2305843009668854600,
        character_id_2=2305843009348154555,
        character_id_3=2305843009802904121,
    )
    player_data_list.append(Mark.process())
    sleep(15)
    
    Connor = Player(
        name="Connor",
        member_type=1,
        member_id=4611686018450697084,
        character_id_main=2305843009644414176,
        character_id_2=2305843009663894341,
        character_id_3=2305843009703275457,
    )
    player_data_list.append(Connor.process())
    sleep(15)
    
    Jack = Player(
        name="Jack",
        member_type=2,
        member_id=4611686018469231992,
        character_id_main=2305843009268771475,
        character_id_2=2305843009891864023,
        character_id_3=2305843009890274343,
    )
    player_data_list.append(Jack.process())
    sleep(15)
    
    Hunter = Player(
        name="Hunter",
        member_type=3,
        member_id=4611686018476416864,
        character_id_main=2305843009359734078,
        character_id_2=2305843009359365362,
        character_id_3=2305843009756404411,
    )
    player_data_list.append(Hunter.process())
    sleep(15)
    
    Cameron = Player(
        name="Cameron",
        member_type=3,
        member_id=4611686018501646188,
        character_id_main=2305843009683284493,
        character_id_2=2305843009683284492,
        character_id_3=2305843009624174508,
    )
    player_data_list.append(Cameron.process())
    sleep(15)
    
    Kade = Player(
        name="Kade",
        member_type=1,
        member_id=4611686018451886498,
        character_id_main=2305843009264637524,
        character_id_2=2305843009264637527,
        character_id_3=2305843010322954573,
    )
    player_data_list.append(Kade.process())
    sleep(15)
    
    Xavier = Player(
        name="Xavier",
        member_type=3,
        member_id=4611686018471574419,
        character_id_main=2305843009306625517,
        character_id_2=2305843009309817521,
        character_id_3=2305843009313885640,
    )
    player_data_list.append(Xavier.process())
    sleep(15)
    
    return player_data_list

def process_clan(player_data_list):
    commendation_data = []
    fishing_data = []
    weapons_data = []
    elements_data = []
    strikes_data = []
    dungeons_data = []
    raids_data = []
    exotic_data = []
    raid_report_data = []
    
    for player in player_data_list:
        commendation_data.append(player["Commendations"])
        fishing_data.append(player["Fishing"])    
        weapons_data.append(player["Weapons"])
        elements_data.append(player["Elements"]) 
        strikes_data.append(player["Strikes"]) 
        dungeons_data.append(player["Dungeons"]) 
        raids_data.append(player["Raids"])
        exotic_data.append(player["Exotics"]) 
        raid_report_data.append(player["RaidReport"])
        
    CommendationDataGenerator.compile_clan(commendation_data)
    FishDataGenerator.compile_clan(fishing_data)
    WeaponDataGenerator.compile_clan(weapons_data)
    ElementalDataGenerator.compile_clan(elements_data)
    StrikeDataGenerator.compile_clan(strikes_data)
    DungeonDataGenerator.compile_clan(dungeons_data)
    RaidDataGenerator.compile_clan(raids_data)
    ExoticDataGenerator.compile_clan(exotic_data)
    RaidCatalyst.compile_clan(raid_report_data)



player_data = process_players()
process_clan(player_data_list=player_data)