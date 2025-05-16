# You’re a programmer working for an organization that is trying to digitize and store poetry called Preserve the Verse.

# You’ve been given two strings, the title of a poem and it’s author, and have been asked 
# to reformat them slightly to fit the conventions of the organization’s database.

poem_title = "spring storm"
poem_author = "William Carlos Williams"

#.title() returns the string in title case, which means the first letter of each word is capitalized.
poem_title_fixed = poem_title.title()
print(poem_title) #  spring storm
print(poem_title_fixed) # Spring Storm


# The organization’s database also needs the author’s name to be uppercase only.
#.upper() returns the string with all uppercase characters.

poem_author_fixed = poem_author.upper()
print(poem_author) # William Carlos Williams
print(poem_author_fixed) # WILLIAM CARLOS WILLIAMS



#.lower() returns the string with all lowercase characters.


# It’s important to remember that string methods can only create new strings, they do not change the original string.
