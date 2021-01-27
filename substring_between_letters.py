# Python 3 (Coded in 2020).

# This returns the substring between the first occurrence of _start_ and _end_ in word. 
# If _start_ or _end_ are not in _word_, the function should return _word_.  
# For example, substring_between_letters("apple", "p", "e") should return "pl".




def substring_between_letters(word, start, end):
  index_start = word.find(start)
  index_end = word.find(end)
  if (index_start == -1 or index_end == -1):
    return word
  else:
    return word[index_start+1:index_end]
  



# Tests
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"
