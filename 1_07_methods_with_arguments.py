class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
 
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"


# Methods can also take more arguments than just self: we defined a DistanceConverter class, instantiated it, 
# and used it to convert 5 miles into kilometers. Even though how_many_kms takes two arguments in its definition, 
# we only pass miles, because self is implicitly passed (and refers to the object converter).




# It’s March 14th (known in some places as Pi day) at Jan van High, 
# and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.

# Circle class with class variable pi set to the approximation 3.14.
class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2
  
circle = Circle()
print(circle.area(3)) # 28.26



# A medium pizza that is 12 inches across.
pizza_area = circle.area(12/2)
print("The area of my pizza is {}".format(pizza_area))
# Your teaching table which is 36 inches across.
teaching_table_area = circle.area(36/2)
print("The area of the teaching table is {}".format(teaching_table_area))
# The Round Room auditorium, which is 11,460 inches across.
round_room_area = circle.area(11460/2)
print("The area of the round room area is {}".format(round_room_area))
