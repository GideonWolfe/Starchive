import re
from art import text2art

'''
Version 0.1
See README.md for usage instructions

Started this repo 60% because of the usefulness and 40% because of the name.
'''
print(text2art("Starchive",font='starwars',chr_ignore=True) + "\n\n\n")

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
    init_q = "Would you like to start a new archive [0] or update an existing archive? [1]\n"

    choice = handle_input([0, 1], init_q)

    


main()