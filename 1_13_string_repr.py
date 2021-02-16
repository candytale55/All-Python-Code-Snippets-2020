# One of the first things we learn as programmers is how to print out information that we need for debugging. 
# When we print out an object we get a default representation that seems fairly useless.

class Employee1():
  def __init__(self, name):
    self.name = name
 
argus = Employee1("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>" 
# This tell us where the class is defined and our computer’s memory address where this object is stored, but no useful information for debugging our code.





# dunder method __repr__() can be used to tell Python what we want the string representation of the class to be. 
# __repr__() can only have one parameter, self, and must return a string.

class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name 
    # it returns the .name attribute of the object
 
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"





class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {}".format(self.radius)
  
medium_pizza = Circle(12)
print(medium_pizza)
#Circle with radius 6.0

teaching_table = Circle(36)
print(teaching_table)
# Circle with radius 18.0

round_room = Circle(11460)
print(round_room)
# Circle with radius 5730.0

# REF: https://discuss.codecademy.com/t/does-the-repr-method-need-to-provide-all-the-attributes-of-an-object/359654
# https://discuss.codecademy.com/t/what-is-the-use-of-repr/465233
