# Python 2
# To run: python AreaCalculator.py

"""
# Python is especially useful for doing math 
and can be used to automate many calculations.
This project is a calculator that can compute
the area of Circles and Triangles.

# The program will:
#Prompt the user to select a shape.
#Calculate the area of that shape.
#Print the area of that shape to the user.
"""


print ("The calculator program is starting up . . . ")

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  radius = float(raw_input("Enter the radius: "))
  #float() converts a string to a floating point number
  area = 3.14159 * (radius ** 2)
  # print("The area of this circle is: " + str(area))
  print ("The area of this circle is %f " % (area))
elif option == "T":
  base = float(raw_input("What's the base?: "))
  height = float(raw_input("What's the height?: "))
  area = (base * height)/2
  print ("The area of this triangle is %f " % (area))
else:
  print ("Invalid shape")

print("Program is exiting . . .")



# From course _Learn Python 2_ here: https://www.codecademy.com/learn/learn-python
# For confirmation: http://es.onlinemschool.com/math/assistance/figures_area/triangle/
