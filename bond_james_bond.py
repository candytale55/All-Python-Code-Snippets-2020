# introduction(first_name, last_name) 
# takes two parameters and should return the last_name, followed by a comma, a space, first_name, another space, and finally last_name.
# Like "Bond, James Bond".

def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

# Tests:
print(introduction("James", "Bond"))
# should print Bond, James Bond

print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou
