# we have two lists that we want to combine into a dictionary, like a list of students and a list of heights(in):
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {key:value for key, value in zip(names, heights)}
print(students)
# {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}


# zipped_drinks is a zipped list of pairs between a list of drinks sold at a coffee shop and a list with the the milligrams of caffeine in each.
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks_1_try = {key:value for key, value in zip(drinks, caffeine)}
print(zipped_drinks_1_try)

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)


# REF: https://discuss.codecademy.com/t/how-do-dictionaries-assign-order/462012
# https://discuss.codecademy.com/t/zip-creates-an-iterator-how-can-we-turn-that-into-a-dictionary/461985 
# https://discuss.codecademy.com/t/what-happens-if-a-list-contains-duplicates-when-creating-a-dictionary-using-zip-and-a-list-comprehension/352858
