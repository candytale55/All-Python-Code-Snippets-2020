# use a for loop on a dictionary to loop through its keys with the following code:

# A simple dictionary
d = {"foo" : "bar", "kate":"soap"}
 
for key in d: 
  print d[key]  

# prints: 
"""
bar
soap
"""

# dictionaries are unordered, meaning that any time you loop through a dictionary, 
# you will go through every key, but you are not guaranteed to get them in any particular order.

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Use a for loop to go through the webster dictionary and print out all of the definitions.
for key in webster:
  print webster[key]

# Prints:
"""
A star of a popular children's cartoon show.
Goes on the floor.
A small amount.
The sound a goat makes.
"""
