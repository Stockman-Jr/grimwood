import time
import story
from functions import typing, input_checker, win_game, game_over
from colorama import Style

modern_flashlight = False
old_flashlight = False
visited = False
OPTIONS = ['a', 'b', 'c', 'd', 'east', 'south', 'west']
print(Style.BRIGHT)


def start_game():
    """
    Prompts user for a name, gives a short introduction
    Then provides to option to start the game
    """

    typing("Well, hello stranger.\n")

    while True:
        player_name = input("Tell me your name.. >\n")
        if player_name == "":
            print("Please... your name.")
        else:
            break

    typing(f"I see... {player_name}. Welcome.\n")
    time.sleep(1)

    typing(story.INTRO_MSG)
    time.sleep(1)
    typing(f"Good luck {player_name}....\n")
    typing(input("Press enter to start game...\n"))
    intro_scene()


def intro_scene():
    """
    First scene of the game, where user will be able
    to choose which direction to take
    """
    global visited
    if visited is False:
        typing("""
        It's almost pitch black, you give yourself a minute to adjust your
        eyes to the darkness.\n""")
        typing("""
        You stand up and look around, you're standing on a path that
        splits in two directions.\n\n""")
    else:
        typing(
            "You're back on the path that splits in two directions.\n")
    time.sleep(1)

    choices = input_checker(
        "Which way will you go? Type east or south.\n\n", OPTIONS[4:6])

    if choices == "east" and visited is False:
        fruit_grove()
    elif choices == "east" and visited is True:
        typing("You probably shouldn't go back there..\n\n")
        time.sleep(0.5)
        return intro_scene()
    elif choices == "south":
        three_fork_path()


def fruit_grove():
    """
    If user chose east from intro scene, this function will play out.
    Some story will be told and then user will be provided with two options.
    """
    global visited

    typing("You've been walking for ten minutes when you suddenly stop.\n")
    typing("""
    You see in front of you what looks like a small grove
    surrounded by trees bearing fruit.
    You stop to think..\n""")

    typing("""
    A. Some fruit might come in handy for your survival, after all you
    have no idea where you are and how long you might be
    stuck in these woods. Go forward and pick up some fruit.\n""")
    typing("""
    B. Seems like a waste of time, you're not hungry.
    Go back and head south instead.\n\n""")

    choices = input_checker(
        "What will you do?(a/b) >> ", OPTIONS[0:2])

    if choices == "a":
        # typing(story.DEAD_GROVE)
        game_over("Didn't last very long did you?\n", start_game)
    elif choices == "b":
        visited = True
        intro_scene()
        return visited


def three_fork_path():
    """
    If user chose south from intro_scene, this function will play out.
    Some story will be told and then user will be prompted to choose
    from three directions.
    """

    typing("""
    You arrive at a three-way-fork in the path.\n
    You stop to think...\n""")
    typing("Looking east, you see a strange, faint light.\n")
    typing("""
    Looking west, the forest looks denser,
    making it darker and harder to see.\n""")
    typing(
        "Maybe you should ignore the paths and continue south, off piste.\n\n")

    choices = input_checker(
        "Where will you go?(west/east/south) >> ", OPTIONS[4:8])

    if choices == "east":
        flashlight_scene()
    elif choices == "west":
        creatures_den()
    elif choices == "south" and modern_flashlight is True:
        abandoned_house()
    elif choices == "south" and modern_flashlight is False:
        game_over("""
        As you walk for hours, struggling to see
        in the darkness, you start to realise that you're lost.
        And as you entered a denser, almost pitch-black part of the woods,
        you could'nt see the cliff you were walking towards..\n""", start_game)


def flashlight_scene():
    """
    If user chose west from three_fork_path, this function will play out.
    The user fill find a flashlight and choose whether to keep it or not.
    That choice will update the global modern_flashlight variable.
    A scene will then play out and promp user to choose from two options.
    """
    global modern_flashlight
    typing(story.FOUND_ITEM)
    time.sleep(1)
    typing("Would you like to keep it?(yes/no) >> \n")
    userInput = input()

    if userInput == "yes":
        modern_flashlight = True
        print("You kept the flashlight.")
        typing(story.ENCOUNTER)
    elif userInput == "no":
        modern_flashlight = False
        win_game("""
        For some reason, unbeknownst to anyone,
        you decided to not keep the flashlight and kicked
        it far off into the woods.

        You kept walking east as you were pondering over this and that.
        After a few hours of walking, you notice the lights of a town
        in front of you...""", start_game)

    typing("You take a second to think...\n")

    typing("""
    A. It's probably your imagination, or some kind of animal.
    Direct your flashlight towards the sounds and see what it is.\n""")
    typing("B. Trust your instincs, flee! Run back to the three-way-fork.\n")

    choices = input_checker(
        "What will you do?(a/b) >> ", OPTIONS[0:2])

    if choices == "a":
        game_over("""
        Whatever it was, it pinpointed your location
        once you shone your light towards it, and it was fast..
        """, start_game)
    elif choices == "b":
        three_fork_path()

    return modern_flashlight


def creatures_den():
    """
    If user chose west from three_fork_path, this function will play out.
    This is where the creature lives, and user will only survive if
    old_flashlight is True.
    """

    if modern_flashlight is True:
        typing(story.DEN_DEATH)
        game_over("then it charges..", start_game)
    elif old_flashlight is True:
        typing(story.DEN_SURVIVAL)
        win_game("""
        As you reach the end of the tunnel
        you see city lights flickering in the distance..""", start_game)
    else:
        game_over("""
        You walk into pitch-black darkness, you can't see a thing.
        But the path is flat and straight, so you keep walking.
        Suddenly you feel something extremely sharp, pierce through your chest.
        """, start_game)


def abandoned_house_encounter():
    """
    This scene will play out if user found old flashlight
    Story will progress and user will be prompted to make another choice
    to proceed further
    """
    global old_flashlight

    typing(story.HOUSE_ENCOUNTER)
    time.sleep(1)
    choices = input_checker("""
    What will you do?(a/b/c)

    A. Slap yourself to release you from the paralyzing fear, and RUN!!!

    B. You're frozen in fear, you stay still and watch as you squeeze the old
    flashlight.

    C. Turn off the flashlight, hold your breath and hide under the desk.

    >>> """, OPTIONS[0:3])
    if choices == "a":
        game_over("""
        You tried to run, but trying to outrun this
        creature proved to be fatal...""", start_game)
    elif choices == "b":
        typing(story.HOUSE_ENCOUNTER_OUTCOME)
        final_decisions()
    elif choices == "c":
        game_over("""
        You close your eyes and cover your mouth,
        hoping for the nightmare to be over..
        And so your hopes came true, but not in a good way..
        """, start_game)


def abandoned_house():
    """
    If user chose south from three_fork_path, this function will play out.
    User can only reach this point if modern_flashlight is True
    """
    global old_flashlight

    typing(story.HOUSE)
    typing("""
        In the left corner there's a bed with a nightstand next to it,
        seems to have two drawers.\n""")
    typing("""
        In front of you there is a desk and a chair, with piles of notes
        and books scattered across the floor and desk.\n""")
    typing("""
        You should probably look around..
        You think about where to start...\n""")

    print("""
          A. Underneath the bed

          B. Check the nightstand

          C. Underneath the desk

          D. Check what's on top of the desk

          """)
    for choices in range(2):
        choices = input_checker("""
        What would you like to investigate?(a/b/c/d) >>
        """, OPTIONS[0:4])

        if choices == "c":
            typing(story.HOUSE_ITEM)
            old_flashlight = True
            abandoned_house_encounter()
            return old_flashlight
        elif choices == "a":
            print(
                """You go to the bed, crouch down and use your
                   flashlight to see what's there..\n""")

            print("Nothing but spiderwebs and dusty old notes..")
        elif choices == "b":
            print("You go to the nightstand and open the drawers..")

            print("Just trash, nothing useful.")
        elif choices == "d":
            print("You go to the desk to check what's on it..")

            print("""Creepy books, notes written in a language you can't
            depict and a tin box that's empty... Nothing useful here.\n""")
    else:
        typing(story.HOUSE_ENCOUNTER)
        game_over("And so your death was inevitable...", start_game)


def final_decisions():
    typing("'What the heck just happened?'\n")
    typing("No point in trying to grasp it, you gotta move on. Will you..\n")
    typing("""
        A. Go back to the path, off piste was a bad idea.

        B. Continue south.\n""")

    choices = input_checker("Where will you go? (a/b) >> ", OPTIONS[0:2])
    if choices == "a":
        three_fork_path()
    elif choices == "b":
        typing(story.SOUTH_SURVIVAL)
        sleep.time(1)
        win_game("""
        'I should probaly keep this....'
        you muttered to yourself as you made your way to safety.
        """, start_game)


start_game()
