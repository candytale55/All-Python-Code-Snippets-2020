# Shopping at the Market
# In order for customers to order online, we are going to have to make a consumer interface.

# Function _compute_bill_ takes one argument _food_ as input. 
# Variable _total_ with initial value of zero is used as counter. 
# For each item in the food list, add the price of that item to total.  

# if an item isn’t in stock, then it shouldn’t be included in the total. 
# You can’t buy or sell what you don’t have! 
# Funciton only adds the price of the item to total if the item’s stock count is greater than zero. 

# if the item is in stock and after you add the price to the total, subtract one from the item’s stock count.

# Finally, returns the total.


#REF: https://discuss.codecademy.com/t/why-does-it-say-groceries-is-not-a-list/339210
# https://discuss.codecademy.com/t/why-is-compute-bill-returning-the-wrong-value/339212



shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

# Write your code below!
def compute_bill(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

print(compute_bill(shopping_list)) # 5.5
print (stock) 
# {'orange': 31, 'pear': 15, 'banana': 5, 'apple': 0}
