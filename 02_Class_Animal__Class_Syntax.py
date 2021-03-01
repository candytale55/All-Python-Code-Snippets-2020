# A basic class consists only of the class keyword, the name of the class, and the class from which the new class inherits in parentheses.  
# For now, our classes will inherit from the _object_ class. 

# This gives them the powers and abilities of a Python object. By convention, user-defined Python class names start with a capital letter.


class NewClass(object):
  # Class magic here
  pass

# pass doesn’t do anything, but it’s useful as a placeholder in areas of your code where Python expects an expression.



# __init__()
#  we start our class definition off with an odd-looking function: __init__(), required for classes, and it’s used to initialize the objects it creates. 

# __init__() always takes at least one argument, self, that refers to the object being created. You can think of __init__() as the function that “boots up” each object the class creates.


class Animal(object):
  def __init__(self, name):
    self.name = name  #  let the function know that name refers to the created object’s name by typing self.name = name


"""
 Python will use the first parameter that __init__() receives to refer to the object being created; 
 this is why it’s often called self, since this parameter gives the object being created its identity. 
 This is a Python convention; there’s nothing magic about the word self but it’s overwhelmingly common 
 to use self as the first parameter in __init__(), so you should use this so that other people will understand your code.
"""

# https://discuss.codecademy.com/t/what-does-it-mean-to-inherit-from-the-object-class/340587
# https://discuss.codecademy.com/t/what-is-the-difference-between-a-class-and-an-object/340593
# https://discuss.codecademy.com/t/what-is-self/340594
