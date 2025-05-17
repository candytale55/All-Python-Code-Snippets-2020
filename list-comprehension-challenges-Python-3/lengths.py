# Create a new list named lengths that contains the size of each name in the list of names (using len())

names = ["Elaine", "George", "Jerry", "Cosmo"]

lengths = [len(x) for x in names]
print (lengths)
# [6, 6, 5, 5]
