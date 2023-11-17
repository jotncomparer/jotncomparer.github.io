# Connor Downs
# Started: 11-17-2023
# Last Updated: 11-17-2023
# Does the same thing as Raid_and_Dungeons.py

# This program allows a user to investigate a single player's raid or dungeon information. The data can be divided into
# a single character for one player, all characters for a player, and all character data for everyone in Jötunn Gang.
# The first section asks the user who they would want to investigate.
# The second section defines the function values for each player and all of their characters.
# The final section looks at the USER value and determines which function to activate.

# def Dungeon():
from DungeonTest import DungeonTest
from random import randrange

print("Players: Connor, Thomas, Douglas, Hunter, Mark, Jack, Cameron, Kade, All")
print("Player Name: Man in the Moon, The Chrome Leaf, "
      "Piepuns, Lachlan, TheZefraOracle, HeavyChevy, SlayWarsV, Gargoyle Goose, All")
USER = input("Please type a player or player name from the above lists to analyse: ")

if USER == "All":
    MODE = input("Choose either Raid or Dungeon to analyse: ")
else:
    print("Titan, Warlock, Hunter, Main, All")
    CHAR = input("Please designate which class to analyse: ")
    MODE = input("Choose either Raid or Dungeon to analyse: ")

if MODE == "Raid":
    MODE = 4
elif MODE == "Dungeon":
    MODE = 82


def Man_in_the_Moon():
    PAGE = 0
    membershipType = 1
    destinyMembershipId = 4611686018450697084
    if CHAR == "Titan" or CHAR == "Main":
        characterId = 2305843009644414176
        if MODE == 82:
            DungeonTest(membershipType, destinyMembershipId, characterId, MODE, PAGE)
    else:
        errorNumb = randrange(1, 5)
        if errorNumb == 1:
            print("She be Rhulking on my Disciple til I Strand.")
        elif errorNumb == 2:
            print("The Wish Wall accepts your wish, O' Gooner Mine.")
        elif errorNumb == 3:
            print("Nice try, Shitass.")
        elif errorNumb == 4:
            print("That Savathussy got me acting lightless.")


if USER == "Man in the Moon" or USER == "Connor":
    Man_in_the_Moon()
else:
    errorNumb = randrange(1, 5)
    if errorNumb == 1:
        print("She be Rhulking on my Disciple til I Strand.")
    elif errorNumb == 2:
        print("The Wish Wall accepts your wish, O' Gooner Mine.")
    elif errorNumb == 3:
        print("Nice try, Shitass.")
    elif errorNumb == 4:
        print("That Savathussy got me acting lightless.")
