"""
The bitwise AND (&) operator compares two numbers on a bit level and returns a number 
where the bits of that number are turned on if the corresponding bits of both numbers are 1. 

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1

For example:

     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10

Using the & operator can only result in a number that is less than or equal to the smaller of the two values.
"""

print 0b111 & 0b1010        # 2
print bin(0b111 & 0b1010)   # 0b10
print int(0b10)  # 2  
#  0b111 (7) & 0b1010 (10) = 0b10 (4)


print 0b1110 & 0b101         # 4
print bin(0b1110 & 0b101)    # 0b100



# https://discuss.codecademy.com/t/what-if-i-want-to-compare-bit-strings-of-uneven-length/340567


"""
If you want to compare bit strings of uneven length, the leftmost unfilled bits will be considered zeros.

For example strings 1001 and 1001 1010 would work like this:

  0000 1001
& 1001 1010
-------------
  0000 1000
"""

print (0b1001 & 0b10011010)     # 8
print bin(0b1001 & 0b10011010)  # 0b1000
