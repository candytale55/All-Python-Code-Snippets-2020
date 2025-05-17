class UserGroup:
  def __init__(self, users, permissions):
    self.user_list = users
    self.permissions = permissions
 
  def __iter__(self):
    return iter(self.user_list)
 
  def __len__(self):
    return len(self.user_list)

# we defined three methods:
# __init__() is the  constructor, which sets a list of users to the instance variable self.user_list and sets the group’s permissions when we create a new UserGroup.
# __iter__ is an iterator, we use the iter() function to turn the list self.user_list into an iterator so we can use for user in user_group syntax. 
# __len__ is the length method. When we call len(user_group) it will return the length of the underlying self.user_list list.
# __contains__ is the check for containment, allows us to use user in user_group syntax to check if a User exists in the user_list we have.

# Those methods allow UserGroup to act like a list using syntax familiar to Python users. 
# If you just need a list, a list is enough, but if you want to bundle some other information 
# (like a group’s permissions, for instance) having syntax that allows for list-like operations can be very powerful.

class User:
  def __init__(self, username):
    self.username = username
 
diana = User('diana')
frank = User('frank')
jenn = User('jenn')
 
can_edit = UserGroup([diana, frank], {'can_edit_page': True})
can_delete = UserGroup([diana, jenn], {'can_delete_posts': True})
 
print(len(can_edit))
# Prints 2
 
for user in can_edit:
  print(user.username)
# Prints "diana" and "frank"
 
if frank in can_delete:
  print("Since when do we allow Frank to delete things? Does no one remember when he accidentally deleted the site?")


# we created a set of users and then added them to UserGroups with specific permissions. 
# Then we used Python built-in functions and syntax to calculate the length of a UserGroup, 
# to iterate through a UserGroup and to check for a User‘s membership in a UserGroup.





class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  def __len__(self):
    return len(self.lawyers)
  def __contains__(self, lawyer):
    return lawyer in self.lawyers

    
d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])

# __len__() method that will return the number of lawyers in the law firm.

# __contains__() method takes two parameters: self and lawyer and checks to see if lawyer is in self.lawyers.


# ref: https://discuss.codecademy.com/t/what-is-the-return-value-when-implementing-contains/361690
# https://discuss.codecademy.com/t/why-do-we-need-a-dunder-method-if-list-already-has-len/467775
