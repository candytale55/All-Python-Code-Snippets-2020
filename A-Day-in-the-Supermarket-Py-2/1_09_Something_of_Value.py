# For paperwork and accounting purposes, let’s record the total value of your inventory. It’s nice to know what we’re worth

prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}


# Inventory
for key in prices:
  print " "
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]


print " "


# The value of any given product is its number of items in stock multiplied by its price. 
# For instance, the total cost for bananas would be 24 (a price of 4 multiplied by 6 bananas in stock).


# determine how much money you would make if you sold all of your food with a for loop.  
# For each key in prices, multiply the number in prices by the number in stock. 
# Print that value into the console and then add it to total.

print "Inventory Value:"
total = 0
for key in prices:
  total += prices[key] * stock[key]
  print total
print "total: " + str(total)
