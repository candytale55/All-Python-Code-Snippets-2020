# There's a Class CandleShop with a method .buy() when CandleShop.buy() tries to buy a candle that’s out of stock it raises exception class class OutOfStock
# An Exception is a class that inherits from Python’s built-in Exception class.


# Exceptions here:
class OutOfStock(Exception):
  pass
  # when CandleShop.buy() tries to buy a candle that’s out of stock.



class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color]==0:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock:
# candle_shop.buy('green')




# An Exception is a class that inherits from Python’s built-in Exception class.

# The issubclass() built-in function is takes two parameters and returns True if the first argument is a subclass of the second argument. 
# It returns False if the first class is not a subclass of the second. If either argument passed in is not a class it raises a TypeError.

print(issubclass(ZeroDivisionError, Exception))
# Returns True

# Exception hierarchy: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

#REFS: 
# https://discuss.codecademy.com/t/how-can-i-catch-a-raised-exception-and-pass-the-lesson/466673 
# https://discuss.codecademy.com/t/how-can-i-print-the-name-in-the-class/466679 
# https://discuss.codecademy.com/t/should-all-custom-exception-classes-inherit-from-exception/360336
