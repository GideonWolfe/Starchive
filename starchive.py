import re
import yaml
import os
import io
from pathlib import Path
from github import Github
from art import text2art

'''
Version 0.1
See README.md for usage instructions

Started this repo 60% because of the usefulness and 40% because of the name.
'''

conf = {}

# Makes sure the user chose a valid action 
def handle_input(valid_arr, qstn):
    inp = -9669230

    while(inp not in valid_arr):
        if(inp != -9669230):
            print("Wrong input...\n")

        inp = input(qstn)
        chk = re.findall("[0-1000]", inp)

        if(chk):
            inp = int(inp)
    
    return inp

# Loads config file
def load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# Executed if user wants to archive a new user
def new_archive():
    print("New archive")
    userUrl = input("Enter the username of the git user you would like to archive starred repositories for.\n")
    gitType = handle_input([0,1], "Will we pull from gitlab[0] or github[1]\n")
    return 1

# Executed when a user wants to update existing archives
def existing_archive():
    dNum = 0
    allDir = []
    x = os.listdir("REPO_LIST/")

    print("Existing Archives\n\n")
    
    # Add all valid directories names to list, print for visual with associated numerical option for choice
    for testDir in x:
        if os.path.isdir(testDir):
            print("[" + x + "]" + " Username: " + testDir)
            allDir.append(testDir)
            dNum += dNum
    

    # Get input for which directories to update
    dirUpdate = input()

    return 1

# Maps users choice to the correct function
def func_switch(arg):
    switch = {
        0: new_archive,
        1: existing_archive,
    }
    ch_func = switch.get(arg, lambda: "Invalid Option")
    print (ch_func())
    return 1
    
def main():
    # Show Program Title
    print(text2art("Starchive",font='starwars',chr_ignore=True) + "\n\n\n")

    # Load config file

    with open("config.yaml", 'r') as stream:
        conf = yaml.safe_load(stream)
        #print(conf['defaults']['outputdir'])

    '''
    # Make the output filepath if it doesn't already exist
    if(Path(outputdir).is_dir() == False):
        Path(outputdir).mkdir(parents=True, exist_ok=True)
    '''
    init_q = "Would you like to: \n\nStart a new archive [0] \nUpdate an existing archive? [1]\n"

    # Handle user action choice
    ch = handle_input([0,1], init_q)
    func_switch(ch) 
    
main()
