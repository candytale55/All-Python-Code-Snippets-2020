# append_sum takes one parameter (lst) and it should add the last two elements of lst together and append the result to lst. 
# It should do this process three times and then return lst.

# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

def append_sum(lst):
  new = lst[-1] + lst[-2]
  lst.append(new)
  new = lst[-1] + lst[-2]
  lst.append(new)
  new = lst[-1] + lst[-2]
  lst.append(new)
  return lst

#Tests
print(append_sum([1, 1, 2]))
# [1, 1, 2, 3, 5, 8]

print(append_sum([1, 9, 9]))
[1, 9, 9, 18, 27, 45]
