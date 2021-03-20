"""
A bit mask is just a variable that aids you with bitwise operations. 
A bit mask can help you turn specific bits on, turn others off, 
or just collect data from an integer about which bits are on or off.
"""

#  we want to see if the third bit from the right is on:
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"

""" we create a mask with the third bit on.
Then, we use a bitwise-AND operation to see if the third bit from the right of num is on.
If desired is greater than zero, then the third bit of num must have been one.
"""



# function _check_bit4_ takes one argument _input_, an integer. It should check to see if the fourth bit from the right is on.

def check_bit4(input):
  mask = 0b1000
  checked = input & mask
  if checked > 1:
    return "on"
  else:
    return "off"

print check_bit4(0b1) # ==> "off"
print check_bit4(0b11011) # ==> "on"
print check_bit4(0b1010) # ==> "on"
