# BASE CLASS:
class Bin:
  pass

class RecyclingBin(Bin):
  pass


# If the bulk of a class’s definition is useful, but we have a new use case that is distinct from how the original class was used, we can inherit from the original class.




# User is the Base class:
class User:
  is_admin = False
  def __init__(self, username)
    self.username = username
 
# Admin is a subclass of User
class Admin(User):
  is_admin = True



# REF: https://discuss.codecademy.com/t/can-a-class-inherit-from-more-than-one-base-class/359836
