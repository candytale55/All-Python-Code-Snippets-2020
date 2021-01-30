# long_string takes an input str and returns True if the string has over 12 characters in it. Otherwise, return False.

long_string = lambda string : len(string) > 12 

print long_string("short")          # False
print long_string("photosynthesis") # True
