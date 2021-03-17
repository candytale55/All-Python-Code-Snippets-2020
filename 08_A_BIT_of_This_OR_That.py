"""
The bitwise OR (|) operator compares two numbers on a bit level and returns a number 
where the bits of that number are turned ON if either of the corresponding bits of either number are 1. 

0 | 0 = 0
0 | 1 = 1 
1 | 0 = 1
1 | 1 = 1

For example:

    a:  00101010  42
    b:  00001111  15       
================
a | b:  00101111  47

The bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.


Meaning:
110 (6) | 1010 (10) = 1110 (14)
"""

print 0b1110 | 0b101        # 15
print bin(0b1110 | 0b101)   # 0b1111

# https://discuss.codecademy.com/t/why-is-my-output-of-bitwise-or-not-correct/340568
