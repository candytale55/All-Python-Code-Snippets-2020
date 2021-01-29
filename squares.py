# Python 3 
# You've been given a list of the numbers between 0 and 10. We created this list using the range function. 
# Create a new list named _squares_ that contains the square of every number in this list.

nums = range(11)
squares = [x ** 2 for x in nums]

print(nums)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
