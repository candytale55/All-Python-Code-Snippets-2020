# When a class has its own functions, those functions are called methods. 
# method _description_ using print statements, prints out the name and age of the animal it’s called on.

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def description(self):
    print self.name
    print self.age

# self must be an argument to the description method. Otherwise, printing self.name and self.age won’t work, 
# since Python won’t know which self (that is, which object) you’re talking about


hippo = Animal("hippy", 2)

hippo.description()
