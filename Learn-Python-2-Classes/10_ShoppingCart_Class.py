"""
classes and objects are often used to model real-world objects. This code is a more realistic example of classes and objects in commercial software. 

This is a basic ShoppingCart class for creating shopping cart objects for website customers; it’s basic but similar to what you’d see in a real program.
"""


class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."



my_cart = ShoppingCart("Victoria")
my_cart.add_item("Radiactive Potatoes", 13)
my_cart.add_item("Plums", 4)

print my_cart.items_in_cart
# {'Radiactive Potatoes': 13, 'Plums': 4}

my_cart.remove_item("Radiactive Potatoes")
print my_cart.items_in_cart
#{'Plums': 4}
