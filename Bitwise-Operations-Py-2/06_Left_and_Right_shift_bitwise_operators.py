"""
The left and right shift bitwise operators work by shifting the bits of a number over by a designated number of slots.

The shift is always a positive integer:

# Left Bit Shift (<<)  
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)       
 
# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0) 


Shift operations are similar to rounding down after dividing and multiplying by 2 (respectively) 
for every time you shift, but it’s often easier just to think of it as shifting 
all the 1s and 0s left or right by the specified number of slots.

Note: You can only do bitwise operations on an integer. 
Trying to do them on strings or floats will result in nonsensical output.
"""


#  shift_right to the right twice 
shift_right  = 0b1100
shift_left  = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right) # 0b11
print bin(shift_left ) # 0b100
print bin(shift_right >> 3) # 0b0
print bin(shift_left << 3) # 0b100000


# https://discuss.codecademy.com/t/how-does-bit-shifting-work/340566
