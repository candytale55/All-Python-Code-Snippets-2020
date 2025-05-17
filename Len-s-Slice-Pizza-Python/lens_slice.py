# You work at Len’s Slice, a new pizza joint in the neighborhood. You are going to use your knowledge of Python lists to organize some of your sales data.



# To keep track of the kinds of pizzas you sell
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# To keep track of how much each kind of pizza slice costs.
prices = [2, 6, 1, 3, 2, 7, 2]



# Find the length of the toppings list and store it in a variable called num_pizzas
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas)+ " different kinds of pizza!") # We sell 7 different kinds of pizza!


# Use zip to combine the two lists into a list called pizzas

pizzas = list(zip(prices, toppings))
print(pizzas)
# [(2, 'pepperoni'), (6, 'pineapple'), (1, 'cheese'), (3, 'sausage'), (2, 'olives'), (7, 'anchovies'), (2, 'mushrooms')]



## Sorting and Slicing Pizzas
pizzas.sort()
print(pizzas)
# [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]

cheapest_pizza = pizzas[0]
print(cheapest_pizza)

#A man in a business suit walks in and shouts “I will have your MOST EXPENSIVE pizza!”
priciest_pizza = pizzas[-1]
print(priciest_pizza)



# Three mice walk into the store. They don’t have much money (they’re mice), but they do each want different pizzas.

# The 3 lowest cost pizzas: To get the first n items of a list, use [:n].  
three_cheapest = pizzas[0:3]
print(three_cheapest)


# Count the number of occurrences of 2 in the prices list
num_two_dollar_slices= prices.count(2)
print(num_two_dollar_slices) # 3

# Walkthrough: https://www.youtube.com/watch?v=CINEiX_Y0K8
