# RPS_rock_paper_scissors_Python_2
Console game of rock, paper, scissors. It asks user for user's option and gets computer option using randint, then compares options and prints the winner. 

## General info
Rock, Paper, Scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). "Scissors"

The rules are:
rock beats scissors but will lose to paper.
paper loses to scissors, but beats rock.
scissors beats paper, but loses to rock.

## Features
The program should do the following:
* Prompt the user to select either Rock, Paper, or Scissors.
* Instruct the computer to randomly select either Rock, Paper, or Scissors.
* Compare the user’s choice and the computer’s choice.
* Determine a winner (the user or the computer).
* Inform the user who the winner is.

## Program parts

__options__: List with the possible options (Rock, Scissors, Paper)

__message__: dictionary that holds the messages for the user in case of win, lost or tie.

__decide_winner()__: function that takes two parameters: user_choice and computer_choice and will return the winner.
Scenarios in which the user wins:
* User: _Rock_, Computer: _Scissors_
* User: _Paper_, Computer: _Rock_
* User: _Scissors_, Computer: _Paper_

If it’s not a tie, and the user did not win, that only means the user lost.

__play_RPS()__ funtion that plays the game. It asks user for an option and gets computer option using randint, then calls decide_winner()


## To-do list:
* Add more flexibility to user input. Right now it only converts everything to CAPS. Let the user enter just intitials for instance.
* Set the option of both choices being random.
* Allow to set number of games to play before winning (i.e. win 2 of 3 games)
* Add the nerdier results like calling _Bureaucrat!_,or _Avalanche!_ when the results match. (See https://en.wikipedia.org/wiki/Rock_paper_scissors#Strategies)


## Screenshots
![Example screenshot](.screenshot.png)

## Technologies
* Python 2

## Setup
NA

## Status
Project is: technically _finished_ but probably will revisit. 

## References
Based on Codecademy's course Learn Python 2.
