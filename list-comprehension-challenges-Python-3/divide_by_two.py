# Python 3
# Create a new list named divide_by_two that contains half of every element in the list nums. Make sure to divide by 2, not 2.0.

nums = [4, 8, 15, 16, 23, 42]
print (nums)
# [4, 8, 15, 16, 23, 42]

divide_by_two = [int(x / 2) for x in nums]
print(divide_by_two)
# [2, 4, 7, 8, 11, 21]
