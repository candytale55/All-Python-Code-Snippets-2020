# function make_spoonerism() takes two strings as parameters named _word1_ and _word2_. Spoonerism switch the first letters of each word and returns the two new words as a single string separated by a space.

# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”.

def make_spoonerism(word1, word2):
  spooned_word = word2[0]+ word1[1:] + " " + word1[0]+ word2[1:]
  return spooned_word
  

#  TESTS:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
