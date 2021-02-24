# Define a function called reverse that takes a string text and returns that string in reverse. For example: reverse("abcd") should return "dcba"

# You may get a string containing special characters (for example, !, @, or #).

# You may not use reversed or [::-1] to help you with this.



def reverse(text):
  letter_list= []
  reversed_list = []
  for letter in text: 
    letter_list.append(letter)
  count = 0
  for i in range(len(letter_list)):
    reversed_list.append(letter_list[len(letter_list)-1-count])
    count += 1
  return "".join(reversed_list)

print reverse('abcd')
print reverse('Python!')  




# Using [::-1]

def reverse_splice(text):
  letter_list= []
  for letter in text: 
    letter_list.append(letter)
  return "".join(letter_list[::-1])

print reverse_splice('abcd')
print reverse_splice('Python!')  


# Using reversed

def reverse_reversed(text):
  return "".join(list(reversed(text)))
  

print reverse_reversed('abcd')
print reverse_reversed('Python!')  


# https://discuss.codecademy.com/t/how-can-i-loop-through-text-starting-from-the-last-character/339346
# https://discuss.codecademy.com/t/works-but-cc-fails-it/387297
# https://thepythonguru.com/python-builtin-functions/reversed/#:~:text=The%20reversed()%20function%20allows,sequence%20and%20returns%20an%20iterator.&text=A%20sequence%20list%20string%2C%20list%2C%20tuple%20etc.&text=To%20produce%20the%20result%20at,in%20a%20list()%20call.  
