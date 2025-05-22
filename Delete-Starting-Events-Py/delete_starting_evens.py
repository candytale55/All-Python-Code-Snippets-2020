# Function delete_starting_evens() takes a parameter named lst. 
# The function should remove elements from the front of lst until the front of the list is not even. 
# The function should then return lst.

# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

# The function must work even if every element in the list is even!



def delete_starting_evens(lst):
  while (len(lst)>0 and lst[0] % 2 == 0): 
  #print(str(lst[0]) + " I'm even")
    lst = lst[1:]
  #print(str(lst[0]) + " I'm odd now!")
  return lst 

# TEST
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
