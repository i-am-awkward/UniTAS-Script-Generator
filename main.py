import sys
import os
from pathlib import Path

# Delaring variables
cwd = os.getcwd() # current working directory
scriptDir = "" # directory of script being created
scriptPath = "" # path directly to script file


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

    if yesNo("Are you sure you want to exit? (y/n)") == 1:
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
        os.chdir(cwd)
    except:
        clearTerminal()
        print("Error creating the file. Make sure file name is valid and a file with that name doesn't already exist")
    else:
        scriptPath = os.path.abspath(scriptFile.name)
        clearTerminal()
        break

print(f"Created file {scriptPath}")
print()