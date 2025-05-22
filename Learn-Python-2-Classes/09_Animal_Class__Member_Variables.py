

class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = "good"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def description(self):
    print self.name
    print self.age



hippo = Animal("hippy", 2)
sloth = Animal("Rush", 4)
ocelot = Animal("Pamela", 3)

print hippo.health
print sloth.health
print ocelot.health





lion = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
lion.is_alive = False
print lion.is_alive
print cat.is_alive

"""
In the example above, we create two instances of an Animal.
Then we print out True, the default value stored in hippo’s is_alive member variable.
Next, we set that to False and print it out to make sure.
Finally, we print out True, the value stored in cat’s is_alive member variable. We only changed the variable in hippo, not in cat.
"""


# https://discuss.codecademy.com/t/member-variables-over-instance-variables/352522/6
