# You are a physics teacher preparing for the upcoming semester. 
# You want to provide your students with some functions that will 
# help them calculate some fundamental physical properties.




# def f_to_c (f_temp)
# takes an input f_temp, a temperature in Fahrenheit, 
# and converts it to c_temp, that temperature in Celsius. 

def f_to_c (f_temp):
  return (f_temp -32) * 5/9

c_temp = f_to_c (32) 
print(c_temp)           #  0.0  

c_temp = f_to_c (15)
print(c_temp)           # -9.444444444444445


# Define a variable f100_in_celsius and set it equal to the value 
# of f_to_c with 100 as an input.
f100_in_celsius = f_to_c (100)
print(f100_in_celsius)   # 37.77777777777778




# def c_to_f (c_temp)
# Write a function called c_to_f that takes an input c_temp, 
# a temperature in Celsius, and converts it to f_temp in Fahrenheit.

def c_to_f (c_temp):
  return c_temp * (9/5) + 32

f_temp = c_to_f(0) 
print (f_temp)     # 32.0

print(c_to_f(15))  # 59.0



# get_force(mass, acceleration)
# Define a function called get_force that takes in mass and acceleration. 
# It should return mass multiplied by acceleration.

def get_force(mass, acceleration):
  return mass * acceleration

train_mass = 22680
train_acceleration = 10

train_force = get_force (train_mass, train_acceleration)
print (train_force)  # 226800

print("The GE train supplies " + str(train_force)+ " Newtons of force.")  
# The GE train supplies 226800 Newtons of force.




# get_energy (mass, c=3*10**8)
# Define a function called get_energy that takes in mass and c.  
# get_energy should return mass multiplied by c squared.

# c is a constant that is usually set to the speed of light, 
# which is roughly 3 x 10^8. Set c to have a default value of 3*10**8.

def get_energy (mass, c=3*10**8):
  return mass * c**2

bomb_mass = 1
bomb_energy = get_energy(bomb_mass)
print (bomb_energy)  # 90000000000000000
print ("A 1kg bomb supplies "+ str(bomb_energy) +" Joules.")


# get_work (mass, acceleration, distance)
# get_work takes in mass, acceleration, and distance.  
# Work is defined as force multiplied by distance. 
# First, get the force using get_force, 
# then multiply that by distance. Return the result.

train_distance = 100

def get_work (mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

train_work = get_work(train_mass, train_acceleration, train_distance)
print (train_work) # 22680000
print ("The GE train does " + str(train_work) + " Joules of work over "+ str(train_distance)+ " meters.")
# The GE train does 22680000 Joules of work over 100 meters.


# Reference: https://www.youtube.com/watch?v=tBG5dCcTjZo
