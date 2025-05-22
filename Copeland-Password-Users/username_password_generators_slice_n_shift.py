# username_generator take two inputs, first_name and last_name and returns a username. The username should be 
# a slice of the first three letters of their first name and the first four letters of their last name. 
# If their first name is less than three letters or their last name is less than four letters it should use their entire names.

def username_generator(first_name, last_name):
  if len(first_name)>=3 and (len(last_name)>=4):
    username = first_name[:3] + last_name[:4]
  elif (len(first_name)<3) and (len(last_name)>=4):
    username = first_name + last_name[:4]
  else:
    username = first_name + last_name
  return username


# TESTS: 
print(username_generator("Abe", "Simpson")) # AbeSimp
print(username_generator("Homer", "Simpson")) # HomSimp
print(username_generator("Ty", "Johnson")) # TyJohn
print(username_generator("Ty", "Chi")) # TyChi
print(username_generator("Mi", "Li")) # MiLi




# For the temporary password, they want the function to take the input user name and shift all of the letters 
# by one to the right, so the last letter of the username ends up as the first letter. 
# If the username is AbeSimp, then the temporary password generated should be pAbeSim.

def password_generator(username):
  return username[-1] + username[0:len(username)-1]

username = username_generator("Abe", "Simpson")
print(username) # AbeSimp
password = password_generator(username)
print(password) # pAbeSim
