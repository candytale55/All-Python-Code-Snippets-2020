# Python 2

from random import randint

#### Creating the board

board = []

def create_board(board_size):
  for x in range(0, board_size):
    board.append(["O"] * board_size)
    
def print_board(board):
  for row in board:
    print " ".join(row)





## Play the game
create_board(5)
print_board(board)


#### Hiding the battleship:

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

def print_battleship(ship_row,ship_col):
  print ship_row, ship_col


# Play the game

def play_battleship():
  for turn in range(4):
    print "Turn", turn + 1
    # Seeking the battleship
    guess_row = int(raw_input("Guess Row: "))-1
    guess_col = int(raw_input("Guess Col: "))-1

    # Determine a win    
    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sank my battleship!"
      break   

    # Handle incorrect guesses
    else:
      if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
      elif board[guess_row][guess_col] == "X":
        print( "You guessed that one already." )
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
      print_board(board)
      print ""

      # Game Over
      if turn == 3:
        print "Game Over"


play_battleship()


# https://discuss.codecademy.com/t/why-do-i-get-a-break-outside-of-loop-error/339281

# https://discuss.codecademy.com/t/why-do-i-get-a-break-outside-of-loop-error/339281
# https://discuss.codecademy.com/t/how-is-this-list-of-lists-going-to-look-like-a-board/339266
# https://discuss.codecademy.com/t/how-do-i-print-each-row-of-the-board/339267
