# scrabble_Py_3
Python 3 practice. Use dictionaries to organize players, words, and points from data from a group of friends playing scrabble. 

## General info
The purpose of the project is just personal learning. 

## Description
* There are two lists, _letters_ and _points_ and then dictionary called _letter_to_points_ that maps each letter to its point value.
* A dictionary _letters_to_points_ is created from these lists, using zip comprehension, and an additional key:value is added to account for blank tiles.
* The function _score_word_ takes in a word and return how many points that word is worth.
* A dictionary _player_to_words_ maps players to a list of the words they have played. 
* An originally empty dictionary _player_to_points_ will be filled in a double loop, with _player_ name value as key and a value of _player_points_. 
  * The outer loop iterates through the items in player_to_words (player is _player_ and each list of words is _words_) 
  * The inner loop uses a variable called player_points (set to 0) will add the score per word passed using function _score_word()_ with word as input.

#### To-do list:
* Add a function _play_word()_ that would take in a player and a word, and add that word to the list of words they’ve played
* Add a funciton _update_point_totals()_ to turn the nested loops into a function that you can call any time a word is played

## Technologies
* Python 3

## Setup
NA - It's only coding examples, there's no setup.

## Status
Project is: _finished_, - But I didn't do the extra activities. 

## References
Based on Codecademy's _Learn Python 3_ course
