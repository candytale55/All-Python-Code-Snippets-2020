# Create a new list named first_only that contains the first element in each sub-list of nested_lists.
nested_lists = [[4, 8], [16, 15], [23, 42]]

first_only = [first for (first, second) in nested_lists]
print (first_only)
# [4, 16, 23]
