class SortedList(list):
  def append(self, value):
    super().append(value)
    self.sort()



## Subclassed a Python primitive and introduced new behavior

# lists have a .append() method that takes a two arguments, self and value. 
# We’re going to have SortedList perform a sort after every .append().

# .append() adds the item to the list, using super() to use the method from the parent class 
# and sorts the list using the self keyword to refer to the list in question: as self.sort()


#### TO DO: 
# When a SortedList gets initialized with unsorted values (say if you call SortedList([4, 1, 5])) those values don’t get sorted.  
# Change SortedList so that the list is sorted right after the object gets created?
# Could you write a new dictionary that uses a fallback value when it tries to retrieve an item and can’t.


# https://discuss.codecademy.com/t/when-do-i-need-to-use-super/436447
# https://discuss.codecademy.com/t/why-does-sortedlist-not-have-a-constructor/361708
# https://discuss.codecademy.com/t/bonus-challenge-discussion/436444
