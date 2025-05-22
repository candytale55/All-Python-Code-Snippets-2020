"""
Use masks to turn a bit in a number on using |. This is to make sure the rightmost bit of a number is turned on:
"""

a = 0b10111011
mask = 0b100
print bin(a | mask) # 0b10111111
print (a | mask)    # 191

mask = 0b1000100
print bin(a | mask) # 0b11111111
print (a | mask)    # 255

