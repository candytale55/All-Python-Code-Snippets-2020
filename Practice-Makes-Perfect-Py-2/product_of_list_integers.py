""" function _product_ that takes a list of integers as input and returns the product of all of the elements in the list. 
For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100). The function should return an integer. """



def product(integer_list):
  total = 1
  if len(integer_list) == 0:
    return 0
  for num in integer_list:
    total *= num
  return int(total)
  


print product([])  # 0
print product([4, 5, 5]) # 100
