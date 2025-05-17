# Not all arguments need to have default values. 
# But Python will only accept functions defined with their parameters in a specific order. 
# The required parameters need to occur before any parameters with a default argument.


# Raises a TypeError
def create_user(is_admin=False, username, password):
  create_email(username, password)
  set_permissions(is_admin)

# If we want to give is_admin a default argument, we need to list it last in our function definition:

# Works perfectly
def create_user(username, password, is_admin=False):
  create_email(username, password)
  set_permissions(is_admin)
