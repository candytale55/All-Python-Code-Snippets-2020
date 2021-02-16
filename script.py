## _You’ve started position as the lead programmer for the family-style Italian restaurant Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen a lot of growth lately. You’ve been hired to keep things organized._

# Basta Fazoolin’ with my Heart  has four different menus: brunch, early-bird, dinner, and kids.



#  .calculate_bill() takes two parameters: self, and purchased_items (a list of the names of purchased items).


class Menu:
  def __init__(self, name, items, start_time,end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "{} menu is available from {} until {}".format(self.name, self.start_time, self.end_time)  

# Brunch is served from 11am to 4pm
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

print(brunch.items)
print(" ")

# Early-bird Dinners are served from 3pm to 6pm.
early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 15, 18)

print(early_bird.items)
print(" ")

# Dinner is served from 5pm to 11pm.
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}, 17, 23)

print(dinner.items)
print(" ")

# Kids menu is available from 11am until 9pm.
kids = Menu("Kids Menu", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11am", "9pm")

print(kids.items)
print(" ")

print(kids)
print(early_bird)
print(brunch)
print(dinner)

print(" ") 


#  .calculate_bill() takes two parameters: self, and purchased_items (a list of the names of purchased items).






# REF: https://docs.python.org/3/library/datetime.html#time-objects
# https://www.youtube.com/watch?v=Dk-ePlxdmBU
