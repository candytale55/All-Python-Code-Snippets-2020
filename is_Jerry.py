# Create a new list called is_Jerry, in which an entry at position i is True if the entry in names at position i equals "Jerry". 
# The entry should be False otherwise. Use string comparison using ==.

names = ["Elaine", "George", "Jerry", "Cosmo"]

is_Jerry = [x == "Jerry" for x in names]
print (is_Jerry)
# [False, False, True, False]
