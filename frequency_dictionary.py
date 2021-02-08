# frequency_dictionary takes a list of elements named words as a parameter. It returns a dictionary containing the frequency of each element in words.

def frequency_dictionary(words):
  frec_dict = {}
  for word in words:
    if frec_dict.get(word) == None:
      frec_dict[word] = 1
    else :
      frec_dict[word]+= 1
  return frec_dict
    

# TESTS
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}

print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}



# FIRST TRY


def frequency_dictionary_wrong (words):
  frec_dict = {}
  for word in words:
    base_word = word
    word_count = 0
    for word in words:
      if word == base_word:
        word_count += 1
      frec_dict [base_word]= word_count
    return frec_dict


# Other solutions: https://discuss.codecademy.com/t/solution-sharing/462893
