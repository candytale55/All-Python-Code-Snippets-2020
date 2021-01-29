# Create a new list named opposite that contains the opposite boolean for each element in the list booleans.
booleans = [True, False, True]
print(booleans)

opposite = [not x for x in booleans]
print (opposite)
# [False, True, False]
