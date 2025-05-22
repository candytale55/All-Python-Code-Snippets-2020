# Python 2 (Coded in 2020)

"""
Rock, Paper, Scissors is a hand game usually played between two people, in which each player 
simultaneously forms one of three shapes with an outstretched hand. 

Features:
The program should do the following:
*Prompt the user to select either Rock, Paper, or Scissors.
Instruct the computer to randomly select either Rock, Paper, or Scissors.
Compare the user's choice and the computer's choice.
Determine a winner (the user or the computer).
Inform the user who the winner is.
"""

from random import randint
from time import sleep

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay, you won!",
  "lost":"Aww, you lost!"
}

def decide_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    print message["tie"]
  # Cases when the user wins  
  elif user_choice == "ROCK" and computer_choice =="SCISSORS":
    print message["won"]
  elif user_choice == "PAPER" and computer_choice =="ROCK":
    print message["won"]
  elif user_choice == "SCISSORS" and computer_choice =="PAPER":
    print message["won"]
  else:
    print message["lost"]


def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper() #Is quicker than adding it to raw_input above.
  computer_choice = options[randint(0,2)]
  sleep(1)
  print "User choice is %s" % user_choice
  print "getting computer choice . . ."
  sleep(1)
  print "Computer choice is %s" % computer_choice
  sleep(1)
  decide_winner(user_choice, computer_choice)



play_RPS()




# Tests
     ## User won ##
#decide_winner("ROCK", "SCISSORS")
#decide_winner("SCISSORS", "PAPER")
#decide_winner("PAPER", "ROCK")
     ## ties ##
#decide_winner("ROCK", "ROCK")
#decide_winner("SCISSORS", "SCISSORS")
#decide_winner("PAPER", "PAPER")
     ## User lost ##
#decide_winner("ROCK", "PAPER")
#decide_winner("SCISSORS", "ROCK")
#decide_winner("PAPER", "SCISSORS")

