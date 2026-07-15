Welcome to my UniTAS script generator! This tool is made in python, so just make sure you have it installed

This currently only made for Ultrakill, and it's intended to get rid of copy pasting boilerplate code and brute forcing specific pixels to menu through.
This tool also writes built-in methods for speedrunning tech in the script itself to avoid more boilerplate. Currently the list of tech and usage is as follows:

- Equip weapons // Usage: equipWeapon(weaponKey, variationKey) 
    weaponKey = key that corresponds to the weapon you're equipping
    variationKey = key that corresponds to the variation you're equipping, does nothing if no argument given

- Ssj's // Usage: SSJ(frame)
    frame = the frame ssj you want

I may in the future add more preset tech

Works for 1920x1080

Installation instructions:

Open your terminal and run:
git clone https://github.com/i-am-awkward/UniTAS-Script-Generator.git

Then in the directory it was cloned in, run:
python ScriptGen.py

Usage instructions:
Just run the python file in your terminal and follow the prompts

Made by Awkward
(I did steal some of Darkn's code so credit to him for some of the Lua preset lines in ScriptData.txt)