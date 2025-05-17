
# The really easy way.

# always_false has one parameter named num. Using an if statement, 
# the num variable num and operators the function will return False
# no matter what number is stored in num.


def always_false(num):
  if num > num:
    return True
  elif num < num:
    return True
  elif num != num:
    return True
  elif num ** 2 < num:
    return True
  elif num/1 > num:
    return True
  else: 
    return False


# tests
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False
