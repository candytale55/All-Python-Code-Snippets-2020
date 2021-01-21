# Python 3 (Coded in Jan 2020)

# magic8.py answers any “Yes” or “No” question with a different random fortune each time it executes using randint and an if/elif/else control flow.  
# It is inspired in the Magic 8-Ball, a popular toy developed in the 1950s for fortune-telling or advice seeking.


import random

#input('What is your name?: ')
name = "Vicky"
question = "Is this just fantasy?"
answer = ""

if (name ==""):
  print("Question: "+ question)
else:
  if (question == ""):
    print(name +" asks: NOTHING")
  else: 
    print(name +" asks: "+ question)

# If you add more answers to the elif flow below, you must also increase the randint range or their random number will never show up.
random_number = random.randint(1,10) 

if (random_number == 1):
  answer = "Yes - definetely"
elif (random_number == 2):
  answer = "It is decidedly so."
elif (random_number == 3):
  answer = "Without a doubt."
elif (random_number == 4):
  answer = "Reply hazy, try again."
elif (random_number == 5):
  answer = "Ask again later."
elif (random_number == 6):
  answer = "Better not tell you now."
elif (random_number == 7):
  answer = "My sources say no."
elif (random_number == 8):
  answer = "Outlook not so good."
elif (random_number == 9):
  answer = "Very doubtful."
elif (random_number == 10):
  answer = "Nope! - sorry."
else:
  answer = "Error"

if (question == ""):
  print("Magic 8-Ball: Hey, if you don't ask your question I can't help you.")
else:
  print("Magic 8-Ball's answer: " + answer)
  
