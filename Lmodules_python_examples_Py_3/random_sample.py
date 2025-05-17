

# random.sample() takes a range and a number as its arguments. It will return the specified number of random numbers from that range.

import codecademylib3_seaborn
from matplotlib import pyplot as plt
import random

numbers_a = range(1,13)
# range of numbers 1 through 12 (inclusive).
print(numbers_a)

numbers_b = random.sample(range(1000),12)
# a random sample of twelve numbers within range(1000).
print(numbers_b)

#  plot these number sets against each other using plt. Call plt.plot() with your two variables as its arguments.
plt.plot(numbers_a, numbers_b)
plt.show()





# When we want to invoke the randint() function we call random.randint(). This is default behavior where Python offers a namespace for the module. 

# A namespace isolates the functions, classes, and variables defined in the module from the code in the file doing the importing. Your local namespace, meanwhile, is where your code is run.

# Python defaults to naming the namespace after the module being imported, but sometimes this name could be ambiguous or lengthy. Sometimes, the module’s name could also conflict with an object you have defined within your local namespace.

# this name can be altered by aliasing using the as keyword:

# _import module_name as name_you_pick_for_the_module_

# You usually use aliases if the name of the library is long and typing it every time you want to use one of its functions takes a lot of time.

# import * where the * ,known as a “wildcard”, matches anything and everything in the library. This syntax is considered dangerous because it could _pollute_ the local namespace. 

# Pollution occurs when the same name could apply to two possible things. For example, you have a function floor() for floor tiles, and using _from math import *_  you also import a function floor() that rounds down floats


# https://discuss.codecademy.com/t/what-happens-if-i-import-an-module-or-function-that-conflicts-with-an-object-defined-in-my-local-namespace/374440
# https://discuss.codecademy.com/t/what-is-the-codecademylib3-seaborn-module/461312
