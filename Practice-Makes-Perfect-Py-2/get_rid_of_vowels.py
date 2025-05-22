# function anti_vowel takes one string "text", as input and returns the text with all of the vowels removed. 
# For example: anti_vowel("Hey You!") should return "Hy Y!". Don’t count Y as a vowel. Make sure to remove lowercase and uppercase vowels.

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def anti_vowel(text):
  no_vowels = ""
  for letter in text:
    if letter not in vowels:
      no_vowels += letter
  return no_vowels


print anti_vowel("abcdefghi")



# https://discuss.codecademy.com/t/why-does-anti-vowel-fail-in-some-cases/339348
