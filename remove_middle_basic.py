# Create a function named remove_middle which has three parameters (lst, start, end). 
# The function should return a list where all elements in lst with an index 
# between start and end (inclusive) have been removed.

# For example remove_middle([4, 8 , 15, 16, 23, 42], 1, 3) should return 
# [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:


def remove_middle(lst, start, end):
  lst_start = lst[:start]
  lst_end = lst[end+1:]
  return lst_start + lst_end

# Return in one line
def remove_middle_improved(lst, start, end):
  return lst[:start] + lst[end+1:]



#This would do the opposite, return the elements in lst between indexes start and end (inclusive)
def dont_remove_middle(lst, start, end):
  return lst[start:end+1]


# TESTS
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))  # [4, 23, 42]

print(remove_middle_improved([4, 8, 15, 16, 23, 42], 1, 3))  # [4, 23, 42]
