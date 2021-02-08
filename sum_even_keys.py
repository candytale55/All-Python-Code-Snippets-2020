# function sum_even_keys takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys in my_dictionary.

def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if (key % 2 == 0):
       total += my_dictionary[key] 
  return total

# Tests:
print(sum_even_keys({1:5, 2:2, 3:3}))
# 2

print(sum_even_keys({10:1, 100:2, 1000:3}))
# 6
