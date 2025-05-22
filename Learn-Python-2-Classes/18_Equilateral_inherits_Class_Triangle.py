class Triangle(object):
  number_of_sides = 3
  def __init__(self, angle1, angle2, angle3):
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    if (self.angle1 + self.angle2 + self.angle3) == 180:
      return True
    else:
      return False
    
class Equilateral(Triangle):
  angle = 60
  def __init__(self):
    self.angle1 = self.angle
    self.angle2 = self.angle
    self.angle3 = self.angle

 
my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()


# https://discuss.codecademy.com/t/how-do-i-add-a-member-variable-to-the-triangle-class/340802
# https://discuss.codecademy.com/t/how-should-i-indent-the-code-to-create-my-triangle/340804
# https://discuss.codecademy.com/t/how-can-i-assign-my-equilateral-angle-values/340805
