# They have delivered you a string that contains a list of poems, titled highlighted_poems, 
# they want to highlight on the site, but they need your help to parse the string into something 
# that can display the name, title, and publication date of the highlighted poems on the site.


highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)
# Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987


# Start by splitting highlighted_poems at the commas 
highlighted_poems_list= highlighted_poems.split(",")
# print(highlighted_poems_list)
# ['Afterimages:Audre Lorde:1997', '  The Shadow:William Carlos Williams:1915', ' Ecstasy:Gabriela Mistral:1925', '   Georgia Dusk:Jean Toomer:1923', '   Parting Before Daybreak:An Qi:2014', ' The Untold Want:Walt Whitman:1871', " Mr. Grumpledump's Song:Shel Silverstein:2004", ' Angel Sound Mexico City:Carmen Boullosa:2013', ' In Love:Kamala Suraiyya:1965', ' Dream Variations:Langston Hughes:1994', ' Dreamwood:Adrienne Rich:1987']


# Then, iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list.
highlighted_poems_stripped = []
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
#print(highlighted_poems_stripped)
# ['Afterimages:Audre Lorde:1997', 'The Shadow:William Carlos Williams:1915', 'Ecstasy:Gabriela Mistral:1925', 'Georgia Dusk:Jean Toomer:1923', 'Parting Before Daybreak:An Qi:2014', 'The Untold Want:Walt Whitman:1871', "Mr. Grumpledump's Song:Shel Silverstein:2004", 'Angel Sound Mexico City:Carmen Boullosa:2013', 'In Love:Kamala Suraiyya:1965', 'Dream Variations:Langston Hughes:1994', 'Dreamwood:Adrienne Rich:1987']


# NOTE THAT THIS DOES NOT WORK AS INTENDED:
highlighted_poems_stripped_bad = []
for poem in highlighted_poems_list:
  poem.strip()
  highlighted_poems_stripped.append(poem)




# Break up all the information for each poem into it’s own list, so we end up with a list of lists. 
# Iterate through highlighted_poems_stripped and split each string around the : characters 
# and append the new lists into highlighted_poems_details

"""
# FIRST SOLUTION: 
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  poem_split = poem.split(":")
  highlighted_poems_details.append(poem_split)
print(highlighted_poems_details)
"""

# Improved in less lines of code
highlighted_poems_details = []
for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(":"))
#print(highlighted_poems_details)



# we want to separate out all of the titles, the poets, and the publication dates into their own lists.
titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
  titles.append(poem[0])
  poets.append(poem[1])
  dates.append(poem[2])
print("Titles: " + str(titles))
print("Poets: " + str(poets))
print("Dates: " + str(dates))
