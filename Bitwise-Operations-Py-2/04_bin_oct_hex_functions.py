"""  In order to print a number in its binary representation, you can use the bin() function. 
bin() takes an integer as input and returns the binary representation of that integer in a string. 
(Keep in mind that after using the bin function, you can no longer operate on the value like a number.) """


print bin(0) # 0b0
print bin(1) # 0b1
print bin(2) # 0b10
print bin(3) # 0b11
print bin(4) # 0b100
print bin(5) # 0b101
print bin(6) # 0b110
print bin(7) # 0b111
print bin(8) # 0b1000
print bin(9) # 0b1001
print bin(10) # 0b1010


# Loop for printing binary numbers:

for number in range (0,11):
  print bin(number)



""" You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. """

print oct(0) # 0
print oct(1) # 01
print oct(2) # 02
print oct(3) # 03
print oct(4) # 04
print oct(5) # 05
print oct(6) # 06
print oct(7) # 07
print oct(8) # 010
print oct(9) # 011
print oct(10) # 012
print oct(11) # 013
print oct(12) # 014

# Loop for printing numbers in base 8:

for number in range (0,13):
  print oct(number)



print hex(0)  # 0x0
print hex(1)  # 0x1
print hex(2)  # 0x2
print hex(3)  # 0x3
print hex(4)  # 0x4
print hex(5)  # 0x5
print hex(6)  # 0x6
print hex(7)  # 0x7
print hex(8)  # 0x8
print hex(9)  # 0x9
print hex(10)  # 0xa
print hex(11)  # 0xb
print hex(12)  # 0xc
print hex(13)  # 0xd
print hex(14)  # 0xe
print hex(15)  # 0xf
print hex(16)  # 0x10
print hex(17)  # 0x11
print hex(18)  # 0x12
print hex(19)  # 0x13
print hex(20)  # 0x14

# Loop for printing hex numbers:

for number in range (0,25):
  print hex(number)

# https://discuss.codecademy.com/t/can-i-use-a-loop-to-print-the-binary-numbers-2-through-5/340571


