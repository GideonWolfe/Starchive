import re
from art import text2art
import yaml
from pathlib import Path
from github import Github

'''
Version 0.1
See README.md for usage instructions

Started this repo 60% because of the usefulness and 40% because of the name.
'''

# Globals

# Loads config file
def load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

# Authenticates and loads github profile for API access
def load_github(ghuser, ghpass, ghtoken):
    g = Github(ghuser, ghpass, ghtoken)

    for repo in g.get_user().get_repos():
        print(repo.name)


# Function to be executed if user wants to archive a new user
def new_archive():
    print("New archive")
    userUrl = input("Enter the URL of the git user you wish to Starchive")
    return 1

# Function to be executed when a user wants to update existing archives
def existing_archive():
    print("Existing Archive")
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

def main():
    # Show Program Title
    print(text2art("Starchive",font='starwars',chr_ignore=True) + "\n\n\n")

    # Load config file
    config = load_config('config.yml')
    outputdir = config['outputdir'][0] # Folder where starchives will be stored
    ghuser = config['githubuser'][0]
    ghpass = config['githubpassword'][0]
    ghtoken = config['githubtoken'][0]
    load_github(ghuser, ghpass, ghtoken)

    # Make the output filepath if it doesn't already exist
    Path(outputdir).mkdir(parents=True, exist_ok=True)

    # Prompt user for desired action
    init_q = "Would you like to: \nstart a new archive [0] \n update an existing archive? [1]\n"

    # Records user action choice
    ch = handle_input([0, 1], init_q)
    func_switch(ch)
    
main()