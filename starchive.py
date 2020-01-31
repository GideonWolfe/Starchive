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

# Make the output filepath if it doesn't already exist

def handle_path(add_dir):
    os.chdir(conf['defaults']['outputdir'])
    if(Path(add_dir).is_dir() == False and add_dir != "/ADD_PATH"):
        Path(add_dir).mkdir(parents=True, exist_ok=True)

# Executed if user wants to archive a new user
def new_archive():
    print("New archive")
    userUrl = input("Enter the username of the git user you would like to archive starred repositories for.\n")
    gitType = handle_input([0,1], "Will we pull from gitlab[0] or github[1]\n")
    return 1

# Executed when a user wants to update all existing archives
# Note: Made executive decision to add in ability to update certain users later and focus on getting all pulled now...
def existing_archive():
    global conf
    users_dat = conf['users']
    # Change Directories
    os.chdir(conf['defaults']['outputdir'])

    print("Existing User Archives\n\n")
    
    # Add all valid directories names to list, print for visual with associated numerical option for choice
    for key in users_dat:

        path = str(key) + "-" + users_dat[key][0]
        handle_path(path)

    exit()



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
    global conf

    print(text2art("Starchive",font='starwars',chr_ignore=True) + "\n\n\n")

    # Load config file & save config file
    with open("config.yaml", 'r') as stream:
        conf = yaml.safe_load(stream)

    outdir = conf['defaults']['outputdir']

    # Make the output filepath if it doesn't already exist
    handle_path(outdir)

    init_q = "Would you like to: \n\nStart a new archive [0] \nUpdate existing archives? [1]\n"
    # Handle user action choice
    ch = handle_input([0,1], init_q)
    func_switch(ch) 
    
main()
