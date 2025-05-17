# Function remainder() with two parameters named num1 and num2.
# returns the remainder of twice num1 divided by half of num2.


def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0
