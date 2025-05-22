"""
Sometimes you’ll want one class that inherits from another to not only take on the methods and attributes of its parent, 
but to override (or re-create) one or more of them.
"""



class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00



# class PartTimeEmployee inherits from Employee. PartTimeEmployee.calculate_wage overrides Employee.calculate_wage
class PartTimeEmployee(Employee):
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00


Joel = PartTimeEmployee("Joel")
print Joel.calculate_wage(23) # 276

Christina = Employee("Christina")
print Christina.calculate_wage(23) # 460


# https://discuss.codecademy.com/t/what-does-it-mean-to-override-a-method/340795
"""
By defining a method with the same name as found in the base class, Employee, 
we are overriding the functionality so that any PartTimeEmployees will have their wages calculated appropriately.
"""

