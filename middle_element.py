# Create a function called middle_element that has one parameter named lst.  
# If there are an odd number of elements in lst, the function should return the middle element. 
#If there are an even number of elements, the function should return the average of the middle two elements.


def middle_element_long(lst):
  if len(lst) % 2 == 0:
    index1 = lst[int(len(lst)/2)-1]
    index2 = lst[int(len(lst)/2)]
    return (index1 + index2) / 2
  else:
    return lst[int(len(lst)/2)]


# Less lines of code:
def middle_element(lst):
  if len(lst) % 2 == 0:
    return (lst[int(len(lst)/2)-1] + lst[int(len(lst)/2)]) / 2
  else:
    return lst[int(len(lst)/2)]


#TESTS

print(middle_element([5, 2, -10, -4, 4, 5])) # -7.0

print(middle_element([5, 2, -10, -4, 4])) # -10
