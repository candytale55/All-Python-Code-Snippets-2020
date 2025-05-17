class Musician:
  title = "Rockstar"
 
drummer = Musician()
print(drummer.title)
# prints "Rockstar"


# When we want the same data to be available to every instance of a class we use a class variable. 
# A class variable is a variable that’s the same for every instance of the class.

# You can define a class variable by including it in the indented part of your class definition, 
# and you can access all of an object’s class variables with object.variable syntax.

# You are digitizing grades for Jan van Eyck High School and Conservatory. At Jan van High, 
# as the students call it, 65 is the minimum passing grade.


#class with a class attribute minimum_passing equal to 65.

class Grade:
  minimum_passing = 65

Test_Grade = Grade()
print(Test_Grade.minimum_passing) # 65


# REF: https://discuss.codecademy.com/t/can-a-class-variable-be-any-type/358375
