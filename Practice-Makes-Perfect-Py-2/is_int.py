# function is_int takes a number x as an input. It returns True if the number is an integer and False otherwise. 
# For the purpose of this lesson, we’ll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.


import math

def is_int(x):
  return True if math.floor(x) - x == 0 else False


print is_int(7.0)   # True    
print is_int(7.5)   # False    
print is_int(-1)    # True








# An integer is a number without a decimal part (for instance, -17, 0, and 42 are all integers, but 98.6 is not). 
# However, for the purpose of this lesson, we’ll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.

# This means that, for this lesson, you can’t just test the input to see if it’s of type int. 
# To solve it: If the difference between a number and that same number rounded is greater than zero.



# REFS:
# https://discuss.codecademy.com/t/how-can-i-test-if-a-number-is-an-integer-without-using-type/339339
