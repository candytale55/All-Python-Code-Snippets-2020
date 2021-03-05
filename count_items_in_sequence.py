# function _count_ takes two arguments called _sequence_ and _item_. It returns the number of times the item occurs in the list. 

# For example: count([1, 2, 1, 1], 1) should return 3 (because 1 appears 3 times in the list).

def count(sequence, item):
  count = 0
  for i in sequence:
    if i == item:
      count += 1
  return count


print count([1, 2, 1, 1], 1) # 3

print count([1, 2.0, 1, "1", 'apple'], 1) #2

print count([1, 2.0, 1, 1.0, 'apple'], 1)  #3
