#Thomas McGinley
#
#This file is used by the developers to update the website

from os import system

system("cd /home/scf/Desktop/jotncomparer.github.io")
system("git pull")
system("python JOTUNN_CATALYST.py")
system("git add data")
system("git add images")
system('git commit -m "Updated player data"')
system("git push")
