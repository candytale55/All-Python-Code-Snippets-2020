# function max_key takes a dictionary my_dictionary as a parameter. It returns the key associated with the largest value in the dictionary.


def max_key(my_dictionary):
  higher_value = float("-inf")
  higher_key = ""
  for key, value in my_dictionary.items():
    if value > higher_value:
      higher_value = value
      higher_key = key
  return higher_key 

    


# TESTS
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1

print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


# Other solutions here: https://discuss.codecademy.com/t/solution-sharing/462846/17
