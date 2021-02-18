# Python_2_Lists_and_Dictionaries_Exercises
Codecademy exercises and notes to learn about the data structures lists and dictionaries in Python 2. It simulates a simple console-based program for a produce shop. 

#### Topics:
* Using for loops with lists and dictionaries.
* Writing functions with loops, lists, and dictionaries
* Updating data in response to changes in the environment (for instance, decreasing the number of bananas in stock by 1 when you sell one).

## Purpose
The purpose of the project is just personal learning. I may revisit this code to find different solutions or to apply it under other context. 

## Description
The exercise is an online supermarket. It reads like this _" You are now the proud owner of your very own Codecademy brand supermarket. As a store manager, you’re also in charge of keeping track of your stock/inventory. For paperwork and accounting purposes, let’s record the total value of your inventory. In order for customers to order online, we are going to have to make a consumer interface."_

Function _compute_bill_ takes one argument _food_ as input. Variable _total_ with initial value of zero is used as counter. For each item in the food list, add the price of that item to total.  If an item isn’t in stock, then it shouldn’t be included in the total. You can’t buy or sell what you don’t have! Funciton only adds the price of the item to total if the item’s stock count is greater than zero. If the item is in stock and after you add the price to the total, subtract one from the item’s stock count. Finally, returns the total.

## Technologies
* Python 2

## Setup
NA - It's only coding examples, there's no setup.

## Status
Project is: _finished_.


## References
Based on Codecademy's _Learn Python 2_ course

