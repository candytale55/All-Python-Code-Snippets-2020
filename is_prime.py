# function is_prime takes a number x as input.For each number n from 2 to x - 1, test if x is evenly divisible by n. 
# If it is, return False. If none of them are, then return True.

def is_prime(x):
  prime_candidate = x
  if x < 2:
    return False
  else:
    for n in range(2, x-1):
      if x % n == 0:
        return False
  return True


for i in range(0,15):
  print "Is " + str(i) + " prime?: " + str(is_prime(i))

"""
Is 0 prime?: False
Is 1 prime?: False
Is 2 prime?: True
Is 3 prime?: True
Is 4 prime?: False
Is 5 prime?: True
Is 6 prime?: False
Is 7 prime?: True
Is 8 prime?: False
Is 9 prime?: False
Is 10 prime?: False
Is 11 prime?: True
Is 12 prime?: False
Is 13 prime?: True
Is 14 prime?: False
"""



# A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. 

# Remember: all numbers less than 2 are not prime numbers

# If you want to test if a number in a variable x is prime, then no other number should go into x evenly besides 1 and x. So 2 and 5 and 11 are all prime, but 4 and 18 and 21 are not.


# https://discuss.codecademy.com/t/why-does-is-prime-fail-for-some-numbers/339345
# https://discuss.codecademy.com/t/how-to-utilize-a-loop-of-for-and-else/439096 
# https://discuss.codecademy.com/t/do-i-need-break-or-return/439101
