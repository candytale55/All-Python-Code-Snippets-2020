# random.choice() takes a list as an argument and returns a number from the list

# random.randint() takes two numbers as arguments and generates a random number between the two numbers you passed in


import random

# Create random_list:  generate a random integer between 1 and 100 (inclusive) for each number in range(101).
random_list = [random.randint(1,101) for i in range(101)]
print (random_list)

# Create randomer_number: randomer_number and set it equal to random.choice() with random_list as an argument.
randomer_number = random.choice(random_list)
print (randomer_number)
