#These are all the commands that were used to build this game. This includes a basic test map

#!/usr/bin/env python3
from Ascii import *
from MAZE1 import *
import time
import subprocess
import os
import shutil


def clear_screen(): #Clear the terminal screen from all characters
    # 'nt' is for Windows, 'posix' is for Mac and Linux
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)


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


#basic commands
def quits():
  while True:
   answer = input("Are you sure you want to exit the game? (Y/N)").upper()
   if answer == "N" or answer == "NO":
    break
   if answer == "Y" or answer == "YES":
    print("You chickened out. BKAW!")
    exit()
bump = "You bumped into a wall"
helpme = 'To walk, type: "WALK (N,E,S,W) or (N,E,S,W), for help type: "HELP" or "H", To exit the game type: "GIVEUP" or "QUIT", Press [ENTER] to close this message.'
#End of Basic Commands

#basic commands
def quits():
  while True:
   answer = input("Are you sure you want to exit the game? (Y/N)").upper()
   if answer == "N" or answer == "NO":
    break
   if answer == "Y" or answer == "YES":
    print("You chickened out. BKAW!")
    exit()
bump = "You bumped into a wall"
helpme = 'To walk, type: "Walk (N,E,S,W) or (N,E,S,W), for help type: "Help" or "H", To exit the game type: "Exit" or "Quit", Press [ENTER] to close this message.'



#==============================================[MAP STRUCTURE CODE]==================================================================================================================



#Map
print(center_text("MAP PREVIEW"))
print(center_text("@ = Player, # = Wall, $ = Exit"))
input("Press [ENTER] to enter the maze")
clear_screen()
print(center_text("You are entering the maze!"))
time.sleep(3)
clear_screen()

#This is the code used for every corridor.

#Movement & Commands
while True:
    clear_screen()
    print(center_text(Cor16))
    print(center_text("You are facing North"))
    choice = input("You: ").upper()
    if choice == "HELP":
        print(center_text(helpme))
    if choice == "WALK N" or choice == "N":
        print(center_text(bump))
        time.sleep(0.5)
    if choice == "WALK E" or choice == "E":
        print(center_text(bump))
        time.sleep(0.5)
        continue
    if choice == "WALK S" or choice == "S":
        print(center_text(bump))
        time.sleep(0.5)
    if choice == "WALK W" or choice == "W":
        print(center_text(bump))
        time.sleep(0.5)
        continue
    if choice == "EXIT" or choice == "QUIT":
        quits()
    if choice == "":
        continue
    else:
        continue