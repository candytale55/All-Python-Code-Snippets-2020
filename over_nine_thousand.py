# over_nine_thousand() takes a list of numbers named lst as a parameter. 
# It sums the elements of the list until the sum is greater than 9000. 
# When this happens, the function should return the sum. 
# If the sum is never greater than 9000, the function should return total sum of all the elements. 
# If the list is empty, the function should return 0. 
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand(lst):
  sum = 0
  for element in lst:
    sum = sum + element
    if sum >= 9000:
      return sum
      break
  return sum


# TESTS
print(over_nine_thousand([8000, 900, 120, 5000]))
print(over_nine_thousand([8000, 900]))
print(over_nine_thousand([8000, 1000]))
print(over_nine_thousand([]))
