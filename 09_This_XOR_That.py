"""
The XOR (^) "exclusive or" operator compares two numbers on a bit level and 
returns a number where the bits of that number are turned on 
if either of the corresponding bits of the two numbers are 1, but not both.

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0

Therefore:
    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37

If a bit is off in both numbers, it stays off in the result. 

XOR-ing a number with itself will always result in 0.


 111 (7) ^ 1010 (10) = 1101 (13)
"""

print 0b1110 ^ 0b101      # 11
print bin(0b1110 ^ 0b101) # 0b1011



# https://discuss.codecademy.com/t/how-can-i-xor-two-numbers-without-using-the-operator/340576

"""
For bit strings of different lengths, simply write out the numbers and fill in the leftmost missing bits with 0s. For example:
0b10011001 ^ 0b1111
We’d write that out as follows:

  1001 1001
^ 0000 1111
-------------
  1001 0110
"""
