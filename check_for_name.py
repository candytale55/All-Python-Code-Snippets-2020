# check_for_name() takes two strings as parameters named _sentence_ and _name_. 
# The function should return _True_ if _name_ appears in sentence in all lowercase letters, 
# all uppercase letters, or with any mix of uppercase and lowercase letters. 
# The function should return _False_ otherwise.



def check_for_name_long(sentence, name):
  result = sentence.lower().find(name.lower())
  if (result == -1): 
    return False
  else:
    return True



# Pending. Check why if you invert the conditions it doesn't work (all three tests below return True)  

def check_for_name_wrong(sentence, name):
  result = sentence.lower().find(name.lower())
  if (result >= -1): 
    return True
  else:
    return False
    
print(check_for_name_wrong("My name is Samantha", "Jamie"))
# should print False, prints True




# Improved: 
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()




#TESTS
print(check_for_name("My name is Jamie", "Jamie"))
# True
print(check_for_name("My name is jamie", "Jamie"))
# True
print(check_for_name("My name is Samantha", "Jamie"))
# False

