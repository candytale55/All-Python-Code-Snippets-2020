# Python 3 - Coded in 2020 

# same_values() takes two lists of numbers of equal size as parameters. 
# The function returns a list of the INDICES (not the values themselves) where the values were equal in lst1 and lst2.


def same_values(lst1, lst2):
  same_values = []
  index = 0
  for index in range(len(lst1)):
    if (lst1[index] == lst2[index]):
      same_values.append(index)  
  return same_values


#TEST
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# returns [0, 2, 3]



# same_values_numbers() takes two lists of numbers of equal size as parameters. 
# The function returns a list of values, that were equal in lst1 and lst2 at the same index.

def same_values_numbers(lst1, lst2):
  same_values = []
  index = 0
  for index in range(len(lst1)):
    if (lst1[index] == lst2[index]):
      same_values.append(lst1[index])  
  return same_values

print(same_values_numbers([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))



# For reference:
# https://discuss.codecademy.com/t/how-could-i-use-list-comprehension-to-solve-this/458265
# https://discuss.codecademy.com/t/how-can-i-make-this-function-work-for-lists-of-unequal-length/376643
