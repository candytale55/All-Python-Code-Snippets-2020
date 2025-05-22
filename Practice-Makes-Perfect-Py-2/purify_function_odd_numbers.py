# function _purify_ takes in a list of numbers. It removes all odd numbers in the list, 
# and returns the result without modifying the original list. For example, purify([1,2,3]) should return [2].


def purify(numbers):
  purified_numbers = []
  for item in numbers:
    if item % 2 == 0:
      purified_numbers.append(item)
  return purified_numbers

print purify([1,2,3])  # [2]

print purify([1,2,3,33,2,12,45,90,91])
# [2, 2, 12, 90]
