"""
sometimes you’ll be working with a derived class (or subclass) and realize that you’ve overwritten 
a method or attribute defined in that class’ base class (also called a parent or superclass) 
that you actually need. Have no fear! You can directly access the attributes or methods of a 
superclass with Python’s built-in super call.

The syntax looks like this:

class Derived(Base):
  def m(self):
    return super(Derived, self).m()

Where m() is a method from the base class.
"""



class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00




# class PartTimeEmployee inherits from Employee. PartTimeEmployee.calculate_wage overrides Employee.calculate_wage. 
# If you want to calculate the full wage, there is another method full_time_wage, 
# to be used if you want to use the parent metod calculate_wage

class PartTimeEmployee(Employee):

  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00





Joel = PartTimeEmployee("Joel")
print Joel.calculate_wage(23) # 276

Christina = Employee("Christina")
print Christina.calculate_wage(23) # 460

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10) # 200
print milton.calculate_wage(10) # 120


# https://discuss.codecademy.com/t/what-does-it-mean-to-override-a-method/340795
# https://discuss.codecademy.com/t/how-do-i-print-my-new-employee-s-full-time-wage-results/340797
"""
By defining a method with the same name as found in the base class, Employee, 
we are overriding the functionality so that any PartTimeEmployees will have their wages calculated appropriately.
"""
