# You have two lists: a list of names and a list of ages. 
# Create a new list named users that contains the string "Name: name, Age: age" 
# for each pair of elements in the original lists. 
# For example, if the 5th item in the names list is "Aiyana" and the 5th item in ages is 42, 
# then the 5th item in the new list should be "Name: Aiyana, Age: 42".


names = ["Shilah", "Arya", "Kele"]
ages = [14, 9, 35]

users = ["Name: "+ name + ", Age: " + str(age) for (name, age) in zip(names, ages) ]
print (users)

# ['Name: Shilah, Age: 14', 'Name: Arya, Age: 9', 'Name: Kele, Age: 35']
