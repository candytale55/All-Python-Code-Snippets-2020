# One way that we can introduce polymorphism to class definitions is by using dunder methods.



# The Atom  .__add__(self, other) method returns a Molecule with the two Atoms together in a list.


class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self, other):
    return Molecule([self, other])

class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
      
sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
# salt = sodium + chlorine




# We can define define dunder methods that define a custom-made class to look and behave like a Python builtin. 


# REF: https://discuss.codecademy.com/t/does-add-for-a-class-have-to-return-a-different-class/361580
# https://discuss.codecademy.com/t/how-can-i-use-string-representation-to-print-the-combined-molecule/467579






class Color:
  def __init__(self, red, green, blue):
    self.red = red
    self.green = green
    self.blue = blue
 
  def __repr__(self):
    return "Color with RGB = ({red}, {green}, {blue})".format(red=self.red, green=self.green, blue=self.blue)
 
  def add(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color(new_red, new_green, new_blue)
 
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
 
magenta = red.add(blue)
print(magenta)
# Prints "Color with RGB = (255, 0, 255)"


# We defined a Color class that implements an addition function. 
# Unfortunately, red.add(blue) is a little verbose for something that we have an intuitive symbol 
# for (i.e., the + symbol). Well, Python offers the dunder method __add__ for this very reason





class Color: 
  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color(new_red, new_green, new_blue)


# red.add(blue) is a little verbose for something that we have an intuitive symbol for (i.e., the + symbol). 
# Well, Python offers the dunder method __add__

class Color2: 
  def __add__(self, other):
    """
    Adds two RGB colors together
    Maximum value is 255
    """
    new_red = min(self.red + other.red, 255)
    new_green = min(self.green + other.green, 255)
    new_blue = min(self.blue + other.blue, 255)
 
    return Color2(new_red, new_green, new_blue)

