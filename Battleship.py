# Python 2


# Creating the board:
# variable board is set it equal to an empty list. Using the built-in range() Python function, looping 5 times to generate the board, which we’ll make into a 5 x 5 grid of all "O"s, for “ocean.”

board = []

board_rows = 5
for i in range(0, board_rows):
  board.append(['O ' * board_rows])

# Function _print_board_ takes a single argument, _board_in_. It prints the board out like a grid with each row on its own line using a for loop to iterates through each row in board and print it to the screen. To get rid of the quote marks and commas part of the list structure we use the _.join_ method with a " " string. 

def print_board (board_in):
  for row in board_in:
    print " ".join(row)

print_board(board)





# https://discuss.codecademy.com/t/how-is-this-list-of-lists-going-to-look-like-a-board/339266
# https://discuss.codecademy.com/t/how-do-i-print-each-row-of-the-board/339267
