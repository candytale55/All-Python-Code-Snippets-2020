

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# Find the second to last character in company_motto. 
second_to_last = company_motto[-2:-1]
print(second_to_last) # f

# create a slice of the last 4 characters in company_motto.
final_word = company_motto[-4:]
print(final_word) # life



# get_length() that takes a string as an input and returns the number of characters in that string. 
# Do this by iterating through the string, don’t cheat and use len()

def get_length(input):
  char_num = 0
  for letter in input:
    #print(letter)
    char_num += 1
  return char_num

print(get_length("Albus")) # 5



# Find / count characters within a string

favorite_fruit = "blueberry"
counter = 0
for character in favorite_fruit:
  if character == "b":
    counter = counter + 1
print(counter) # 2


def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False
 # This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
  for char in word:
    if char == letter:
      return True
  return False

print(letter_check("Albus", "u")) # True



#  "letter in word" is a boolean expression that is True if the string letter is in the string word. Here are some examples. It not only works with letters, but with entire strings as well.

print("melon" in "watermelon") # True
print("melon" in "butterfly")  # False



# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string. For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.

def contains_long(big_string, little_string):
  if little_string in big_string:
    return True
  return False

# Better solution:
def contains(big_string, little_string):
  return little_string in big_string



# Write a function called common_letters that takes two arguments, string_one and string_two and then returns a list with all of the letters they have in common.

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common


print(common_letters("butterfly", "fly")) # ['f', 'l', 'y']

print(common_letters("mississippi", "pizza")) # ['i', 'p']

print(common_letters("mississippi", "bear")) # []
