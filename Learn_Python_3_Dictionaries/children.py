
# We can have a list or a dictionary as a value  in a dictionary, but these can't be keys If we try to, we'll get a TypeError. 
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# TypeError: unhashable type: 'list'

# unhashable” in this context means that the list is an object that can be changed.
# Dictionaries rely on each key having a hash value = specific identifier for the key. 
# If the key can change, that hash value would not be reliable. 

# Keys must always be unchangeable, hashable data types, like numbers or strings.

children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

print(children)
print(children["von Trapp"])
print(children["Corleone"])


# REF: https://discuss.codecademy.com/t/can-a-tuple-be-used-as-a-dictionary-key/352837
