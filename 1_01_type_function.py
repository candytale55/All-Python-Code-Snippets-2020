# Python equips us with many different ways to store data. Float is a different kind of number from an int, 
# and we store different data in a list than we do in a dict. These are known as different types. 
# We can check the type of a Python variable using the type() function.

# A variable’s type determines what you can do with it and how you can use it. 
# You can’t .get() something from an integer, just as you can’t add two dictionaries together using +. 
# This is because those operations are defined at the type level.


a_string = "Cool String"
an_int = 12
 
print(type(a_string))
# prints "<class 'str'>"
 
print(type(an_int))
# prints "<class 'int'>"

print(type(5))
# prints "<class 'int'>"

print(type({'name': 'A dictionary'}))
# <class 'dict'>

my_dict = {}
print(type(my_dict))
# <class 'dict'>

my_list = []
print(type(my_list))
# <class 'list'>


class TestClass:
    def __init__(self):
        self.value = 0

    def getVal(self):
        return self.value

my_class = TestClass()
print(type(my_class))
# <class '__main__.TestClass'>
