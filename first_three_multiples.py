 # first_three_multiples() has one parameter named num. It prints the first three multiples of num in different lines. Then, returns the third multiple.

def first_three_multiples(num):
  print (num * 1)
  print (num * 2)
  print (num * 3)
  return num * 3


# tests

third_multiple_of_ten = first_three_multiples(10)
# should print 10, 20, 30, and return 30
print(third_multiple_of_ten) # 30

first_three_multiples(0)
# should print 0, 0, 0, and return 0

first_three_multiples(7) 
# should print 7, 14, and 21 and return 21.

print(first_three_multiples(8))
# should print 8, 16, 24 and 24.

print(first_three_multiples(-5))
# should print -5, -10, -15 and -15.
