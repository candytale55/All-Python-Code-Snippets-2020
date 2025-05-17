menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print(menu)
#  If we already have an 'avocado toast' entry in the menu dictionary, our value assignment would overwrite the existing value.
menu["oatmeal"] = 5
menu['avocado toast'] = 7
print(menu)



oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"]= "Viola Davis"
oscar_winners["Best Picture"]="Moonlight"
print(oscar_winners)


# REF: https://discuss.codecademy.com/t/can-the-data-type-of-a-value-be-changed-when-overwriting-it-in-a-dictionary/352855
# https://discuss.codecademy.com/t/can-we-overwrite-a-key/461952 
# https://discuss.codecademy.com/t/should-we-use-update-or-value-assignment/461981
