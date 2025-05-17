# Create a new list named greater_than that contains True if the first number in the sub-list is greater than the second number in the sub-list, and False otherwise.

nested_lists = [[4, 8], [16, 15], [23, 42]]

greater_than = [first > second for (first, second) in nested_lists]
print (greater_than)
# [False, True, False]
