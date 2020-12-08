# function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False

def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False

# Tests in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False
