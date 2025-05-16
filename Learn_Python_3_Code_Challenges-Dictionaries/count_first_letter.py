# count_first_letter takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names.

def count_first_letter(names):
  new_dict = {}
  for key,values in names.items():
    if key[0] not in new_dict:
      new_dict[key[0]] = len(values)
    else:
      new_dict[key[0]]+= len(values)
  return new_dict


# TESTS
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}


# REF: https://discuss.codecademy.com/t/is-it-possible-to-solve-this-with-list-comprehension/463057
# https://discuss.codecademy.com/t/what-does-key-0-from-the-dictionary-represent/463064
# https://discuss.codecademy.com/t/how-does-accessing-the-first-letter-work/463074
