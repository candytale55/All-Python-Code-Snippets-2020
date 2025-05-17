# Polymorphism is an abstract concept that covers a lot of ground, 
# but defining class hierarchies that all implement the same interface 
# is a way of introducing polymorphism to our code.



a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print(len(a_list))  # 4
print(len(a_dict))  # 1
print(len(a_string))  # 21


# REF: https://discuss.codecademy.com/t/how-do-i-make-len-work-with-my-class/361573/2

#  Flexibility in programming is a broad philosophy, 
# but what’s worth remembering is that we want to implement forms 
# that are familiar in our programs so that usage is expected. 

# All of these things are, for the arguments given to them, the intuitive result of adding them together. 


# For an int and an int, + returns an int
2 + 4 == 6
 
# For a float and a float, + returns a float
3.1 + 2.1 == 5.2
 
# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"
 
# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]



# Polymorphism is the term used to describe the same syntax (like the + operator here, but it could be a method name) doing different actions depending on the type of data.
