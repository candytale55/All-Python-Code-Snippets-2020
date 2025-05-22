# We’ve defined our own class, Fruit, and created a lemon instance.

class Fruit(object):
  """A class that makes various tasty fruits."""
  def __init__(self, name, color, flavor, poisonous):
    self.name = name
    self.color = color
    self.flavor = flavor
    self.poisonous = poisonous

  def description(self):
    print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

  def is_edible(self):
    if not self.poisonous:
      print "Yep! I'm edible."
    else:
      print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
# I'm a yellow lemon and I taste sour.

lemon.is_edible()
# Yep! I'm edible.


print dir(lemon)
# ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'color', 'description', 'flavor', 'is_edible', 'name', 'poisonous']


"""
  You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its methods.

len("Eric")
my_dict.items()

 Python checks to see if my_dict has an items() method (which all dictionaries have) and executes that method if it finds it.

 What makes "Eric" a string and my_dict a dictionary is that they’re instances of the str and dict classes, respectively. 
 
   A class is a way of organizing and producing objects with similar attributes and methods.
"""
