# Function reverse_string() takes a string named _word_ as a parameter. The function should return _word_ in reverse.

def reverse_string_basic(word):
  new_word = ""
  x = (len(word)-1)
  for i in range(len(word)):
    new_word += word[x] 
    x-=1
  return new_word



# More concise.
def reverse_string_concise(word):
  new_word = ""
  for i in range(len(word)-1, 0, -1):
    new_word += word[i] 
  return new_word



# Without using range
def reverse_string(word):
  new_word = ""
  for i in word:
    new_word = i + new_word
  return new_word



# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print
