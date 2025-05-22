# dictionaries, once and twice have the same keys, so we can loop through one dictionary and print values from both once and twice.

once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
  print "Once: %s" % once[key]
  print "Twice: %s" % twice[key]

# Prints:
"""
Once: 1
Twice: 2
Once: 2
Twice: 4
"""

print ""
print ""



prices = {
 "banana": 4, 
 "apple": 2, 
 "orange": 1.5, 
 "pear": 3 
}

stock = {
  "banana": 6, 
  "apple": 0, 
  "orange": 32, 
  "pear": 15
}


#  print out the key along with its price and stock information. 
# Because you know that the prices and stock dictionary have the same keys, 
# you can access the stock dictionary while you are looping through prices.



for food in prices:
  print ""
  print food
  print "price: %s" % prices[food]
  print "stock: %s" % stock[food]
