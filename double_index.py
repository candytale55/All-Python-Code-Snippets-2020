# Function double_index takes two parameters: a list (lst) and a single number (index). 
# It should return a new list where all elements are the same as in lst except for the element at index. 
# The element at index should be double the value of the element at index of the original lst.

# For example, double_index([1, 2, 3, 4], 2) should return [1,2,6,4] because the element at index 2 has been doubled.

# If index is not a valid index, the function should return the original list.


def double_index(lst, index):
  if index >= 0 and index < len(lst):
    lst[index] = lst[index] * 2
    return lst
  else: 
    return lst



# TESTS
print(double_index([3, 8, -10, 12], 2))
# [3, 8, -20, 12]

print(double_index([3, 8, -10, 12], 7)) # invalid index
# [3, 8, -10, 12]
