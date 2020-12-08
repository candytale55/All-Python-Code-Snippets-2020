"""
lots_of_math() has four parameters named a, b, c, and d. It prints 3 lines and returns 1 value.
- print the sum of a and b.
- print d subtracted from c.
- print the first number printed, multiplied by the second number printed.
- Return the third number printed modulo a.
"""

def lots_of_math(a,b,c,d):
  print(a+b)
  print(c-d)
  print((a+b) * (c-d))
  return ((a+b) * (c-d)) % a

#  TESTS:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0

print(lots_of_math(1, 1, 1, 1))
# should print 2, 0, 0, 0
