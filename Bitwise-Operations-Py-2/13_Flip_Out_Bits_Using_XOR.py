"""
Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

To flip all of the bits in a :

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
"""


# Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped.
a = 0b11101110
mask = 0b11111111

print bin(a ^ mask) # 0b10001
