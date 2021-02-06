# A dictionary is an unordered set of key: value pairs. EXAMPLES: 


# You have a dictionary of temperature sensors in your house and what temperatures they read. 

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# The dictionary num_cameras represents the number of cameras in each area around your house.
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
# {'living room': 21, 'kitchen': 23, 'bedroom': 20, 'pantry': 22}

print(num_cameras)
# {'backyard': 6, 'garage': 2, 'driveway': 1}



# keys can be numbers as well. For example, mapping restaurant bill subtotals to the bill total after tip: 
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

# Values can be any type: a string, a number, a list, or even another dictionary: 
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}
print (students_in_classes["software design"])
# ['Aaron', 'Delila', 'Samson']

# You can also mix and match key and value types:

person = {"name": "Shuri", "age": 18, "siblings": ["T'Chaka", "Ramonda"]}



# Reference: https://discuss.codecademy.com/t/why-arent-dictionaries-printed-in-the-same-order-as-they-are-created/461685
