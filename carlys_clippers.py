# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. 
# Your job is to go through the lists of data that have been collected in the past couple of weeks. 
# You will be calculating some important metrics that Carly can use to 
# plan out the operation of the business for the rest of the month.


# names of the cuts offered at Carly’s Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

# price of each hairstyle in the hairstyles list
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# the number of each hairstyle in hairstyles that was purchased last week (in other words, the number of people who got each hairstyle)
last_week = [2, 3, 5, 8, 4, 4, 6, 2]



# 1. We want to find out what the average price of a cut is.
total_price = 0

for price in prices:
  total_price += price
# print(total_price)  # 255

average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price)) # 31.875


# 5. That average price is too expensive. She wants to cut all prices by 5 dollars (using a list comprehension).

new_prices = [price - 5 for price in prices]
new_total = 0
for price in new_prices:
  new_total += price
#print(new_prices)
print("New Average Haircut Price " + str(new_total/len(new_prices)))




#  To know how much revenue was brought in last week.

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue: " + str(total_revenue)) 


# Find the average daily revenue by dividing total_revenue by 7.
average_daily_revenue = total_revenue / 7
print("Average daily revenue " + str(average_daily_revenue))



# Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars. Use a list comprehension.

# Without list comprehension
cuts_under_30 = []
for i in range(len(new_prices)-1):
  if new_prices[i]<30:
    cuts_under_30.append(hairstyles[i])
print(cuts_under_30)
# ['bouffant', 'pixie', 'crew', 'bowl']

# Same result Using list comprehension
cuts_under_30 = []
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i]<30]
print(cuts_under_30)
# ['bouffant', 'pixie', 'crew', 'bowl']

print("Try these awesome cuts for less than $30.00")
for cuts in cuts_under_30:
  print("The " + cuts )





# Walktrough: https://youtu.be/ddMHCEs-wmE
