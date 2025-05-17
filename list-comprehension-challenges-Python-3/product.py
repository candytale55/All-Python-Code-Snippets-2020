# Create a new list named product that contains the product of each sub-list of nested_lists.

nested_lists = [[4, 8], [15, 16], [23, 42]]

product = [first * second for (first,second) in nested_lists]
print (product)
# [32, 240, 966]
