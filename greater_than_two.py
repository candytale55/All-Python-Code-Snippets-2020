# Create a new list called greater_than_two, in which an entry at position i is True if the entry in nums at position i is greater than 2.

nums = [5, -10, 40, 20, 0]

greater_than_two = [x > 2 for x in nums]
print (greater_than_two)
# [True, False, True, True, False]
