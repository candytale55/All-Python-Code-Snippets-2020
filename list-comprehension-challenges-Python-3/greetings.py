# Create a new list named greetings that adds "Hello, " in front of each name in the list names.

names = ["Elaine", "George", "Jerry", "Cosmo"]

greetings = ["Hello, " + x for x in names]
print(greetings)
# ['Hello, Elaine', 'Hello, George', 'Hello, Jerry', 'Hello, Cosmo']
