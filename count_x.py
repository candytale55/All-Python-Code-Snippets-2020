# count_char_x takes a string named _word_ and a single character named _x_ as parameters. 
# The function should return the number of times _x_ appears in _word_.



def count_char_x(word, x):
  count = 0
  for char in word:
    if char == x:
      count +=1
  return count



# TESTS
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
