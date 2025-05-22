# THIS IS BY FAR NOT THE BEST PYTHON SOLUTION, but it is a copy of the procedure followed for the JavaScript simplest solution (the original problem). 


story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.'

# The string "story" splitted into individual words
story_splitted = story.split(" ")
#print story_splitted

unnecessary_words = ['extremely', 'literally', 'actually' ]

# Count how manny unnecessary words
# The words inside story_splitted are compared to unnecessary_words and counted

count_extremely = 0
count_literally = 0
count_actually = 0

for word in story_splitted:
  if word == "extremely":
    count_extremely += 1
  elif word == "literally":
    count_literally += 1
  elif word == "actually":
    count_actually += 1

print "Freq. extremely = " + str(count_extremely)
print "Freq. literally = " + str(count_literally)
print "Freq. actually = " + str(count_actually)

# Freq. extremely = 2
# Freq. literally = 1
# Freq. actually = 3


# REMOVE the unnecessary words
#  words in story_splitted are compared to unnecessary_words and if they are a match, they aren't added to new array story_filtered. 

story_filtered = []
for word in story_splitted:
  if word == "extremely":
    continue
  elif word =="literally":
    continue
  elif word == "actually":
    continue
  else:
    story_filtered.append(word)



fixed_story = " ".join(story_filtered)
print(fixed_story)
# Last weekend, I took the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It's really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you cross back into New York! At this point, you are very close to the end.




# PROOF: 
count_extremely = 0
count_literally = 0
count_actually = 0

for word in story_filtered:
  if word == "extremely":
    count_extremely += 1
  elif word == "literally":
    count_literally += 1
  elif word == "actually":
    count_actually += 1

print "Freq. extremely = " + str(count_extremely)
print "Freq. literally = " + str(count_literally)
print "Freq. actually = " + str(count_actually)

# Freq. extremely = 0
# Freq. literally = 0
# Freq. actually = 0
