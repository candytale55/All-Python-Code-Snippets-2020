# We usually know the diameter beforehand, but what we need for most calculations is the radius. 
# Instance variable _self.radius_ is set to equal half the diameter that gets passed in.

# circumference function takes as argument, self, and returns the circumference 
# of a circle with the given radius by this formula: circumference = 2 * pi * radius


class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Assignment for self.radius:
    self.radius = diameter / 2
  def circumference(self):
      return 2 * self.pi * self.radius



# TESTS:

# A medium pizza that is 12 inches across.
medium_pizza = Circle(12)
print(medium_pizza.circumference()) # 37.68
# Your teaching table which is 36 inches across.
teaching_table = Circle(36)
print(teaching_table.circumference()) # 113.04
# The Round Room auditorium which is 11,460 inches across.
round_room = Circle(11460) # 35984.4
print(round_room.circumference())


# Since we can use dictionaries to store key-value pairs, using objects for that purpose is not really useful. 
# Instance variables are more powerful when you can guarantee a rigidity to the data the object is holding.


# This is most apparent when the constructor creates the instance variables, using the arguments passed in to it. 






class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url
 
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.secure())
# prints "https://www.codecademy.com"
 
print(wikipedia.secure())
# prints "https://www.wikipedia.org"

# Explanation:  We are creating a search engine and we want to create classes for each separate entry we could return. 
# The secure() method takes just the one required argument, self. We access both the class variable self.secure_prefix 
# and the instance variable self.url to return a secure URL.




    # REF: https://discuss.codecademy.com/t/what-are-the-differences-between-instance-variables-and-class-variables-or-why-do-i-need-to-use-self-pi/444112
    # https://discuss.codecademy.com/t/why-does-circumference-require/444204 
    # https://discuss.codecademy.com/t/when-should-i-create-a-new-method-vs-placing-it-in-init/444225
