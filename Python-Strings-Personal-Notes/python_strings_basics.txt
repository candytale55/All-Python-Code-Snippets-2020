# len() gets the length (the number of characters) of a string!

parrot = "Norwegian Blue"
print len(parrot) # 14


# lower() gets rid of all the capitalization in your strings.
parrot = "Norwegian Blue"
print parrot.lower() # norwegian blue


# upper() makes a string completely upper case.
parrot = "norwegian blue"
print parrot.upper() # NORWEGIAN BLUE


# str() method turns non-strings into string
pi = 3.14
print str(pi) # 3.14


# Methods that use dot notation only work with strings. On the other hand, len() and str() can work on other data types.

ministry = "The Ministry of Silly Walks"

print len(ministry) # 27
print ministry.upper() # THE MINISTRY OF SILLY WALKS


# Turn 3.14 into a string on line 3!


print "The value of pi is around " + str(3.14)

# Sometimes you need to combine a string with something that isn’t a string. In order to do that, you have to convert the non-string into a string with str().

