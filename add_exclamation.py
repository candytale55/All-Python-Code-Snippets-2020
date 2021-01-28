# add_exclamation() takes one parameter named _word_. This function should add exclamation points to the end of _word_ until word is 20 characters long. If _word_ is already at least 20 characters long, just return _word_.

def add_exclamation(word):
  for i in range(20-len(word)):
    word += "!"
  return word


#  TESTS:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
