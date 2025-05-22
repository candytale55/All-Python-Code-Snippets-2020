# DESCRIPTION: When planning a vacation, it’s very important to know exactly how much you’re going to spend. 
# Function trip_cost takes three parameters, city, days and spending_money and returns the sum of calling 
# functions rental_car_cost(days), hotel_cost(days - 1), and plane_ride_cost(city) functions + spending_money 
# passed as argument to provide a total cost for a vacation.




# Function hotel_cost takes one argument "nights" as input.  The hotel costs $140 per night. 
# So, the function hotel_cost should return 140 * nights.

def hotel_cost(nights):
  return 140 * nights

print hotel_cost(3) # 420




# plane_ride_cost that takes a string, city, as input. 
# The function should return a different price depending on the location

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh": 
    return 222
  elif city == "Los Angeles": 
    return 475
  else: 
    return "nope, try other city"

print plane_ride_cost("Charlotte")  # 183
print plane_ride_cost("Tampa")      # 220 
print plane_ride_cost("Pittsburgh") # 222
print plane_ride_cost("Los Angeles")  # 475
print plane_ride_cost("Cairo") # nope, try other city





# Calculate the cost of renting a car. Every day you rent the car costs $40. 
# If you rent the car for 7 or more days, you get $50 off your total. 
# Alternatively (elif), if you rent the car for 3 or more days, you get $20 off your total. 
# You cannot get both of the above discounts.

def rental_car_cost(days):
  if (days <3):
    return days * 40
  elif (days >= 3 and days <7):
    return (days * 40) - 20 
  elif (days >= 7):
    return (days * 40) - 50
  
print rental_car_cost(2)  #  80
print rental_car_cost(3)  # 100
print rental_car_cost(6)  # 220
print rental_car_cost(7)  # 230
print rental_car_cost(8)  # 270





# trip_cost takes three parameters, city, days and spending_money and returns 
# the sum of calling the rental_car_cost(days), hotel_cost(days - 1), and plane_ride_cost(city) functions + spending_money 
# passed as argument (spending_money intended for additional costs like fancy food or souvenirs.).


# Argument of hotel_costs() from nights to days - 1 => Since we want trip-cost to only depend on two parameters, 
# we have to convert the variable nights into days. If you are going to be staying somewhere, 
# the number of nights you stay there is one less than the number of days you were there.


def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money


print trip_cost("Tampa", 3, 100) # 700
print trip_cost("Charlotte", 3, 5) # 568


# print out the trip_cost( to "Los Angeles" for 5 days with an extra 600 dollars of spending money.

print trip_cost("Los Angeles", 5, 600)
