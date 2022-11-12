# Grimwood
Grimwood is a command line game in the genre of text-based adventure/survival.
It's the old but cliché story where the character wakes up in the middle of the woods with no memory of how they got there, and they're not alone.... 
The user will navigate through the story by typing an option of their choice in the command line when prompted to.
The goal of the game is to make the right choices and make it out of the woods alive.

- - - 

## Table of Contents

* [User Stories](#user-stories)
* [Design](#design)
* [Features](#features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
* [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Bugs](#bugs)
    * [Unsolved Bugs](#unsolved-bugs)
* [Technologies Used](#technologies-used)
  * [Main Languages](#main-languages)
  * [Frameworks, Libraries & Programs](#frameworks-libraries--programs)
* [Deployment](#deployment)
* [Credits](#credits)
  * [Code](#code)

  
- - -
## User Stories

### As a user playing the game I want..
  * Clear instructions
  * The game content to be displayed nicely so that it's easy to read
  * For the game to be engaging and fun enough to play again
  * To experience different outcomes based on my choices

### As a site owner I want..
  * For input to be handled efficiently
  * To provide a fun and engaging gaming experience
  * For the game to be clear to users at all times

- - -
## Design

- - -
## Features

### Existing Features


#### Start screen
The starting screen features an ascii art banner, and will ask the user to provide a name. The name will only be accepted if it only contains letters.
A short introduction message will then be displayed for the user, and let them know how to play the game.
The user will then be able to press enter to start the game.

The purpose of this is to introduce the user to the story and how to play the game.

#### Displaying text contents
Since this game is pretty heavy on the story part, I've done my best to make everything as clean and readable as possible using colorama library, whitespacing and new lines. The longer parts of the story are all colored text, and has been placed in a separate file to keep the main game file cleaner.
The purpose of this is to not overwhelm the user and provide them with a structured and clean output, so that it's easy to keep up.


#### Player options
The options provided will be displayed for the user along with a prompt that will mostly ask for a direction or a choice between a-d.

#### Winning and losing
If the user wins or lose the game, a function will be called to display a message. In both scenarios a prompt will also appear to ask the user if they want to play again, typing "yes" will restart the game, and any other key press will exit the game.



### Future Features
  * I would like to implement more types of user interactions to the game, maybe provide some puzzles for the user to solve.
  * More "rooms" and outcomes.



---

## Testing




### Validator Testing





### Bugs

#### Bug
  * **Expected** - 
  * **Testing** - 
  * **Result** -
  * **Fix** - 




### Unsolved bugs
 
---

## Technologies Used

### Main Languages
  * Python

### Frameworks, Libraries & Programs
  * Python libraries used:
      * colorama
      * time
      * sys
  * [GitHub](https://github.com/) - To save and store files for the website.
  * Git - For version control.
  * Visual Studio Code(desktop) - for testing and experimenting with code
  * LucidChart - for creating a flow chart to map out the game
---

## Deployment

---

## Credits

### Code
