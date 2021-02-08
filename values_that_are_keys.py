# function values_that_are_keys takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.

def values_that_are_keys(my_dictionary):
  list_of_values_that_are_keys = []
  for value in my_dictionary.values():
    for key in my_dictionary.keys():
      if value == key:
        list_of_values_that_are_keys.append(value)
  return list_of_values_that_are_keys
    

# TESTS
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]

print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
