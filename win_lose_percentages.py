# Functions win_percentage() and lose_percentage() take two parameters named wins and losses.
# return out the total percentage of games won or lost by a team based on these two numbers.

# Write your win_percentage function here:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100

def lose_percentage(wins, losses):
  return losses / (wins + losses) * 100

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100

print(lose_percentage(5, 5))
# should print 50
print(lose_percentage(10, 0))
# should print 0
