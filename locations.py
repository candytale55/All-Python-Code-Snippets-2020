# You have two lists: a list of capitals and a list of countries. 
# Create a new list named locations that contains the string "capital, country" for each item in the original lists. 
# For example, if the 5th item in the capitals list is "Lima" and the 5th item in the countries list is "Peru", 
# then the 5th item in the new list should be "Lima, Peru"

capitals = ["Santiago", "Paris", "Copenhagen"]
countries = ["Chile", "France", "Denmark"]

locations = [item1 +", "+ item2 for (item1,item2) in zip(capitals, countries)]
print (locations)
# ['Santiago, Chile', 'Paris, France', 'Copenhagen, Denmark']
