#!/usr/bin/env python3
import os
import time
def clear_screen():
 # 'nt' is for Windows, 'posix' is for Mac and Linux
 os.system('cls' if os.name == 'nt' else 'clear')

#basic commands
bump = "You bumped into a wall"
help = 'To walk, type: "Walk (N,E,S,W) or (N,E,S,W), for help type: "Help" or "H", To exit the game type: "Exit", Press [ENTER] to close this message.'

clear_screen()
print("This game is the first one i have ever created, it is an ambitious attempt to show off what i have learned so far. Please, please, please note any critiques or any bugs/issues in the comments.")
print("This game was made by Regnbuebork on PyCharm.")
input("Press [ENTER] to start")
clear_screen()
print("#$######")
print("# #    #")
print("# # ## #")
print("# #  # #")
print("# ## # #")
print("#    #@#")
print("########")
print("@ = Player, # = Wall, $ = Exit")
print("You entered the maze")
input(help)
input("Press [ENTER] to enter the maze")
while True:
 clear_screen()
 print("\\           /")
 print(" \\         /")
 print("  \\       /")
 print("          ")
 print("          ")
 print("          ")
 print("  /       \\ ")
 print(" /         \\ ")
 print("/           \\ ")
 print("You are facing North")
 choice = input("You: ").upper()
 if choice == "HELP":
  input(help)
 if choice == "WALK N" or choice == "N":
  while True:
   clear_screen()
   print("\\            /")
   print(" |          /")
   print(" |_________/")
   print(" |           ")
   print(" |           ")
   print(" |_________  ")
   print(" |         \\ ")
   print(" |          \\ ")
   print("/            \\ ")
   print("You are facing North")
   choice = input("You: ").upper()
   if choice == "HELP":
    input(help)
   if choice == "WALK N" or choice == "N":
    while True:
     clear_screen()
     print("_            /")
     print(" |\\         /")
     print(" | \\       /")
     print(" |           ")
     print(" |           ")
     print(" |            ")
     print(" | /       \\ ")
     print("_|/         \\ ")
     print("             \\ ")
     print("You are facing West")
     choice = input("You: ").upper()
     if choice == "HELP":
      input(help)
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
       print("\\            /")
       print(" |          /")
       print(" |_________/")
       print(" |           ")
       print(" |           ")
       print(" |_________  ")
       print(" |         \\ ")
       print(" |          \\ ")
       print("/            \\ ")
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
         print("              /")
         print("_            /")
         print(" |__________/")
         print(" |           ")
         print(" |           ")
         print(" |            ")
         print(" |__________ ")
         print("_|          \\")
         print("             \\")
         print("You are facing South")
         choice = input("You: ").upper()
         if choice == "HELP":
          print(
           help)
         if choice == "WALK N" or choice == "N":
          print("You bumped into a wall!")
          continue
         if choice == "WALK S" or choice == "S":
          while True:
           clear_screen()
           print("            /")
           print(" |\\        /")
           print(" | \\      /")
           print(" |        ")
           print(" |        ")
           print(" |        ")
           print(" | /      \\ ")
           print(" |/        \\ ")
           print("            \\ ")
           print("You are facing East")
           choice = input("You: ").upper()
           if choice == "HELP":
            input(help)
           if choice == "WALK N" or choice == "N":
            choice == ""
            break
           if choice == "WALK E" or choice == "E":
            while True:
             clear_screen()
             print("\\            _ ")
             print(" \\__________|")
             print("            |")
             print("            |")
             print("            |")
             print("            |")
             print("  __________|")
             print(" /          |_")
             print("/            ")
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
               print("\\            _ ")
               print(" \\__________|")
               print("            |")
               print("            |")
               print("            |")
               print("            |")
               print("  __________|")
               print(" /          |_")
               print("/            ")
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
                 print("\\            _ ")
                 print(" \\          |")
                 print("  \\         |")
                 print("            |")
                 print("            |")
                 print("            |")
                 print("  /         |")
                 print(" /          \\")
                 print("/            \\_")
                 print("You are facing West")
                 choice = input("You: ").upper()
                 if choice == "HELP":
                  print(help)
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
                   print("\\           /")
                   print(" \\         /")
                   print("  \\       /")
                   print("          ")
                   print("          ")
                   print("          ")
                   print("  /       \\ ")
                   print(" /         \\ ")
                   print("/           \\ ")
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
                     print("\\           /")
                     print(" \\         /")
                     print("  \\       /")
                     print("          ")
                     print("          ")
                     print("          ")
                     print("  /       \\ ")
                     print(" /         \\ ")
                     print("/           \\ ")
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
                       print("\\            / ")
                       print(" \\__________|")
                       print("            |")
                       print("            |")
                       print("            |")
                       print("            |")
                       print("  __________|")
                       print(" /          | ")
                       print("/            \\")
                       print("you are facing West")
                       choice = input("You: ").upper()
                       if choice == "HELP":
                        input(help)
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
                         print("\\            _ ")
                         print(" \\         /|")
                         print("  \\       / |")
                         print("            |")
                         print("            |")
                         print("            |")
                         print("  /       \\ |")
                         print(" /         \\|_ ")
                         print("/            ")
                         print("You are facing North")
                         choice = input("You: ").upper()
                         if choice == "HELP":
                          print(
                           help)
                         if choice == "WALK N" or choice == "N":
                          while True:
                           clear_screen()
                           print("\\           /")
                           print(" \\         /")
                           print("  \\       /")
                           print("          ")
                           print("          ")
                           print("          ")
                           print("  /       \\ ")
                           print(" /         \\ ")
                           print("/           \\ ")
                           print("You are facing North")
                           choice = input("You: ").upper()
                           if choice == "HELP":
                            print(
                             help)
                           if choice == "WALK N" or choice == "N":
                            while True:
                             clear_screen()
                             print("\\   [EXIT]  /")
                             print(" \\ ________/ ")
                             print("  |        |  ")
                             print("  |  ####  |  ")
                             print("  |  EXIT  |  ")
                             print("  |  @==@  |  ")
                             print("  |__####__|  ")
                             print(" /          \\  ")
                             print("/            \\")
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
                             if choice == "EXIT":
                              while True:
                               answer = input("Are you sure you want to exit the game? (Y/N)").upper()
                               if answer == "N" or answer == "NO":
                                break
                               if answer == "Y" or answer == "YES":
                                print("You chickened out. BKAW!")
                                exit()
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
                           if choice == "EXIT":
                            while True:
                             answer = input("Are you sure you want to exit the game? (Y/N)").upper()
                             if answer == "N" or answer == "NO":
                              break
                             if answer == "Y" or answer == "YES":
                              print("You chickened out. BKAW!")
                              exit()
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
                         if choice == "EXIT":
                          while True:
                           answer = input("Are you sure you want to exit the game? (Y/N)").upper()
                           if answer == "N" or answer == "NO":
                            break
                           if answer == "Y" or answer == "YES":
                            print("You chickened out. BKAW!")
                            exit()
                           if choice == "":
                            continue
                           else:
                            continue
                         else:
                          print("Command not found")
                          choice == ""
                        continue
                       if choice == "EXIT":
                        while True:
                         answer = input("Are you sure you want to exit the game? (Y/N)").upper()
                         if answer == "N" or answer == "NO":
                          break
                         if answer == "Y" or answer == "YES":
                          print("You chickened out. BKAW!")
                          exit()
                         if choice == "":
                          continue
                         else:
                          continue
                       else:
                        print("Command not found")
                        choice == ""
                   else:
                    print("Command not found")
                 if choice == "EXIT":
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
               if choice == "WALK W" or choice == "W":
                choice = ""
                break
               if choice == "EXIT":
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
             if choice == "WALK S" or choice == "S":
              print(bump)
              time.sleep(0.5)
              continue
             if choice == "WALK W" or choice == "W":
              choice = ""
              break
             if choice == "EXIT":
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
           if choice == "WALK S" or choice == "S":
            print(bump)
            time.sleep(0.5)
            continue
           if choice == "WALK W" or choice == "W":
            print(bump)
            time.sleep(0.5)
            continue
           if choice == "EXIT":
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
         if choice == "WALK W" or choice == "W":
          print(bump)
          time.sleep(0.5)
          continue
         if choice == "EXIT":
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
       if choice == "EXIT":
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
     if choice == "EXIT":
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
   if choice == "EXIT":
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
 if choice == "EXIT":
  while True:
   choice = input("Are you sure you want to exit the game? (Y/N)").upper()
   if choice == "N" or choice == "NO":
    break
   if choice == "Y" or choice == "YES":
    print("You chickened out. BKAW!")
    exit()
   else:
    continue
   if choice == "":
    continue
 else:
  print("Command not found")
  continue