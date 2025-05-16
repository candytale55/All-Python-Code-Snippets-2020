# .format() takes variables as an argument and includes them in the string that it is run on. 
# You include {} marks as placeholders for where those variables will be imported.

def favorite_song_statement(song, artist):
  return "My favorite song is {} by {}.".format(song, artist)

print(favorite_song_statement("Smooth", "Santana")) # My favorite song is Smooth by Santana.




# poem_title_card() takes two inputs: the title of the poem and the poet. 
# The function should use .format() to return the following string:  The poem "[TITLE]" is written by [POET].

def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card("I Hear America Singing", "Walt Whitman")) 
# The poem "I Hear America Singing" is written by Walt Whitman.



# .format() can be made even more legible for other people reading your 
# code by including keywords in the string and in the arguments. 

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc


my_beard_description = poem_description(
author = "Shel Silverstein",
title = "My Beard",
original_work = "Where the Sidewalk Ends",
publishing_date = "1974"
)
print(my_beard_description)
# The poem My Beard by Shel Silverstein was originally published in Where the Sidewalk Ends in 1974.


# Returns the same as:
my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")
print(my_beard_description)
# The poem My Beard by Shel Silverstein was originally published in Where the Sidewalk Ends in 1974.
