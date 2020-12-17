
# .replace(). takes two arguments and replaces all instances of the first argument in a string with the second argument.

toomer_bio = "Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands."

# change all instances of Tomer in the bio to Toomer.

toomer_bio_fixed = toomer_bio.replace("Tomer", "Toomer")
print(toomer_bio_fixed)
# Nathan Pinchback Toomer, who adopted the name Jean Toomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Toomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Toomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.


# .find() takes a string as an argument and searching the string it was run on for that string. 
# It then returns the first index value where that string is located.

god_wills_it_line_one = "The very earth will disown you"

# At what index place does the word “disown” appear?

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

# https://www.poetryfoundation.org/poetrymagazine/browse?contentId=23104

# You can also search for larger strings, and .find() will return the index value of the first character of that string. 
