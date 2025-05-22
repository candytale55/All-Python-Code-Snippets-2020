# Class definition
class Animal(object):
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry



# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.



zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry   # Jeffrey 2 True
print giraffe.name, giraffe.age, giraffe.is_hungry   # Bruce 1 False
print panda.name, panda.age, panda.is_hungry   # Chad 7 True




"""
You can think of __init__() as the method that “boots up” a class’ instance object, short for “initialize.”

The first argument __init__() gets is used to refer to the instance object, and by convention, that argument is called self. 

If you add additional arguments—for instance, a name and age for your animal—setting each of those equal to self.name and self.age 
in the body of __init__() will make it so that when you create an instance object of your Animal class, 
you need to give each instance a name and an age, and those will be associated with the particular instance you create.
"""


# https://discuss.codecademy.com/t/why-do-we-not-pass-anything-for-self/340596
