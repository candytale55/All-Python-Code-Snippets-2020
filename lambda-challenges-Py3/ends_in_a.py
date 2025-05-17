# named ends_in_a takes an input str and returns True if the last character in the string is an a. Otherwise, return False.

ends_in_a = lambda string : string[len(string)-1] == "a"

print ends_in_a("data")      # True
print ends_in_a("aardvark")  # False
