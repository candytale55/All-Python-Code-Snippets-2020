# The dir() function can be used to investigate an object’s attributes at runtime. 
# dir() is short for directory and offers an organized presentation of object attributes.

# Attributes can be added to user-defined objects after instantiation, 
# so it’s possible for an object to have some attributes that are not explicitly defined in an object’s constructor. 

# Python automatically adds a number of attributes that are usually indicated by double-underscores. 
# But dir() also list your attributes



print("int 5: ")
print(dir(5))
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']





print("")

def this_function_is_an_object(string):
  return string.upper()


print(this_function_is_an_object("Hurraaa"))

print(dir(this_function_is_an_object))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



print("")
print("Examine: ")


# you can use dir() to examine a class in addition to calling it on an object of a class. 
# In the following code example, you can see that the dir() call on the object 
# of class Examine shows the instance variable created in the object while the call for the class does not.

class Examine:
    class_var = "This is a class variable"
    def __init__(self):
        self.inst_var = "This is an instance variable"

myobj = Examine()

print(dir(Examine))
# OUTPUTS: ['__doc__', '__init__', '__module__', 'class_var']

print(dir(myobj))
# OUTPUTS: ['__doc__', '__init__', '__module__', 'class_var', 'inst_var']



print("")
print("fake_dict: ")


class FakeDict:
  pass
 
fake_dict = FakeDict()
fake_dict.attribute = "Cool"
 
print(dir(fake_dict))
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']

# You are able to use type() on Python’s native data types because they are also objects in Python. 
# Their classes are int, float, str, list, and dict. 
# These Python classes have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically, 
# but these instances are still full-blown objects to Python.

print("")
print("fun_list: ")

fun_list = [10, "string", {'abc': True}]
 
type(fun_list)
# Prints <class 'list'>
 
print(dir(fun_list))
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']




