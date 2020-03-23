import re
import yaml
import os
import io
from pathlib import Path
from github import Github
from art import text2art

from repo_scraper import get_github_repos
from repo_scraper import get_gitlab_repos
from repo_scraper import clone_repos

'''
Version 0.1
See README.md for usage instructions

Started this repo 60% because of the usefulness and 40% because of the name.
'''

conf = {}
repos = {}

# Load config file
def load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
# Create directories given path
def handle_path(add_dir):
    try:
        if(Path(add_dir).is_dir() == False and add_dir != "/ADD_PATH"):
            Path(add_dir).mkdir(parents=True, exist_ok=True)
    except PermissionError:
        print("\nConfiguration Error: Incorrect permissions! Could not create path from outputdir.\n")
        exit()
# Create user directories 
def handle_directories():
    global conf
    users_dat = conf['users']

    os.chdir(conf['defaults']['outputdir'])
    for key in users_dat:
        user_path = str(key) + "-" + users_dat[key][0]
        handle_path(user_path)

# Execute when a user wants to update all existing archives
# Note: Made executive decision to add in ability to update certain users later and focus on getting all pulled now...
def full_archive():
    global conf
    global repos
    arc_dir = conf['defaults']['outputdir']

    handle_directories()

    users_dat = conf['users']
    os.chdir(arc_dir)
    for key in users_dat:
        # Create partial path for repos cloning
        user_path = (str(key) + "-" + users_dat[key][0])
        repo_dir = (arc_dir + "/" + user_path)
        # Get repositories of user
        if(users_dat[key][1] == "gitlab"):
            repos = get_gitlab_repos(users_dat[key][0], users_dat[key][2])
        elif(users_dat[key][1] == "github"):
            repos = get_github_repos(users_dat[key][0], users_dat[key][2])
        # Clone all repos
        clone_repos(repos, arc_dir, repo_dir)

def main():
    global conf

    print(text2art("Starchive",font='starwars',chr_ignore=True) + "\n\n\n")
    # Load config file & save config file
    with open("config.yaml", 'r') as stream:
        conf = yaml.safe_load(stream)

    outdir = conf['defaults']['outputdir']
    # Make the output filepath if it doesn't already exist
    handle_path(outdir)
    # Update Existing Archives
    full_archive()
    
main()
