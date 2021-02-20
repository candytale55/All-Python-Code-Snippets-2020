# Battleship_Py_2
Build a simplified, one-player version of the classic board game Battleship with Python 2. There will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship. Codecademy practice project.

## General info
The purpose of the project is just personal learning. 

## Description

#### Creating the board:
* A variable _board_ is set it equal to an empty list. Using the built-in _range()_ Python function, looping 5 times will generate the board, which will be a 5 x 5 grid of all "O"s, for “ocean.”. 

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



#### To-do list:
* Wow improvement to be done 1
* Wow improvement to be done 2


## Table of contents
* [General info](#general-info)
* [Description](#description)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)
* [References](#references)


## Screenshots
![Example screenshot](./img/screenshot.png)

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
