# .split() takes one argument (delimiter) and returns a list of substrings found between the given argument ). 
# The following syntax should be used:  string_name.split(delimiter).  
# If you do not provide an argument for .split() it will default to splitting at spaces.


line_one = "The sky has given over"

# create a list called line_one_words that contains each word in this line of poetry.
line_one_words = line_one.split()
print(line_one_words)
# ['The', 'sky', 'has', 'given', 'over']


# If we provide an argument for .split() we can dictate the character we want our string to be split on. 
# This argument should be provided as a string itself.


# create a list called author_names containing each individual author name as it’s own string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)  
# ['Audre Lorde', 'Gabriela Mistral', 'Jean Toomer', 'An Qi', 'Walt Whitman', 'Shel Silverstein', 'Carmen Boullosa', 'Kamala Suraiyya', 'Langston Hughes', 'Adrienne Rich', 'Nikki Giovanni']


# now it turns out they didn’t want poet’s first names
# There are several ways to do this, but one way is to iterate through the list
# and use .split(), negative indexing, and .append() to construct the new list.

author_last_names = []
for name in author_names:
  author_last_names.append(name.split()[-1]) 
print(author_last_names)
# ['Lorde', 'Mistral', 'Toomer', 'Qi', 'Whitman', 'Silverstein', 'Boullosa', 'Suraiyya', 'Hughes', 'Rich', 'Giovanni']

