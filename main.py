#!/usr/bin/env python3
from Ascii import *
import time
import subprocess
import os
def clear_screen():
    # 'nt' is for Windows, 'posix' is for Mac and Linux
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)

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

#Intro
clear_screen()
print("This game is the first one i have ever created, it is an ambitious attempt to show off what i have learned so far. Please, please, please note any critiques or any bugs/issues in the comments.")
print("This game was made by Regnbuebork on PyCharm.")
input("Press [ENTER] to start")
clear_screen()

#Map
print(Map1)
print("@ = Player, # = Wall, $ = Exit")
input("Press [ENTER] to enter the maze")
clear_screen()
print("You are entering the maze!")
time.sleep(3)
clear_screen()

#Game Start
while True:
 clear_screen()
 print(Cor1)
 print("You are facing North")
 choice = input("You: ").upper()
 if choice == "HELP":
  input(helpme)
 if choice == "WALK N" or choice == "N":
  while True:
   clear_screen()
   print(Cor2)
   print("You are facing North")
   choice = input("You: ").upper()
   if choice == "HELP":
    input(helpme)
   if choice == "WALK N" or choice == "N":
    while True:
     clear_screen()
     print(Cor3)
     print("You are facing West")
     choice = input("You: ").upper()
     if choice == "HELP":
      input(helpme)
     if choice == "WALK N" or choice == "N":
      print(bump)
      time.sleep(0.5)
      continue
     if choice == "WALK E" or choice == "E":
      print(bump)
      time.sleep(0.5)
      continue
     if choice == "WALK S" or choice == "S":
      choice == ""
      break
     if choice == "WALK W" or choice == "W":
      while True:
       clear_screen()
       print(Cor2)
       print("You are facing West")
       choice = input("You: ").upper()
       if choice == "HELP":
        print(
         help)
       if choice == "WALK N" or choice == "N":
        print(bump)
        time.sleep(0.5)
        continue
       if choice == "WALK E" or choice == "E":
        choice == ""
        break
       if choice == "WALK S" or choice == "S":
        print(bump)
        time.sleep(0.5)
        continue
       if choice == "WALK W" or choice == "W":
        while True:
         clear_screen()
         print(Cor4)
         print("You are facing South")
         choice = input("You: ").upper()
         if choice == "HELP":
          input(helpme)
         if choice == "WALK N" or choice == "N":
          print("You bumped into a wall!")
          continue
         if choice == "WALK S" or choice == "S":
          while True:
           clear_screen()
           print(Cor6)
           print("You are facing East")
           choice = input("You: ").upper()
           if choice == "HELP":
            input(helpme)
           if choice == "WALK N" or choice == "N":
            choice == ""
            break
           if choice == "WALK E" or choice == "E":
            while True:
             clear_screen()
             print(Cor1)
             print("You are facing East")
             choice = input("You: ").upper()
             if choice == "HELP":
              print(
               help)
             if choice == "WALK N" or choice == "N":
              print(bump)
              time.sleep(0.5)
              continue
             if choice == "WALK E" or choice == "E":
              while True:
               clear_screen()
               print(Cor8)
               print("You are facing South")
               choice = input("You: ").upper()
               if choice == "HELP":
                print(
                 help)
               if choice == "WALK N" or choice == "N":
                print(bump)
                time.sleep(0.5)
                continue
               if choice == "WALK E" or choice == "E":
                print(bump)
                time.sleep(0.5)
                continue
               if choice == "WALK S" or choice == "S":
                while True:
                 clear_screen()
                 print(Cor9)
                 print("You are facing West")
                 choice = input("You: ").upper()
                 if choice == "HELP":
                  input(helpme)
                 if choice == "WALK N" or choice == "N":
                  choice = ""
                  break
                 if choice == "WALK E" or choice == "E":
                  print(bump)
                  time.sleep(0.5)
                  continue
                 if choice == "WALK S" or choice == "S":
                  print(bump)
                  time.sleep(0.5)
                  continue
                 if choice == "WALK W" or choice == "W":
                  while True:
                   clear_screen()
                   print(Cor1)
                   print("You are facing West")
                   choice = input("You: ").upper()
                   if choice == "HELP":
                    print(
                     help)
                   if choice == "WALK N" or choice == "N":
                    print(bump)
                    time.sleep(0.5)
                    continue
                   if choice == "WALK E" or choice == "E":
                    choice = ""
                    break
                   if choice == "WALK S" or choice == "S":
                    print(bump)
                    time.sleep(0.5)
                    continue
                   if choice == "WALK W" or choice == "W":
                    while True:
                     clear_screen()
                     print(Cor1)
                     print("You are facing West")
                     choice = input("You: ").upper()
                     if choice == "HELP":
                      print(
                       help)
                     if choice == "WALK N" or choice == "N":
                      print(bump)
                      time.sleep(0.5)
                      continue
                     if choice == "WALK E" or choice == "E":
                      choice = ""
                      break
                     if choice == "WALK S" or choice == "S":
                      print(bump)
                      time.sleep(0.5)
                      continue
                     if choice == "WALK W" or choice == "W":
                      while True:
                       clear_screen()
                       print(Cor10)
                       print("you are facing West")
                       choice = input("You: ").upper()
                       if choice == "HELP":
                        input(helpme)
                       if choice == "WALK N" or choice == "N":
                        print(bump)
                        time.sleep(0.5)
                        continue
                       if choice == "WALK E" or choice == "E":
                        choice = ""
                        break
                       if choice == "WALK S" or choice == "S":
                        print(bump)
                        time.sleep(0.5)
                        continue
                       if choice == "WALK W" or choice == "W":
                        while True:
                         clear_screen()
                         print(Cor11)
                         print("You are facing North")
                         choice = input("You: ").upper()
                         if choice == "HELP":
                          print(
                           help)
                         if choice == "WALK N" or choice == "N":
                          while True:
                           clear_screen()
                           print(Cor1)
                           print("You are facing North")
                           choice = input("You: ").upper()
                           if choice == "HELP":
                            print(
                             help)
                           if choice == "WALK N" or choice == "N":
                            while True:
                             clear_screen()
                             print(exit)
                             print("You are facing North")
                             choice = input("You: ").upper()
                             if choice == "HELP":
                              print(
                               help)
                             if choice == "WALK N" or choice == "N":
                              clear_screen()
                              print("You escaped!")
                              time.sleep(3)
                              clear_screen()
                              print("if you enjoyed the game, check out my site! - https://silly-goober.neocities.org")
                              exit()
                             if choice == "WALK E" or choice == "E":
                              print(bump)
                              time.sleep(0.5)
                              continue
                             if choice == "WALK S" or choice == "S":
                              choice = ""
                              break
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
                            else:
                              print("Command not found")
                              choice == ""
                           if choice == "WALK E" or choice == "E":
                            print(bump)
                            time.sleep(0.5)
                            continue
                           if choice == "WALK S" or choice == "S":
                            choice = ""
                            break
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
                          else:
                            print("Command not found")
                            choice == ""
                          continue
                         if choice == "WALK E" or choice == "E":
                          choice = ""
                          break
                         if choice == "WALK S" or choice == "S":
                          print(bump)
                          time.sleep(0.5)
                          continue
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
                        else:
                          print("Command not found")
                          choice == ""
                        continue
                       if choice == "EXIT" or choice == "QUIT":
                        quits()
                       if choice == "":
                          continue
                       else:
                          continue
                      else:
                        print("Command not found")
                        choice == ""
                   else:
                    print("Command not found")
                 if choice == "EXIT" or choice == "QUIT":
                  quits()
                 if choice == "":
                    continue
                 else:
                    continue
                else:
                  print("Command not found")
               if choice == "WALK W" or choice == "W":
                choice = ""
                break
               if choice == "EXIT" or choice == "QUIT":
                quits()
               if choice == "":
                  continue
               else:
                  continue
              else:
                print("Command not found")
             if choice == "WALK S" or choice == "S":
              print(bump)
              time.sleep(0.5)
              continue
             if choice == "WALK W" or choice == "W":
              choice = ""
              break
             if choice == "EXIT" or choice == "QUIT":
              quits()
             if choice == "":
                continue
             else:
                continue
            else:
              print("Command not found")
           if choice == "WALK S" or choice == "S":
            print(bump)
            time.sleep(0.5)
            continue
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
          else:
            print("Command not found")
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
        else:
          print("Command not found")
          continue
       if choice == "EXIT" or choice == "QUIT":
        quits()
       if choice == "":
          continue
       else:
          continue
      else:
        print("Command not found")
      continue
     if choice == "EXIT" or choice == "QUIT":
      while True:
       choice = input("Are you sure you want to exit the game? (Y/N)").upper()
       if choice == "N" or choice == "NO":
        break
       if choice == "Y" or choice == "YES":
        print("You chickened out. BKAW!")
        exit()
       if choice == "":
        continue
       else:
        continue
     else:
      print("Command not found")
    continue
   if choice == "WALK E" or choice == "E":
    print(bump)
    time.sleep(0.5)
    continue
   if choice == "WALK S" or choice == "S":
    choice = ""
    break
    continue
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
  else:
    print("Command not found")
    continue
  continue
 if choice == "WALK E" or choice == "E":
  print(bump)
  time.sleep(0.5)
  continue
 if choice == "WALK S" or choice == "S":
  print(bump)
  time.sleep(0.5)
  continue
 if choice == "WALK W" or choice == "W":
  print(bump)
  time.sleep(0.5)
  continue
 if choice == "EXIT" or choice == "QUIT":
  quits()
 else:
  print("Command not found")
  continue