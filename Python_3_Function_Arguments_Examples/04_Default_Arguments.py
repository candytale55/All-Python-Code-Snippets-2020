# The second example doesn't work ok. The email creation can generate dupe email accounts and the print statements don't prove anything.

import os

def make_folders(folders_list, nest=False):
  if nest:
    """
    Nest all the folders, like
    ./Music/fun/parliament
    """
    path_to_new_folder = "."
    for folder in folders_list:
      path_to_new_folder += "/{}".format(folder)
      try:
        print(path_to_new_folder)
        os.makedirs("./" + path_to_new_folder)
      except FileExistsError:
        continue
  else:
    """
    Makes all different folders, like
    ./Music/ ./fun/ and ./parliament/
    """
    for folder in folders_list:
      try:
        os.makedirs(folder)

      except FileExistsError:
        continue

make_folders(['Music', 'fun', 'parliament'])





# Function arguments are required in Python. So a standard function definition that defines two parameters 
# requires two arguments passed into the function. 
# But if we give a default argument to a Python function that argument won’t be required when we call the function.

# Function defined with one required and one optional parameter
def create_user(username, is_admin=False):
  def create_email(username):
    return "username@mimail.com"
  def set_permissions(is_admin):
    pass
 
# Calling with two arguments uses the default value for is_admin. It assumes the default value for is_admin: False
user2 = create_user('djohansen')
print (user2)



# We can make all three parameters optional
def create_user_2(username=None, is_admin=False):
  if username is None:
    username = "Guest"
  else:
    def create_email(username):
      return "no email for Guest"
  def set_permissions(is_admin):
    pass
 
# So we can call with just one value
user3 = create_user_2('ssylvain')
# Or no value at all, which would create a Guest user
user4 = create_user_2()
print(user3)
print(user4)
