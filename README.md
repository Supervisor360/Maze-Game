# Maze-Game

<pre>
Ascii 3D Labyrinth Game example made in Python. Made to test my abilities in Python.

This is one of my first games made in Python, as well as the most ambitious one I have created. It is a simple maze game with 3D Ascii graphics, made to show what I have learned and to expand on my current abilities.

This was released as is in order to get ideas and constructive critique from code reviewers on how to Improve, Clean, and Repair my code, as well as what I could do, add, and how to add such features.

The Source Code is literally in a single file called "source.py". The actual executables are as of currently available as a Unix Executable File with a Windows port being released once I either setup a virtual machine or get home on my Windows PC.

The game is fully Open Source and I insist that you modify the code to your hearts content to help give me a visual example to work and learn off of. It will highly benefit me to be able to see what I can do to improve the code.

Other than that, enjoy the game! More documentation and manual is available below.

========================================================================================

  
                            --=={    CONTROLS    }==--

  
#NOTE: Commands are not case sensitive, however they must be written correctly.

Movement: Type "Walk (N, E, S, W)" or just "(N, E, S, W)." (N, E, S, W refer to North, East, South, and West respectedly.)

Help: Type "Help" for a list of available commands and their arguments.

Exit: Type "Exit" to leave the game. You will be prompted whether or not you want to leave. Y = Leave, N = Stay.

More commands are planned to be implemented soon.

========================================================================================

  
                            --=={    Maze Map    }==--
   

The map is currently very small with plans to implement (a possibly terrible) automatically generated map in the future. Right now the map is just a simple dungeon of around 16 total available steps to victory. Below is an ASCII representation of the Maze as shown overhead. This map is also shown at the start of the game.

#$###### | # = Wall
# #    # | $ = Exit
# # ## # | @ = Player
# #  # # | 
# ## # # | 
#    #@# | 
######## | 

========================================================================================

  
                            --=={     VIEW     }==--
  

The dungeon is shown in ASCII characters with the view direction shown just below the view window.

\\           /
 \\         /
  \\       /

               <-- 3D View Window of the Dungeon

  /       \\ 
 /         \\ 
/           \\ 
You are facing North <-- View Direction

========================================================================================

This game was created by Luis Cruz or as I like to go online by, Regnbuebörk. This software was released to the public on May 13, 2026.
  
You can check out my site at https://silly-goober.neocities.org

Enjoy!
</pre>
