# Python 2

"""
The int function an optional second parameter. 
When given a string containing a number and the base that number is in, 
the function will return the value of that number converted to base ten.

int("110", 2)
# ==> 6

"""

print int("1",2)      # 1   
print int("10",2)     # 2
print int("111",2)    # 7
print int("0b100",2)  # 4
print int(bin(5),2)   # 5
# Print out the decimal equivalent of the binary 11001001.
print int("11001001", 2)  # 201



# https://discuss.codecademy.com/t/why-does-my-code-not-print-the-base-10-equivalent-of-the-binary-string/340564
