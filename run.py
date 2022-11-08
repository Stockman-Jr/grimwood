import time
import story
from functions import typing

modern_flashlight = False
old_flashlight = False
OPTIONS = ['a', 'b', 'c', 'd', 'east', 'south', 'west']


def start_game():
    typing("Well, hello stranger.\n")
    player_name = input("Tell me your name.. >\n")
    typing(f"I see... {player_name}. Welcome.\n")
    # time.sleep(1)

    # typing(story.INTRO_MSG)
    # time.sleep(1)
    typing(f"Good luck {player_name}....\n")
    typing(input("Press enter to start game...\n"))