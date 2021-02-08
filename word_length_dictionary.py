# function word_length_dictionary takes a list of strings named words as a parameter. It returns a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

def word_length_dictionary(words):
  dictionary = {}
  for word in words: 
    dictionary[word] = len(word)
  return dictionary

# TESTS:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}

print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# Ref: https://discuss.codecademy.com/t/could-this-be-solved-with-list-comprehension/462853
# https://discuss.codecademy.com/t/how-does-the-provided-solution-create-new-keys/462855
