#Thomas McGinley
#
#This file is used by the developers to update the website

from os import system
from time import sleep

system("cd /home/scf/Desktop/jotncomparer.github.io")
system("git pull")
system("python ElementalDataGenerator.py")
sleep(15)
system("python ExoticDataGenerator.py")
sleep(15)
system("python FishDataGenerator.py")
sleep(15)
system("python DungeonDataGenerator.py")
sleep(15)
system("python WeaponDataGenerator.py")
sleep(15)
system("python StrikeDataGenerator.py")
sleep(15)
system("python RaidDataGenerator.py")
sleep(15)
system("python CommendationDataGenerator.py")
sleep(15)
system("python EmblemGenerator.py")
system("git add data")
system("git add images")
system('git commit -m "Updated player data"')
system("git push")
