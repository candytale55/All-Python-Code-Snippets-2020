# function sum_values takes a dictionary named my_dictionary as a parameter. It returns the sum of the values of the dictionary

def sum_values(my_dictionary):
  sum_of_values = 0
  for value in my_dictionary.values():
    sum_of_values += value
  return sum_of_values


# Tests
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
#  10

print(sum_values({10:1, 100:2, 1000:3}))
#  6
