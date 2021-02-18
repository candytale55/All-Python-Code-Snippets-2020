# Functions can also take lists as inputs and perform various operations on those lists.

# Function _count_small_ takes one parameter, _numbers_, creates variable _total_ to use as counter in the for loop. 
# If n is less than 10, we increment total.  Total is returned after the loop.

def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total
 
lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print small  # 2



# function _fizz_count_ counts how many times the string "fizz" appears in a list

def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count +=1
  return count

print (fizz_count(["fizz","cat","fizz", "dog", "fizz"])) #3 
