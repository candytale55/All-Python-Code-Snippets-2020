# function _censor_ takes two strings, _text_ and _word_, as input. 
# It should return the text with the word you chose replaced with asterisks. 
# For example: censor("this hack is wack hack", "hack") should return "this **** is wack ****"  

# Assume your input strings won’t contain punctuation or upper case letters. 
# The number of asterisks you put should correspond to the number of letters in the censored word.



def censor (text, word):
  word_list = text.split()
  censored_word = "*"*len(word)
  for i in range(len(word_list)):
    if word_list[i] == word:
      word_list[i] = censored_word
  return " ".join(word_list) 

print censor("hey hey mother fucker", "fucker")




# Other ways to create the censored word:

def censor_a_word_with_for(word):
  censored_word = ""
  for char in word:
    censored_word += "*"
  return censored_word  

print censor_a_word_with_for("hellou")



# https://discuss.codecademy.com/t/how-can-i-use-split-to-make-censor/339351
# https://discuss.codecademy.com/t/why-do-we-need-to-use-a-count-variable-in-censor/346785
# https://discuss.codecademy.com/t/why-do-we-need-to-use-a-count-variable-in-censor/346785




