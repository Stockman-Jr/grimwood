import time
import sys


def typing(text):
    """
    Will type out text letter by letter
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


def input_checker(prompt, opts):
    """
    A loop to prompt user for input and validate it
    """
    choice = input(prompt)

    while choice not in opts:
        print(f"Please enter a valid choice {opts}")
        choice = input(prompt)

    return choice


def win_game(message):
    """
    This function will be called if user clears the game
    and display a message
    """
    typing(message)
    typing("You made it to safety, you won!")


def game_over(message):
    """
    This function will be called if user lose the game
    and display a message
    """
    typing(message)
    typing("You died")
