#function digit_sum_floor_div takes a positive integer n as input and returns the sum of all that number’s digits. 
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)


# 2nd solution: To get the rightmost digit of a number, you can modulo (%) the number by 10. 
# To remove the rightmost digit you can floor divide (//) the number by 10. 
# (Don’t worry if you’re not familiar with floor division—you can look up the documentation here: 
# http://docs.python.org/2/reference/expressions.html#binary-arithmetic-operations


# Try working this into a pattern to isolate all of the digits and add them to a total.



def digit_sum_floor_div(num):
  total = 0
  for x in str(num):
    q = int(x) % 10
    print q
    total += q
    q //= 10
  return total


print digit_sum_floor_div(1234)

# REF: 
# https://python-reference.readthedocs.io/en/latest/docs/operators/floor_division.html
# https://www.geeksforgeeks.org/division-operator-in-python/

