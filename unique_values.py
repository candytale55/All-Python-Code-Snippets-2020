# function unique_values takes a dictionary named my_dictionary as a parameter and returns the number of unique values in the dictionary.

def unique_values(my_dictionary):
  unique_values = []
  for value in my_dictionary.values():
    if value not in unique_values:
      unique_values.append(value)
  return len(unique_values)




# TESTS
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2

print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

# REF: https://discuss.codecademy.com/t/solution-sharing/462901
# https://discuss.codecademy.com/t/why-must-an-empty-list-be-created/462905
