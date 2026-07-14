import sys
import os
from pathlib import Path
from enum import Enum

# * Delaring variables/functions
cwd = os.getcwd() # current working directory
scriptDir = "" # directory of script being created
scriptPath = "" # path directly to script file

# Awkward note: Getting all these coordinates took way too long T-T
class DifCoordinates(Enum): # Stores coordinates of difficulty buttons
    HARMLESS = 560, 850
    LENIENT = 560, 750
    STANDARD = 560, 550
    VIOLENT = 560, 450
    BRUTAL = 560, 250

class LevCoordinates(Enum): # Stores coordinates of level buttons
    LEVEL_0_s = 1650, 900
    LEVEL_0_1 = 230, 625
    LEVEL_0_2 = 600, 625
    LEVEL_0_3 = 950, 625
    LEVEL_0_4 = 1325, 625
    LEVEL_0_5 = 1700, 625
    LEVEL_1_s = 1600, 940
    LEVEL_1_1 = 270, 675
    LEVEL_1_2 = 715, 675
    LEVEL_1_3 = 1150, 675
    LEVEL_1_4 = 1600, 675
    LEVEL_2_s = 1600, 900 # Relative to scroll 1
    LEVEL_2_1 = 270, 625 # Relative to scroll 1
    LEVEL_2_2 = 725, 625 # Relative to scroll 1
    LEVEL_2_3 = 1150, 625 # Relative to scroll 1
    LEVEL_2_4 = 1600, 625 # Relative to scroll 1
    LEVEL_3_1 = 500, 500 # Relative to scroll 2
    LEVEL_3_2 = 1380, 500 # Relative to scroll 2
    LEVEL_4_s = 1600, 940
    LEVEL_4_1 = 270, 675
    LEVEL_4_2 = 715, 675
    LEVEL_4_3 = 1150, 675
    LEVEL_4_4 = 1600, 675
    LEVEL_5_s = 1600, 900 # Relative to scroll 1
    LEVEL_5_1 = 270, 625 # Relative to scroll 1
    LEVEL_5_2 = 725, 625 # Relative to scroll 1
    LEVEL_5_3 = 1150, 625 # Relative to scroll 1
    LEVEL_5_4 = 1600, 625 # Relative to scroll 1
    LEVEL_6_1 = 500, 500 # Relative to scroll 2
    LEVEL_6_2 = 1380, 500 # Relative to scroll 2
    LEVEL_7_s = 1600, 940
    LEVEL_7_1 = 270, 675
    LEVEL_7_2 = 715, 675
    LEVEL_7_3 = 1150, 675
    LEVEL_7_4 = 1600, 675
    LEVEL_8_1 = 270, 625 # Relative to scroll 1
    LEVEL_8_2 = 725, 625 # Relative to scroll 1
    LEVEL_8_3 = 1150, 625 # Relative to scroll 1
    LEVEL_8_4 = 1600, 625 # Relative to scroll 1
    LEVEL_0_e = 220, 650
    LEVEL_1_e = 580, 650
    LEVEL_p_1 = 415, 600
    LEVEL_p_2 = 950, 600
    
class LayCoordinates(Enum): # Store coordinates of layer buttons
    PRELUDE = 1200, 750
    ACT_1 = 1200, 670
    ACT_2 = 1200, 600
    ACT_3 = 1200, 520
    ENCORES = 1200, 360
    PRIME_SANCTUMS = 1200, 280

# Deletes in-progress script
def deleteScript():
    if scriptPath != "":
        os.remove(scriptPath)

# Clears terminal when called
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Takes the question as an argument, returns 1 if "y", returns 0 if "n", repeats if input isnt either. Takes user input as argument
def yesNo(prompt):
    while True:
        print(prompt)
        answer = input().strip().lower()

        if exitCheck(answer) == 1: continue       

        if answer == "y":
            return 1

        elif answer == "n":
            return 0

        clearTerminal()
        print('Not a valid input, please only type a "y" or an "n"')

# Terminates the program if "exit" is typed at any point, checks if input is "exit" then terminated based on a y/n. Returns 1 if no. Takes user input as argument
def exitCheck(prompt):
    clearTerminal()
    if prompt.strip().lower() != "exit":    return

    if yesNo("Are you sure you want to exit? Any in-progress script will be deleted. (y/n)") == 1:
        deleteScript()
        print("Terminating program...")
        sys.exit(0)
    print("Not terminating, returning...")
    return 1

# Checks what layer a level belongs to, if you need to scroll and if so how much, Takes validated user inputted level as argument
# Returns: Corresponding layer enum, if you need to scroll in level select (0 = no scrolling, 1 = middle scroll, 2 = full scroll)
def LevelMenuCheck(level):
    if level[2] == 'e':
        return LayCoordinates["ENCORES"], 0
    if level[0] == 'p':
        return LayCoordinates["PRIME_SANCTUMS"], 0
    if level[0] == '0':
        return LayCoordinates["PRELUDE"], 0
    if level[0] == '1' or level[0] == '2' or level[0] == '3':
        needsToScroll = int(level[0]) - 1 # Subtracts 1 from layer number to get correct amount to scroll
        return LayCoordinates["ACT_1"], needsToScroll
    if level[0] == '4' or level[0] == '5' or level[0] == '6':
        needsToScroll = int(level[0]) - 4 # Subtracts 4 from layer number to get correct amount to scroll
        return LayCoordinates["ACT_2"], needsToScroll
    if level[0] == '7' or level[0] == '8':
        needsToScroll = int(level[0]) - 7 # Subtracts 7 from layer number to get correct amount to scroll
        return LayCoordinates["ACT_3"], needsToScroll
    
# * MAIN CODE START
# * MAIN CODE START
# * MAIN CODE START

# intro message / greeting
print("Welcome to the Ultrakill Tas Script Generator!")
print("This tool was made to get rid of the time spent on creating boilerplate code")
print("like selecting the level, difficulty, alignment, etc.")
print("Just follow the prompts and the script will be created automatically!")
print('Type "exit" at any time to terminate the program and delete any data created in the session')
print("Created by Awkward :)")
print()

# Asks if they want to create script, breaks if "y", terminates if "n", repeats if neither
if yesNo("Ready to create a script? (y/n)") == 0:
    print("Terminating program...")
    sys.exit(0)

# Checks if filePath given is a valid path, or defaults to CreatedScripts
while True:
    print("Where would you like the file to be created?")
    print("Please type as a filepath")
    print(f'Default is "{cwd}/CreatedScripts", enter nothing to use this default')

    filePath = input()
    if exitCheck(filePath) == 1: continue

    if filePath == "":
        scriptDir = f"{cwd}/CreatedScripts"
        if not os.path.exists(scriptDir): os.mkdir(scriptDir)
        print(f"Using default filepath {scriptDir}")
        break

    elif Path(filePath).exists():
        scriptDir = filePath
        print(f"Using filepath {scriptDir}")
        break

    clearTerminal()
    print("Invalid path given, make sure the folder is already created. Please try again.")

# Naming the file, checks for invalid file names
while True:
    print("What would you like to name the script?")

    name = input()
    if exitCheck(name) == 1: continue

    try:
        os.chdir(scriptDir)
        scriptFile = open(f"{name}.lua", "x")
        scriptPath = os.path.abspath(scriptFile.name)
        os.chdir(cwd)
    except:
        clearTerminal()
        print("Error creating the file. Make sure file name is valid and a file with that name doesn't already exist")
    else:
        scriptFile.close()
        clearTerminal()
        break

print(f"Created file {scriptPath}")

# * BEGINS WRITING TO SCRIPT FILE
with open(f"{scriptPath}", "a") as script, open ("ScriptData.txt", "r") as data:
        lines = data.readlines()

        print("Writing default parameters and setup to file...")

        # Write lines 1-58 in ScriptData file, default parameters
        for line in lines[:58]:
            script.write(line)

        # * DIFFICULTY PROMPTS
        while True:
            print("Which difficulty will you be playing on?")
            difficulty = input().strip()
            
            if exitCheck(difficulty) == 1: continue
            clearTerminal()

            try: # Checks if difficulty in in DifCoordinates Enum
                coords = DifCoordinates[difficulty.upper()]

            except:
                print(f"{difficulty} not a valid difficulty. Please make sure you entered a valid Ultrakill difficulty")
                continue

            else: # Writes difficulty presets to file
                print(f"Selecting difficulty {difficulty}\n")

                script.write(f'print("Selecting {difficulty} difficulty")\n')
                script.write("movie.frame_advance(30)\n")
                script.write(f"mouse.move({str(coords.value)})\n")
                script.write("movie.frame_advance(30)\n")
                script.write("mouse.left(true)\n")
                script.write("movie.frame_advance(30)\n")
                script.write("mouse.left(false)\n")
                script.write("movie.frame_advance(30)\n\n")

                break

        # * LAYER/LEVEL PROMPTS
        while True:
            print("Which level are you playing on?")
            print("Main levels, secret levels, encores, prime sanctums work")
            print("Please use the level abbreviation (0-1, p-2, 4-s, 1-e, etc)")

            level = input().strip().lower()
            if exitCheck(level) == 1: continue
            clearTerminal()

            try: # Checks if level in LevCoordinates Enum
                coords = LevCoordinates[f"LEVEL_{level[0]}_{level[2]}"] # Turns level input into LevCoordinates format (1-2 -> LEVEL_1_2)
                    
            except:
                print(f"LEVEL_{level[0]}_{level[2]}")
                print(f"{level} not a valid level. Please make sure you entered a valid Ultrakill level with correct formatting")
                continue
            else:
                levelData = LevelMenuCheck(level) # Returns a tuple of Corresponding layer enum, if you need to scroll in level select (0 = no scrolling, 1 = middle scroll, 2 = full scroll)
                print(f"Selecting level {level} in {levelData[0].name}")
                
                # Writes layer select to script
                script.write(f'print("Selecting {levelData[0].name}")\n')
                script.write(f"mouse.move({str(coords.value)})\n")
                script.write("movie.frame_advance(30)\n")
                script.write("mouse.left(true)\n")
                script.write("movie.frame_advance(30)\n")
                script.write("mouse.left(false)\n")
                script.write("movie.frame_advance(30)\n\n")

                script.write(f'print("Selecting {level}")\n')
                # Writes scroll 1 to script if applicable
                if levelData[1] == 1:
                    script.write("mouse.move(1890,800)\n")
                    script.write("movie.frame_advance(30)\n")
                    script.write("mouse.left(true)\n")
                    script.write("movie.frame_advance(30)\n")
                    script.write("mouse.move(1890,500)\n")
                    script.write("movie.frame_advance(30)\n")
                    script.write("mouse.left(false)\n")
                    script.write("movie.frame_advance(30)\n")
                
                # Writes scroll 2 to script if applicable
                if levelData[1] == 2:
                    script.write("mouse.move(1890,800)\n")
                    script.write("movie.frame_advance(30)\n")
                    script.write("mouse.left(true)\n")
                    script.write("movie.frame_advance(30)\n")
                    script.write("mouse.move(1890,225)\n")
                    script.write("movie.frame_advance(30)\n")
                    script.write("mouse.left(false)\n")
                    script.write("movie.frame_advance(30)\n")

                

                break
