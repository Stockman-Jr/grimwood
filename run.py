import time
import story
from functions import typing, input_checker

modern_flashlight = False
old_flashlight = False
OPTIONS = ['a', 'b', 'c', 'd', 'east', 'south', 'west']


def start_game():
    """
    Prompts user for a name, gives a short introduction
    Then provides to option to start the game
    """
    typing("Well, hello stranger.\n")
    player_name = input("Tell me your name.. >\n")
    typing(f"I see... {player_name}. Welcome.\n")
    # time.sleep(1)

    # typing(story.INTRO_MSG)
    # time.sleep(1)
    typing(f"Good luck {player_name}....\n")
    typing(input("Press enter to start game...\n"))


def intro_scene():
    """
    First scene of the game, where user will be able
    to choose which direction to take
    """
  
    # typing(
    #   "It's almost pitch black, you give yourself a minute to adjust your eyes to the darkness.\n")
    typing(
        "You stand up and look around, you're standing on a path that splits in two directions.\n")
    time.sleep(1)

    choices = input_checker(
        "Which way will you go? Type east or south.\n", OPTIONS[4:7])

    if choices == "east":
        fruit_grove()
    elif choices == "south":
        three_fork_path()


def fruit_grove():
    """
    If user chose east from intro scene, this function will play out.
    Some story will be told and then user will be provided with two options.
    """


def three_fork_path():
    """
    If user chose south from intro_scene, this function will play out.
    Some story will be told and then user will be prompted to choose
    from three directions.
    """


def flashlight_scene():
    """
    If user chose west from three_fork_path, this function will play out.
    The user fill find a flashlight and choose whether to keep it or not. 
    That choice will update the global modern_flashlight variable.
    A scene will then play out and promp user to choose from two options.
    """


def creatures_den():
    """
    If user chose east from three_fork_path, this function will play out.
    This is where the creature lives, and user will only survive if 
    old_flashlight is True.
    """


def abandoned_house():
    """
    If user chose south from three_fork_path, this function will play out.
    User can only reach this point if modern_flashlight is True
    """


start_game()
