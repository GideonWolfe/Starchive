import re
from art import text2art

'''
Version 0.1
See README.md for usage instructions

Started this repo 60% because of the usefulness and 40% because of the name.
'''

# Globals

def new_archive():
    print("new archive")
    return 1

def existing_archive():
    print("Existing Archive")
    return 1

def func_switch(arg):
    switch = {
        0: new_archive,
        1: existing_archive,
    }
    ch_func = switch.get(arg, lambda: "Invalid Option")
    print (ch_func())
    return 1

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
    print(text2art("Starchive",font='starwars',chr_ignore=True) + "\n\n\n")
    init_q = "Would you like to start a new archive [0] or update an existing archive? [1]\n"

    ch = handle_input([0, 1], init_q)
    func_switch(ch)
    
main()