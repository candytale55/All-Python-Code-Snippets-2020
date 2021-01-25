#max_num() takes a list of numbers as a parameter and returns the largest number

def max_num(nums):
  largest = nums[0]
  for num in nums:
    if num >= largest:
      largest = num
  return largest


print(max_num([50, -10, 0, 75, 20]))
