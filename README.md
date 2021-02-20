# Battleship_Py_2
Build a simplified, one-player version of the classic board game Battleship with Python 2. There will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship. Codecademy practice project.

## General info
The purpose of the project is just personal learning. 

## Description

#### Creating the board:
* A variable _board_ is set it equal to an empty list. This will represent the board. "O" will mean "Ocean", "X" will mean missed shot.

* Function **_create_board_** takes one int parameter _board_size_. Using the built-in _range()_ Python function, looping the number of times indicated by _board_size_ will generate the board, a grid of all "O"s, for “ocean.”. Right now it will have an equal size of rows and columns. 

* Function **_print_board_** takes a single argument, _board_in_. It prints the board out like a grid with each row on its own line using a for loop to iterates through each row in board and print it to the screen.  To get rid of the quote marks and commas part of the list structure we use the _.join_ method with a " " string. 


#### Hiding the battleship:
* Since we have a 2-dimensional list, we’ll use two variables to store the ship’s location, _ship_row_ and _ship_col_. We'll use randint so that the location is random in two functions _random_col_  and _random_row_ that will return a random index.

``` 
def random_col(board_in):   
  return randint(0, len(board_in) - 1) 
```
  
Note that we could just call randint(0, 4), but we use len(board) - 1 in case we want to change the board size later.

#### Seek the batleship:
* Using _raw_input_ asks the user for input and returns it as a string, so we wrap the raw_inputs with int() to convert them to int, to get the player’s guess.

#### Determine win /lose
* We have the actual location of the ship and the player’s guess so we can check to see if the player guessed right. For a guess to be right, guess_col should be equal to ship_col and guess_row should be equal to ship_row.

* Checks if guess_row equals ship_row and guess_col equals ship_col. If that is the case, prints out a note to the user stating he won, and if it isn't, that he lost 

#### Repeat for 4 turns:
* A for loop that repeats the guessing and checking part of your game for 4 turns, like the example above.  At the beginning of each iteration, print "Turn", turn + 1 to let the player know what turn they are on.


#### Game Over:
* If the user guesses wrong on their last turn it prints "Game Over". It must print  no matter what the cause of the misses. So, under the else that accounts for misses and  after the if/elif/else statements that check for the reason the player missed we set an if statement. Our turn variable starts at 0 and goes to 3, we will want to end the game when turn equals 3 (4 turns).

### To-do list:
* The zero-based list may confuse the user, who may be expecting the coordinates to start at 1.
* Make a two-player game.
* Make multiple battleships: Make sure that you don’t place battleships on top of each other on the game board and make to balance the size of the board with the number of ships so the game is still challenging and fun to play.
* Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.


## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [References](#references)


## Screenshots
![Example screenshot](screenshot.jpg)

## Technologies
* Python 2

## Setup
NA - It's only coding examples, there's no setup.

## Status
Project is: _in progress_, _finished_, - may come back and improve it, or not.


## References
Based on Codecademy's _Learn Python 2_ course, _Battleship!_

#### Relevant discussion links
* https://discuss.codecademy.com/t/can-i-make-the-game-have-2-players-and-more-ships/339263
* https://discuss.codecademy.com/t/how-does-the-join-method-work/339268
* https://discuss.codecademy.com/t/how-should-my-conditional-statements-be-nested/339275
* https://discuss.codecademy.com/t/how-can-i-be-sure-i-tested-my-battleship-project-properly/339283
