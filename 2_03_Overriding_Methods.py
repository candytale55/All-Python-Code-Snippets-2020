# Inheritance is a useful way of creating objects with different class variables, 
# but if one of the methods from the parent class needs to be implemented differently, 
# in Python you  have to override a method definition and offer a new definition for the method in our subclass.

# An overridden method is one that has a different definition from its parent class. 
# What if User class didn’t have an is_admin flag but just checked if it had permission for something based on a permissions dictionary.


# class User which takes a permissions parameter in its constructor. 

class User1:
  def __init__(self, username, permissions):
    self.username = username
    self.permissions = permissions
 
  def has_permission_for(self, key):
    if self.permissions.get(key):
      return True
    else:
      return False

# Let’s assume permissions is a dict. User has a method .has_permission_for() implemented, where it checks to see if a given key is in its permissions dictionary. We could then define our Admin user like this:

class Admin1(User1):
  def has_permission_for(self, key):
    return True

# Admin class has all methods, attributes, and functionality that User has. 
# However, if you call has_permission_for on an instance of Admin, it won’t check its permissions dictionary. 
# Since this User is also an Admin, we just say they have permission to see everything




class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text


# Create an Admin class that subclasses the User class and override User's .edit_message() method in Admin so that an Admin can edit any messages.

class Admin(User):
    def edit_message(self, message, new_text):
      message.text = new_text


# REF: https://discuss.codecademy.com/t/can-an-method-which-is-overridden-still-call-the-parent-method-if-needed/360643
# https://discuss.codecademy.com/t/how-does-edit-message-know-to-reference-the-message-class/466691
