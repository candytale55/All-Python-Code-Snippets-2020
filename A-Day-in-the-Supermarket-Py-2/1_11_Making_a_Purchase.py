# Shopping at the Market
# In order for customers to order online, we are going to have to make a consumer interface.

#REF: https://discuss.codecademy.com/t/why-does-it-say-groceries-is-not-a-list/339210
# https://discuss.codecademy.com/t/why-is-compute-bill-returning-the-wrong-value/339212


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




shopping_list = ["banana", "orange", "apple"]

# Function _compute_bill_ takes one argument _food_ (list) as input. 
# Variable _total_ with initial value of zero is used as counter. 
# For each item in the food list, add the price of that item to total. Finally, return the total.

def compute_bill (food):
  total = 0
  for item in food:
    total += prices[item]
  return total 

# Right now it ignores whether or not the item is in stock.

print(compute_bill(shopping_list))
