#!/usr/bin/env python3

#Starter Commands



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


print("This is a test map used simply to test out stuff.")

#Map
print(Map2)
print("@ = Player, # = Wall, $ = Exit")
input("Press [ENTER] to enter the maze")
clear_screen()
print("You are entering the maze!")
time.sleep(3)
clear_screen()

#This is the code used for every corridor.

#Movement & Commands
while True:
    clear_screen()
    print(Cor16)
    print("You are facing North")
    choice = input("You: ").upper()
    if choice == "HELP":
        print(helpme)
    if choice == "WALK N" or choice == "N":
        print(bump)
        time.sleep(0.5)
    if choice == "WALK E" or choice == "E":
        print(bump)
        time.sleep(0.5)
        continue
    if choice == "WALK S" or choice == "S":
        print(bump)
        time.sleep(0.5)
    if choice == "WALK W" or choice == "W":
        print(bump)
        time.sleep(0.5)
        continue
    if choice == "EXIT" or choice == "QUIT":
        quits()
    if choice == "":
        continue
    else:
        continue