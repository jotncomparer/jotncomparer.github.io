#Thomas McGinley
#
#This file is used by the developers to update the website

import os
import time

os.system("cd /home/scf/Desktop/jotncomparer.github.io")
os.system("python ElementalDataGenerator.py")
time.sleep(100)
os.system("python ExoticDataGenerator.py")
time.sleep(100)
os.system("python FishDataGenerator.py")
time.sleep(100)
os.system("python DungeonDataGenerator.py")
time.sleep(100)
os.system("python WeaponDataGenerator.py")
os.system("git add data")
os.system('git commit -m "Updated player data"')
os.system("git push")
