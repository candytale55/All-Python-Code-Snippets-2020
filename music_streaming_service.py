# We are building a music streaming service. We have two lists, representing songs in a user’s library and the amount of times each song has been played.
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.

plays = {key:value for key,value in zip(songs, playcounts)}
print(plays)

# Add a new song "Purple Haze" with playcount 1.
plays["Purple Haze"]=1
# user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect"
plays["Respect"]+=5
print(plays)

# Create a dictionary called library that has two key: value pairs:  key "The Best Songs" with a value of the dictionary plays. key "Sunday Feelings" with a value of an empty dictionary
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)

# Ref: https://discuss.codecademy.com/t/is-it-possible-to-statically-define-a-dictionary-which-contains-another-dictionary-without-using-another-variable/353052
