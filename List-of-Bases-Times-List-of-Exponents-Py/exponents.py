# Python 3. Coded in 2020

#exponents() takes two lists as parameters named bases and powers. 
#Return a new list containing every number in bases raised to every number in powers. 
#For example with exponents([2, 3, 4], [1, 2, 3])  the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64] 
#because it would first include the three solutions for base 2  [(2**1), (2**2) and (2**3)], 
#then for the next base (3) and so on. 



def exponents(bases, powers):
  new_list = []
  for base in bases: 
    for exponent in powers:
      new_list.append(base**exponent)
  return new_list


# TESTS:
print(exponents([2, 3, 4], [1, 2, 3]))

print(exponents([3, 9, 12], [1, 2, 3]))
