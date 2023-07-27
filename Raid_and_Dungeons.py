# Connor Downs
# Started: 7-11-2023
# Last Updated: 7-27-2023
# This program requires these programs to operate properly: oneCharOnePage, oneCharTwoPages, allCharsThreePagesONE,
# allCharsThreePagesTWO, allCharsFourPages, allCharsTwoPages, allPlayersR_and_D, Time_Converter

# This program allows a user to investigate a single player's raid or dungeon information. The data can be divided into
# a single character for one player, all characters for a player, and all character data for everyone in Jötunn Gang.
# The first section asks the user who they would want to investigate.
# The second section defines the function values for each player and all of their characters.
# The final section looks at the USER value and determines which function to activate.


from oneCharOnePage import oneCharOnePage
from oneCharTwoPages import oneCharTwoPages
from allCharsThreePagesONE import allCharsThreePagesONE, URLZero, URLOne, URLTwo
from allCharsThreePagesTWO import allCharsThreePagesTWO, URLZeroCTPT, URLOneCTPT, URLTwoCTPT
from allCharsFourPages import allCharsFourPages, URLZero, URLOne, URLTwo, URLThree
from allCharsTwoPages import allCharsTwoPages, URLZero, URLOne
from allPlayersR_and_D import allPlayersR_and_D, URLZero, URLOne, URLTwo, URLThree, URLFour, URLFive, URLSix, \
    URLSeven, URLEight, URLNine, URLTen, URLEleven, URLTwelve, URLThirteen, URLFourteen, URLFifteen, URLSixteen,\
    URLEighteen, URLNineteen, URLTwenty, URLTwenOne, URLTwenTwo, URLTwenThree, URLTwenFour, URLTwenFive

print("Players: Connor, Thomas, Douglas, Hunter, Mark, Jack, Cameron, Kade, All")
print("Player Name: Man in the Moon, The Chrome Leaf, "
      "Piepuns, Lachlan, TheZefraOracle, HeavyChevy, SlayWarsV, Gargoyle Goose, All")
USER = input("Please type a player or player name from the above lists to analyse: ")
print("Titan, Warlock, Hunter, All, Main")
CHAR = input("Please designate which class to analyse: ")
MODE = input("Choose either Raid or Dungeon to analyse: ")

if MODE == "Raid":
    MODE = 4
elif MODE == "Dungeon":
    MODE = 82
else:
    print("Please type an available activity type.")

# Clan ID
groupId = 4268087

def Man_in_the_Moon():
    membershipType = 1
    destinyMembershipId = 4611686018450697084
    if CHAR == "Titan" or CHAR == "Main":
        characterId = 2305843009644414176
        if MODE == 4:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
        elif MODE == 82:
            oneCharTwoPages(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Warlock":
        characterId = 2305843009663894341
        if MODE == 4:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
        elif MODE == 82:
            print("None to report")
    if CHAR == "Hunter":
        characterId = 2305843009703275457
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "All":
        if MODE == 4:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009644414176
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009663894341
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009703275457
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsThreePagesONE(MODE)
        elif MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009644414176
                    URLZeroCTPT(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009644414176
                    URLOneCTPT(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009703275457
                    URLTwoCTPT(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsThreePagesTWO(MODE)

def The_Chrome_Leaf():
    membershipType = 1
    destinyMembershipId = 4611686018444441571
    if CHAR == "Warlock" or CHAR == "Main":
        characterId = 2305843009265786295
        if MODE == 4 or MODE == 82:
            oneCharTwoPages(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Titan":
        characterId = 2305843009283965144
        if MODE == 4 or MODE == 82:
                oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Hunter":
        characterId = 2305843009569534739
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "All":
        if MODE == 4 or MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009644414176
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                    URLThree(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009663894341
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009703275457
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsFourPages(MODE)

def Piepuns():
    membershipType = 1
    destinyMembershipId = 4611686018434621591
    if CHAR == "Hunter" or CHAR == "Main":
        characterId = 2305843010083874501
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Warlock":
        characterId = 2305843009301374530
        if MODE == 4:
            oneCharTwoPages(membershipType, destinyMembershipId, characterId, MODE)
        elif MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Titan":
        characterId = 2305843009293915719
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "All":
        if MODE == 4:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843010083874501
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009301374530
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                    URLThree(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009293915719
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsFourPages(MODE)
        elif MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843010083874501
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009301374530
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009293915719
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsThreePagesONE(MODE)

def TheZefraOracle():
    membershipType = 1
    destinyMembershipId = 4611686018432221111
    if CHAR == "Titan" or CHAR == "Main":
        characterId = 2305843009668854600
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Hunter":
        characterId = 2305843009348154555
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Warlock":
        characterId = 2305843009802904121
        if MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
        elif MODE == 4:
            print("None to report")
    if CHAR == "All":
        if MODE == 4:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009668854600
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009348154555
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009802904121
                char += 1
            allCharsTwoPages(MODE)
        if MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009668854600
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009348154555
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009802904121
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsThreePagesONE(MODE)
def HeavyChevy():
    membershipType = 2
    destinyMembershipId = 4611686018469231992
    if CHAR == "Hunter" or CHAR == "Main":
        characterId = 2305843009268771475
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Warlock":
        characterId = 2305843009891864023
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Titan":
        characterId = 2305843009890274343
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "All":
        if MODE == 4 or MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009268771475
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009891864023
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009890274343
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsThreePagesONE(MODE)

def Lachlan():
    membershipType = 3
    destinyMembershipId = 4611686018476416864
    if CHAR == "Hunter" or CHAR == "Main":
        characterId = 2305843009359734078
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Warlock":
        characterId = 2305843009359365362
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Titan":
        characterId = 2305843009756404411
        if MODE == 4 or MODE == 82:
            print("None to report")
    if CHAR == "All":
        if MODE == 4 or MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009359734078
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009359365362
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009756404411
                char += 1
            allCharsTwoPages(MODE)

def SlayWarsV():
    membershipType = 3
    destinyMembershipId = 4611686018501646188
    if CHAR == "Warlock" or CHAR == "Main":
        characterId = 2305843009683284493
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Titan":
        characterId = 2305843009624174508
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Hunter":
        characterId = 2305843009683284492
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "All":
        if MODE == 4 or MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009683284493
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009624174508
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843009683284492
                    URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsThreePagesONE(MODE)

def Gargoyle_Goose():
    membershipType = 1
    destinyMembershipId = 4611686018451886498
    if CHAR == "Warlock" or CHAR == "Main":
        characterId = 2305843009264637524
        if MODE == 4 or MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "Titan":
        characterId = 2305843009264637527
        if MODE == 4:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
        elif MODE == 82:
            print("None to report")
    if CHAR == "Warlock":
        characterId = 2305843010322954573
        if MODE == 4:
            print("None to report")
        elif MODE == 82:
            oneCharOnePage(membershipType, destinyMembershipId, characterId, MODE)
    if CHAR == "All":
        if MODE == 4:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009264637524
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009264637527
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                if char == 2:
                    characterId = 2305843010322954573
                char += 1
            allCharsTwoPages(MODE)
        if MODE == 82:
            char = 0
            while char < 3:
                if char == 0:
                    characterId = 2305843009264637524
                    URLZero(membershipType, destinyMembershipId, characterId, MODE)
                if char == 1:
                    characterId = 2305843009264637527
                if char == 2:
                    characterId = 2305843010322954573
                    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                char += 1
            allCharsTwoPages(MODE)

def ALL():
    if MODE == 4:
        PLAYER = 0
        while PLAYER < 8:
            # Man in the Moon
            while PLAYER == 0:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018450697084
                while char < 3:
                    if char == 0:
                        characterId = 2305843009644414176
                        URLZero(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009663894341
                        URLOne(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009703275457
                        URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # The Chrome Leaf
            while PLAYER == 1:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018444441571
                while char < 3:
                    if char == 0:
                        characterId = 2305843009265786295
                        URLThree(membershipType, destinyMembershipId, characterId, MODE)
                        URLTwenFour(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009283965144
                        URLFour(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009569534739
                        URLFive(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # Piepuns
            while PLAYER == 2:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018434621591
                while char < 3:
                    if char == 0:
                        characterId = 2305843010083874501
                        URLSix(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009301374530
                        URLSeven(membershipType, destinyMembershipId, characterId, MODE)
                        URLTwenFive(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009293915719
                        URLEight(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # TheZefraOracle
            while PLAYER == 3:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018432221111
                while char < 3:
                    if char == 0:
                        characterId = 2305843009668854600
                        URLNine(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009348154555
                        URLTen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009802904121
                    #    URLEleven(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # HeavyChevy
            while PLAYER == 4:
                char = 0
                membershipType = 2
                destinyMembershipId = 4611686018469231992
                while char < 3:
                    if char == 0:
                        characterId = 2305843009268771475
                        URLTwelve(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009891864023
                        URLThirteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009890274343
                        URLFourteen(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # Lachlan
            while PLAYER == 5:
                char = 0
                membershipType = 3
                destinyMembershipId = 4611686018476416864
                while char < 3:
                    if char == 0:
                        characterId = 2305843009359734078
                        URLFifteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009359365362
                        URLSixteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009756404411
                    #    URLSeventeen(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # SlayWarsV
            while PLAYER == 6:
                char = 0
                membershipType = 3
                destinyMembershipId = 4611686018501646188
                while char < 3:
                    if char == 0:
                        characterId = 2305843009683284493
                        URLEighteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009624174508
                        URLNineteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009683284492
                        URLTwenty(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # Gargoyle Goose
            while PLAYER == 7:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018451886498
                while char < 3:
                    if char == 0:
                        characterId = 2305843009264637524
                        URLTwenOne(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009264637527
                        URLTwenTwo(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843010322954573
                    #    URLTwenThree(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            allPlayersR_and_D(MODE)
    if MODE == 82:
        PLAYER = 0
        while PLAYER < 8:
            # Man in the Moon
            while PLAYER == 0:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018450697084
                while char < 3:
                    if char == 0:
                        characterId = 2305843009644414176
                        URLZero(membershipType, destinyMembershipId, characterId, MODE)
                        URLTwenFour(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009663894341
                    #    URLOne(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009703275457
                        URLTwo(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # The Chrome Leaf
            while PLAYER == 1:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018444441571
                while char < 3:
                    if char == 0:
                        characterId = 2305843009265786295
                        URLThree(membershipType, destinyMembershipId, characterId, MODE)
                        URLTwenFive(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009283965144
                        URLFour(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009569534739
                        URLFive(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # Piepuns
            while PLAYER == 2:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018434621591
                while char < 3:
                    if char == 0:
                        characterId = 2305843010083874501
                        URLSix(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009301374530
                        URLSeven(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009293915719
                        URLEight(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # TheZefraOracle
            while PLAYER == 3:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018432221111
                while char < 3:
                    if char == 0:
                        characterId = 2305843009668854600
                        URLNine(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009348154555
                        URLTen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009802904121
                        URLEleven(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # HeavyChevy
            while PLAYER == 4:
                char = 0
                membershipType = 2
                destinyMembershipId = 4611686018469231992
                while char < 3:
                    if char == 0:
                        characterId = 2305843009268771475
                        URLTwelve(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009891864023
                        URLThirteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009890274343
                        URLFourteen(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # Lachlan
            while PLAYER == 5:
                char = 0
                membershipType = 3
                destinyMembershipId = 4611686018476416864
                while char < 3:
                    if char == 0:
                        characterId = 2305843009359734078
                        URLFifteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009359365362
                        URLSixteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009756404411
                    #    URLSeventeen(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # SlayWarsV
            while PLAYER == 6:
                char = 0
                membershipType = 3
                destinyMembershipId = 4611686018501646188
                while char < 3:
                    if char == 0:
                        characterId = 2305843009683284493
                        URLEighteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009624174508
                        URLNineteen(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 2:
                        characterId = 2305843009683284492
                        URLTwenty(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            # Gargoyle Goose
            while PLAYER == 7:
                char = 0
                membershipType = 1
                destinyMembershipId = 4611686018451886498
                while char < 3:
                    if char == 0:
                        characterId = 2305843009264637524
                        URLTwenOne(membershipType, destinyMembershipId, characterId, MODE)
                    if char == 1:
                        characterId = 2305843009264637527
                    #    URLTwenTwo(membershipType, destinyMembershipId, characterId)
                    if char == 2:
                        characterId = 2305843010322954573
                        URLTwenThree(membershipType, destinyMembershipId, characterId, MODE)
                    char += 1
                PLAYER += 1
            allPlayersR_and_D(MODE)


if USER == "Man in the Moon" or USER == "Connor":
    Man_in_the_Moon()
elif USER == "The Chrome Leaf" or USER == "Thomas":
    The_Chrome_Leaf()
elif USER == "Piepuns" or USER == "Douglas":
    Piepuns()
elif USER == "TheZefraOracle" or USER == "Mark":
    TheZefraOracle()
elif USER == "HeavyChevy" or USER == "Jack":
    HeavyChevy()
elif USER == "Lachlan" or USER == "Hunter":
    Lachlan()
elif USER == "SlayWarsV" or USER == "Cameron":
    SlayWarsV()
elif USER == "Gargoyle Goose" or USER == "Kade":
    Gargoyle_Goose()
elif USER == "All":
    ALL()



