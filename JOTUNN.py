# Connor Downs
# Started: 8-2-2023
# Last Updated: 8-2-2023
# This program needs Exotics.py, Raid_and_Dungeons.py, and Character_Metrics.py to work properly.

# This program is used to define every player in Jötunn Gang.
# This program asks the user which report type they wish tp make.
# This program specifically looks to the three programs made as of (8/2/2023), exotics, raid and dungeons,
# and all character triumphs and metrics

from Exotics import Exotics
from Raid_and_Dungeons import Raid_and_Dungeons
from Character_Metrics import Character_Metrics


print("Exotic Use Reporter (1), Raid and Dungeon Reporter (2), Player Metric Reporter (3)")
TOOL = input('Please type which tool you wish to use: ')

if TOOL == '1':
    Exotics()
elif TOOL == '2':
    Raid_and_Dungeons()
elif TOOL == '3':
    Character_Metrics()
else:
    print("She be Rhulking on my Disciple til I Strand.")
