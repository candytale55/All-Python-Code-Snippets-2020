# Magic-8-Ball-Python3
This program answers any “Yes” or “No” question with a different random fortune each time it executes.  It is inspired in the Magic 8-Ball, a popular toy developed in the 1950s for fortune-telling or advice seeking.


## General info

magic8_elifs.py answers any “Yes” or “No” question with a different random fortune each time it executes using randint and an if/elif/else control flow.  

## Features

* The Magic 8-Ball will give at least these 9 answers:
    + Yes - definitely.
    + It is decidedly so.
    + Without a doubt.
    + Reply hazy, try again.
    + Ask again later.
    + Better not tell you now.
    + My sources say no.
    + Outlook not so good.
    + Very doubtful.

* The output of the program will have this form:

  [Name] asks: [Question]
  Magic 8-Ball’s answer: [Answer]

  If the the value of name is an empty string it should print out just the question, like this:

  [Question]
  Magic 8-Ball’s answer: [Answer]

*  If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune



#### To-do list:
* elifs means the randint range must be manually fixed everytime a new answer is included to the elifs flow. Change it to a list and use the list lenght to automatically update the range of random. 
* The _name_ and _question_ variables are hard coded. Include input() to request the information to the user. 


## Technologies
* Python 3

## Setup
NA - It's only coding examples, there's no setup.

## Status
Project is: technically _finished_ but I will probably come back and do the stuff in the to-do-list.

## References
Project based on Codecademy _Magic 8-Ball_ project from _Learn Python 3_ course
More info about Magic 8-balls: https://en.wikipedia.org/wiki/Magic_8-Ball and in Spanish too: https://es.wikipedia.org/wiki/Magic_8-Ball . It's cool, the real life Magic 8-balls are or were made with a cylindrical reservoir that contains a white plastic icosahedron die floating in ~100mL of alcohol dyed dark blue. 
