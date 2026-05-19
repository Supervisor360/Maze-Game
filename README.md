# Maze-Game
<pre>
                           ==============================================================================
                             ▗▄▖  ▗▄▄▖▗▖ ▗▖ ▗▄▄▖ ▗▄▄▖    ▗▖  ▗▖ ▗▄▖ ▗▄▄▄▄▖▗▄▄▄▖     ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖
                            ▐▌ ▐▌▐▌   ▐▌ ▐▌▐▌   ▐▌       ▐▛▚▞▜▌▐▌ ▐▌   ▗▞▘▐▌       ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌   
                            ▐▌ ▐▌▐▌   ▐▌ ▐▌ ▝▀▚▖ ▝▀▚▖    ▐▌  ▐▌▐▛▀▜▌ ▗▞▘  ▐▛▀▀▘    ▐▌▝▜▌▐▛▀▜▌▐▌  ▐▌▐▛▀▀▘
                            ▝▚▄▞▘▝▚▄▄▖▝▚▄▞▘▗▄▄▞▘▗▄▄▞▘    ▐▌  ▐▌▐▌ ▐▌▐▙▄▄▄▖▐▙▄▄▖    ▝▚▄▞▘▐▌ ▐▌▐▌  ▐▌▐▙▄▄▖
                           ==============================================================================
                                                A TERRIBLE CLI maze game by Regnbuebörk
        
                                   
Ascii 3D Labyrinth Game example made in Python. Made to test my abilities in Python.

This is one of my first games made in Python, as well as the most ambitious one I have created. It is a simple maze game with 3D Ascii graphics, made to show what I have learned and to expand on my current abilities.

This was released as is in order to get ideas and constructive critique from codereviewers on how to Improve, Clean, and Repair my code, as well as what I could do, add, and how to add such features.

The actual executables are as of currently available as a Unix Executable File with a Windows port being released once I either setup a virtual machine or get home on my Windows PC.

The game is fully Open Source and I insist that you modify the code to your heartscontent to help give me a visual example to work and learn off of. It will highly benefit me to be able to see what I can do to improve the code.

Other than that, enjoy the game! More documentation and manual is available below.

       
============================================================================================================================================


  
                                                    --=={    CONTROLS    }==--

  
#NOTE: Commands are not case sensitive, however they must be written correctly.

Movement: Type "Walk (N, E, S, W)" or just "(N, E, S, W)." (N, E, S, W refer to North, East, South, and West respectedly.)

Help: Type "Help" for a list of available commands and their arguments.

Exit: Type "Exit" or "QUIT" to leave the game. You will be prompted whether or not youwant to leave. (Y = Leave, N = Stay.)

More commands are planned to be implemented soon.

       
============================================================================================================================================


  
                                                    --=={    Maze Map    }==--
   

The map is currently very small with plans to implement (a possibly terrible)automatically generated map in the future. Right now the map is just a simple dungeon of around 16 total available steps to victory. Below is an ASCII representation of the Maze as shown overhead. This map is also shown at the start of the game.

                                                        #$###### | # = Wall
                                                        # #    # | $ = Exit
                                                        # # ## # | @ = Player
                                                        # #  # # | 
                                                        # ## # # | 
                                                        #    #@# | 
                                                        ######## | 

       
============================================================================================================================================


  
                                                    --=={     VIEW     }==--
  

The dungeon is shown in ASCII characters with the view direction shown just below the view window.
        

                                                         \            /
                                                          \          /
                                                           \        /

                                                                       <-- 3D View Window of the Dungeon

                                                           /        \
                                                          /          \
                                                         /            \  
                                                      You are facing North <-- View Direction
                                                              You: <-- Your input (See "Controls" for commands)

                                              
============================================================================================================================================



                                              
                                                    --=={    Map Creation    }==--


Each map is created with a set of if and else statements confined within a while True. No map is randomly generated as i do not know how to implement that myself. In order to create a map you need to understand how the commands will work.

                                              
                                                    [Imports and Starter Commands]   

The code relies on several imported features including time, subprocess, os, as well as the several maps. in order to test your map. You need to 
                                              
                                                          [Before Maze Entry]


Now before the player enters the maze, we MAY want to add a overhead view and show the player how the map looks. This is a totally optional step, leaving the player in the dark may make the maze even more fun! However, sometimes we may want to note stuff still before the player enters the maze. that is why this is here.


</pre>
```python 
print(center_text('''
# ######
# #    #
# # ## #
# #  # #
# ## # #
#    #@#
########
'''))
print(center_text("@ = Player, # = Wall, $ = Exit"))
input("Press [ENTER] to enter the maze")
clear_screen()
print(center_text("You are entering the maze!"))
time.sleep(3)
clear_screen()
```

<pre>
                                                                      
                                              
                                                          [Movement & Commands]

                                              
The script below allows the player to not only move but also use commands such as Exit and Help.
                                                             
</pre>
```python                                              
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
```

<pre>
                                                                      
Now currently, every direction is blocked. However if you wanted to allow the player to move EAST, you would simply take the if choice == "WALK E" commands and replace what is contained within said if statement and replace it with the code above to add a new room. It is also recommended that the opposite area has a "break" statement to go back to the previous room.


</pre>
```python
    if choice == "WALK E" or choice == "E":
        (SCRIPT ABOVE)
        if choice == "WALK W" or choice == "W":
        choice == "" 
        break
        continue
```                                                  
<pre>

                                                          [Exit]


Now what is a maze game without an exit? Incorporating an exit is easy! first we will  set the "Corridor" as exit, and set the direction where the exit is located (In this we will use "North" as an example. Below is an example of a valid exit.


</pre>
```python
while True:
    clear_screen()
    print(center_text(exit))
    print(center_text("You are facing North"))
    choice = input("You: ").upper()
    if choice == "HELP":
        print(center_text(helpme))
    if choice == "WALK N" or choice == "N":
        input(center_text("You Escaped!))
        exit()
    if choice == "WALK E" or choice == "E":
        print(center_text(bump))
        time.sleep(0.5)
        continue
    if choice == "WALK S" or choice == "S":
        choice = ""
        break
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
```
<pre>


While map creation can be tough as there isnt much of a visual way of doing it unless developed later, these steps can help simplify the instructions. Any custom map made will be added to the game with credits of each map maker included in the credits!

                                              
============================================================================================================================================

                                              
This game was created by Luis Cruz or as I like to go online by, Regnbuebörk. This software was released to the public on May 13, 2026.
  
                                You can check out my site at https://silly-goober.neocities.org

                                                         Enjoy!
</pre>
