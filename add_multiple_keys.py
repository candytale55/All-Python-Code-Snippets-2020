# to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20}

# If we want to add 3 new rooms:
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)




user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# Ref: https://discuss.codecademy.com/t/if-a-dictionary-is-updated-with-an-empty-key-value-will-it-erase-the-contents-of-the-dictionary/352849
# https://discuss.codecademy.com/t/can-an-empty-key-be-used-to-insert-a-value-into-a-dictionary/352848
# https://discuss.codecademy.com/t/if-a-dictionary-is-updated-with-an-empty-key-value-will-it-erase-the-contents-of-the-dictionary/352849
