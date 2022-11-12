import time
import sys
from colorama import Fore
import getch

BANNER = print(Fore.RED + """
       ▄█▀─▄▄▄▄▄▄▄─▀█▄
       ▀█████████████▀
       ────█▄███▄█
       ─────█▀█▀█
            
█▀▀ █▀█ █ █▀▄▀█ █░█░█ █▀█ █▀█ █▀▄
█▄█ █▀▄ █ █░▀░█ ▀▄▀▄▀ █▄█ █▄█ █▄▀ 

""" + Fore.RESET)

YOU_DIED = ("""

                   YOU DIED   
                        
                                ▄▄▄░
           ▄▄▄▄░              ░█████░   
          ░████▌               ▐███▀   ▐▌
      ░    ░▀▀▀░                       █
       ▓                             ▐▌
        █▒                          ▐▓
         ▀▓▄                     ▄▐▌█
           ▒▀▌▄ ▄              ▄▐▌▐▌▌
             ▐████▀█▐▓▐█▒██▐█▒▀██▐░
              ▀▀▌▀█░▓▓▐▓░▓▒░▀░▌█▌
                 ░▀▐▐▓░█▒▓▒▐▓▐░
                     ▀ █▒█▌░▀
    
      """)


def typing(text):
    """
    Will type out text letter by letter
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


def player_menu(func):
    while True:
        print("Press enter to start game, or 'i' for instructions.\n")
        char = getch.getch()
        if char == "\n":
            func()
            break
        elif char == "i":
            print("""
        How to play:
        You'll be provided with options to
        choose from throughout the game, just type in the
        option of your choice when prompted to and press enter.\n\n""")


def input_checker(prompt, opts):
    """
    A loop to prompt user for input and validate it
    """
    choice = input(prompt)

    while choice not in opts:
        print(Fore.BLUE + f"Please enter a valid choice {opts}" + Fore.RESET)
        choice = input(prompt)

    return choice


def win_game(message):
    """
    This function will be called if user clears the game
    and display a message
    """
    typing(message)
    time.sleep(1)
    print("•·✦º✦·» ヽ(´▽`)/ «·✦º✦·•\n")
    typing("You survived Grimwood and made it to safety, you won!")
    time.sleep(1)
    play_again(func)


def game_over(message, func):
    """
    This function will be called if user lose the game
    and display a message
    """
    typing(message)
    time.sleep(1)
    print(YOU_DIED)
    play_again(func)


def play_again(restart):
    print("Would you like to play again?\n")
    choice = input("Type 'yes' or click button at the top to restart game. >> ")
    if choice == "yes":
        restart()
    else:
        print("Wise choice... Thanks for playing.")
        exit()
