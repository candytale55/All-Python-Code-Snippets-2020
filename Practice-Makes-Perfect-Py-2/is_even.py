# function is_even takes a number x as input. If x is even, then return True. Otherwise, return False.

def is_even(number):
  if number % 2 == 0:
    return True
  else:
    return False

print is_even(7) # False
print is_even(8) # True



def is_even_ternary(number):
  return True if number % 2 == 0 else False

print is_even_ternary(100) # True
print is_even_ternary(41)  # False



# https://discuss.codecademy.com/t/how-do-i-use-the-operator/339337
# https://book.pythontips.com/en/latest/ternary_operators.html
