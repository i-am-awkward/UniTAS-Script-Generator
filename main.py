import sys
import os
from pathlib import Path
from enum import Enum

# TODO: Find coordinates to other difficulties

# Delaring variables
cwd = os.getcwd() # current working directory
scriptDir = "" # directory of script being created
scriptPath = "" # path directly to script file

class Coordinates(Enum): # Stores coordinates of buttons
    HARMLESS = 560,840
    LENIENT = 222,222
    STANDARD = 333,333
    VIOLENT = 444,444
    BRUTAL = 555,555


# Deletes in-progress script
def deleteScript():
    if scriptPath != "":
        os.remove(scriptPath)

# Clears terminal when called
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Takes the question as an argument, returns 1 if "y", returns 0 if "n", repeats if input isnt either
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

# Terminates the program if "exit" is typed at any point, checks if input is "exit" then terminated based on a y/n. Returns 1 if no
def exitCheck(prompt):
    clearTerminal()
    if prompt.strip().lower() != "exit":    return

    if yesNo("Are you sure you want to exit? Any in-progress script will be deleted. (y/n)") == 1:
        deleteScript()
        print("Terminating program...")
        sys.exit(0)
    print("Not terminating, returning...")
    return 1

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

            try: # Checks if difficulty in in Coordinates Enum
                coords = Coordinates[difficulty.upper()]

            except:
                print(f"{difficulty} not a valid difficulty. Please make sure you entered a valid Ultrakill difficulty")
                continue

            else: # Writes difficulty presets to file
                print(f"Selecting difficulty {difficulty}\n")
                script.write(f'print("Selecting {difficulty} difficulty")\n')
                script.write("movie.frame_advance(30)\n")
                script.write(f"mouse.move{str(coords.value)}\n")
                script.write("movie.frame_advance(30)\n")
                script.write("mouse.left(true)\n")
                script.write("movie.frame_advance(30)\n")
                script.write("mouse.left(false)\n")
                script.write("movie.frame_advance(30)\n")
                break