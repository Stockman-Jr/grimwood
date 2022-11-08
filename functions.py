import time
import sys


def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


def input_checker(prompt, opts):
    choice = input(prompt)

    while choice not in opts:
        print(f"Please enter a valid choice {opts}")
        choice = input(prompt)

    return choice