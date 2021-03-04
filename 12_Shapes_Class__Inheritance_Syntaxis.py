"""
In Python, inheritance works like this:

class DerivedClass(BaseClass):
  # code goes here

where DerivedClass is the new class you’re making and BaseClass is the class from which that new class inherits.
"""


class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# class Triangle inherits from Shape
class Triangle(Shape):
  def __init__(self, side1, side2, side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3


# https://discuss.codecademy.com/t/how-will-triangle-objects-know-which-init-method-to-use/340794
"""
Python is smart enough to see that we intended to use the initialize method in our Triangle class when creating a new Triangle object.
Python checks the object that called the method and sees that it has a method of the same name that then takes priority over the one in the base class.
In the case of __init__() being defined twice, it sees that we’re initializing a Triangle, so we use that method.
"""
