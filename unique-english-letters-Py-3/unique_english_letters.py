# Python 3 (Coded in 2020)
# The function iterates through _word_, and compares if the letter is already in the list _unique_ (that starts as an empty list). 
# If it hasn't been added to unique before, it appends it. The function returns the length of _unique_


letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def unique_english_letters(word):
  uniques = []
  for letter in word: 
    if letter in word and not letter in uniques:
      uniques.append(letter)
  return len(uniques)


print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
print(unique_english_letters("Mama"))
# prints 3
