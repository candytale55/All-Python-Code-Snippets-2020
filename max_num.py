# max_num() has three parameters named num1, num2, and num3. 
# The function should return the largest of these three numbers.  
# If any of two numbers tie as the largest, you should return "It's a tie!".


def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  elif num2 > num1 and num2 > num3:
    return num2
  elif num3 > num2 and num3 > num1:
    return num3
  elif num1 == num2 or num1 == num3 or num2 == num3:
    return  "It's a tie!"
  else:
    return "Check your numbers, there was an error"


# Tests
print(max_num(-10, 0, 10))
# should print 10
print(max_num(-10, 5, -30))
# should print 5
print(max_num(-5, -10, -10))
# should print -5
print(max_num(2, 3, 3))
# should print "It's a tie!"
