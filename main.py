#!/usr/bin/env python3
#starter imports
from Ascii import *
import time
import subprocess
import os
import shutil

#Import maps
from MAZE1 import *
#from TESTMAP import *


def center_text(s: str, vertically: bool = False) -> str: #Credits to mouad.0 on discord for the script
    """centers given text based on terminal size
    Args:
        s (str): text to center
        vertically (bool, optional): whether to center text vertically, for this to work, the terminal must be empty. Defaults to False.

    Returns:
        str: the centered text
    """
    size = os.get_terminal_size()
    columns, lines = size.columns, size.lines
    clean_lines = []
    for line in s.splitlines():
        if len(line) == 0:
            continue
        clean = ""
        keep_removing = True
        for character in line[::-1]:
            if character == " " and keep_removing:
                continue
            elif character != " ":
                keep_removing = False
            clean += character
        clean = clean[::-1]
        clean_lines.append(clean)
    clean_s = "\n".join(clean_lines)
    highest = 0
    for line in clean_s.splitlines():
        if len(line) == 0:
            continue
        if len(line) > highest:
            highest = len(line)
    text = ""
    if vertically:
        half = (lines / 2) - (len(clean_s.splitlines()) / 2)
        to_sub = 2 if half % 1 == 0.5 else 1
        for _ in range((lines // 2) - (len(clean_s.splitlines()) // 2) - to_sub):
            text += "\n"
    before = ((columns // 2) - (highest // 2))
    for line in s.splitlines():
        text += (" " * before) + line + ("\n" if len(s.splitlines()) > 1 else "")
    return text


def clear_screen(): #Clear the terminal screen from all characters
    # 'nt' is for Windows, 'posix' is for Mac and Linux
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)


#basic commands
def quits():
  while True:
   answer = input(center_text("Are you sure you want to exit the game? (Y/N)").upper())
   if answer == "N" or answer == "NO":
    break
   if answer == "Y" or answer == "YES":
    print(center_text("You chickened out. BKAW!"))
    exit()
bump = "You bumped into a wall"
helpme = 'To walk, type: "WALK (N,E,S,W) or (N,E,S,W), for help type: "HELP" or "H", To exit the game type: "GIVEUP" or "QUIT", Press [ENTER] to close this message.'
#End of Basic Commands


#Intro
clear_screen()
print(center_text("This game is the first one i have ever created, it is an ambitious attempt to show off what i have learned so far. Please, please, please note any critiques or any bugs/issues in the comments."))
print(center_text("This game was made by Regnbuebork on PyCharm."))
input(center_text("Press [ENTER] to start"))
clear_screen()
#End of intro


#Below are the maps that will run. Each map includes their own python file to minimize the python code. Insert ever maze one by one.
maze1()
#testmap() #Just a dumb test map used to test level transition, DO NOT UNCOMMENT, there is NO ESCAPE from this map, you are willingly trapping yourself. FOREVER!!!

#After the final maze
input("You beat the game! Press [ENTER] to exit")
clear_screen()
print(center_text('if you enjoyed the game, check out my site! (https://silly-goober.neocities.org). If you have any feedback, please leave it in the "Feedback" discussion in the game\'s GitHub page (https://github.com/Supervisor360/Maze-Game/discussions/1)'))
print(center_text('With support from Mouad.0 and Sastacet on the Python Discord Server. (if you want to be apart of the supporters, help by giving feedback and ideas)'))
time.sleep(1)
exit()