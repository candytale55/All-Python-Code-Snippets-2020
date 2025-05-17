# Every time we create an instance of Shouter the program prints out a shout. 
# When we created each of our objects we passed an argument to the constructor. 
" The constructor takes the argument phrase and, if it’s a string, prints out the all-caps version of phrase.

class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:
 
      # then shout it out
      print(phrase.upper())
 
shout1 = Shouter("shout")
# prints "SHOUT"
 
shout2 = Shouter("shout")
# prints "SHOUT"
 
shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"


# There are several methods that we can define in a Python class that have special behavior = dunder methods. 
# Dunder methods are so-named because they have two underscores (double-underscore abbreviated to “dunder”) on either side of them.

  # There are several methods that we can define in a Python class that have special behavior. 
  # These methods are sometimes called “magic,” because they behave differently from regular methods. 
  # Another popular term is _dunder methods_, so-named because they have two underscores 
  # (double-underscore abbreviated to “dunder”) on either side of them.

  # The __init__() method (note the two underscores before and after the word “init”) 
  # is a dunder method is used to initialize a newly created object. 
  # It is called every time the class is instantiated.

  # Methods that are used to prepare an object being instantiated are called constructors. 
  # The word “constructor” is used to describe similar features in other object-oriented programming 
  # languages but programmers who refer to a constructor in Python are usually talking about the __init__() method.




class Circle:
  pi = 3.14
  # constructor:
  def __init__(self, diameter):
    print("New circle with diameter: {}".format(diameter))

teaching_table = Circle(36)



#REF: https://discuss.codecademy.com/t/what-is-the-difference-between-calling-a-variable-with-self-or-the-classname/464689
# https://discuss.codecademy.com/t/what-does-instantiate-mean-in-the-context-of-this-lesson/465216
