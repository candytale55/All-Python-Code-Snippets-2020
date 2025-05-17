#larger_sum() takes two lists of numbers as parameters named lst1 and lst2. It returns the list whose elements sum to the greater number. If the sum of the elements of each list are equal, it returns lst1.

# Python 3
# Loops through each list separately and adds to variables sum1 and sum2. After looping is done it, compares the two sums in an if statement and return the correct list.

def larger_sum(lst1, lst2):
  sum1 = 0;
  sum2 = 0;
  for item in lst1:
    sum1 = sum1 + item
  for item in lst2:
    sum2 = sum2 + item
  if sum1 >= sum2:
    return lst1
  else:
    return lst2



print(larger_sum([1, 9, 5], [2, 3, 7])) 
# [1, 9, 5]
