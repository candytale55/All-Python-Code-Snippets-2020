# function digit_sum takes a positive integer n as input and returns the sum of all that number’s digits. 
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)



# 1st Failed attempt:
"""
def digit_sum(n):
  num_sum = 0
  for digit in n: 
    num_sum += digit
  return num_sum


print digit_sum(1234)
"""

# Traceback error:
"""
Traceback (most recent call last):
  File "python", line 10, in <module>
  File "python", line 5, in digit_sum
TypeError: 'int' object is not iterable
"""




# Solution: convert the integer to a string with str(), iterate over it, and turn the substrings back into integers with int() to do the addition.


def digit_sum(n):
  num_sum = 0
  for digit in str(n): 
    num_sum += int(digit)
  return num_sum


print digit_sum(1234) # 10



#REF:
# https://discuss.codecademy.com/t/how-can-i-break-down-these-problems-into-easier-parts/339340
