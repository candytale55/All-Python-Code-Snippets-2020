# Python 3 (Coded in 2020)
# function every_other_letter() takes a string named _word_ as a parameter. The function returns a string containing every other letter in word.

def every_other_letter(word):
  new_word = ""
  if (word == ""):
    return "No word given"
  for i in range(len(word)):
    if (i % 2 == 0):
      new_word+= word[i]
  return new_word


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 
