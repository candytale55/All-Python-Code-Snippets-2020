# multiple_of_three takes an integer named num. If num is a multiple of three, return "multiple of three". Otherwise, return "not a multiple"


multiple_of_three = lambda num : "multiple of three" if num % 3 == 0 else "not a multiple"

print multiple_of_three(9)
# multiple of three

print multiple_of_three(10)
# not a multiple
