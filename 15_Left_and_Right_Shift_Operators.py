"""
You can use the left shift (<<) and right shift (>>) operators to slide masks into place.
If you want to turn ON the 10th bit from the right of the integer a, 
instead of writing out the entire number, we slide a bit over using the << operator.

We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.
"""

a = 0b101 
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten 
desired = a ^ mask
print bin(desired) # 0b1000000101



"""
function flip_bit takes the inputs (number, n). 
It flips the nth bit (with the ones bit being the first bit = 0b1) 
and store in variable result. It returns result of calling bin(result)

The mask should be created by shifting a 1 left by n - 1 digits. If we shift by n, 
that is one too many, because 1 starts off in the first position.

"""

def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

print flip_bit(a, 10)  # 0b1000000101



def flip_bit_one_line(number, n):
  return bin( number ^ (0b1 << (n-1)))

print flip_bit_one_line(a, 10)  #  0b1000000101


# https://discuss.codecademy.com/t/why-does-my-flip-bit-function-return-the-wrong-number/340585
