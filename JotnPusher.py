#Thomas McGinley
#
#This file is used by the developers to update the website

import os

os.system("cd /home/scf/Desktop/jotncomparer.github.io")
os.system("python ExoticDataGenerator.py")
os.system("git add data")
os.system('git commit -m "Updated player data"')
os.system("git push")
