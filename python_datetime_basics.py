from datetime import datetime
now = datetime.now()


# use function datetime.now() to retrieve the current date and time.
now = datetime.now()
print now  # 2020-11-27 16:12:26.951093

# print year, month and day separatedly
print now.year  # 2020
print now.month # 11
print now.day   # 27

# The code %B tells strftime() that we want to display the month as its full name.  Check: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
print(now.strftime('%B'))  # November

# Display date in mm/dd/yyyy format using string substitution.  The standalone % operator after the string will fill the %02d and %04d placeholders 
print '%02d/%02d/%04d' % (now.month, now.day, now.year)  # 11/27/2020

# Display date in mm-dd-yyyy
print '%02d-%02d-%04d' % (now.month, now.day, now.year)  # 11-27-2020

# Hour, minute, second in format hh:mm:ss
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second) # 16:12:26

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second) # 11/27/2020 16:12:26

print '%02d-%02d-%04d' % (now.month, now.day, now.year)

# Hour, minute, second: 
print '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

# Print the date and time together in the form: mm/dd/yyyy hh:mm:ss
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second)  # 11/27/2020 16:12:26
