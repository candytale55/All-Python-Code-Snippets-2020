# Python 3. 

# initials.py displays the initials of your name in block letters (ASCII art) using multiple print() statements.
# ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced 
# together from individual characters. 





## Candy Tale 55  
## Fun Fact: I love weird books.


## BASIC SOLUTION 

print("   A   ","BBBBB  ","  C C   ")
print("  A A  ","B    B ","C     C ")
print(" A   A ","B    B ","C       ")
print("A A A A","BBBBB  ","C       ")
print("A     A","B    B ","C       ")
print("A     A","B    B "," C    C ")
print("A     A","BBBBB  ","  C C   ")



## MY SOLUTION: 

a = [
"   A    ",
"  A A   ",
" A   A  ",
"A A A A ",
"A     A ",
"A     A ",
"A     A "]


b = [
"BBBBB  ",
"B    B ",
"B    B ",
"BBBBB  ",
"B    B ",
"B    B ",
"BBBBB  "
]

c = [
"  C C   ",
"C     C ",
"C       ",
"C       ",
"C       ",
" C    C ",
"  C C   "
]

for i in range(7):
  print(a[i],b[i],c[i])







# With functions. It only prints one letter at a time.

def print_a():
  print("   A  ")
  print("  A A ")
  print(" A   A")
  print("A A A A")
  print("A     A")
  print("A     A")
  print("A     A")

# print_a() 


def print_b():
  print("BBBBB  ")
  print("B    B ")
  print("B    B ")
  print("BBBBB  ")
  print("B    B ")
  print("B    B ")
  print("BBBBB  ")



def print_s():
  print("  SSS  ")
  print(" S   S ")
  print(" S     ")
  print("  SSS  ")
  print("     S ")
  print(" S   S ")
  print("  SSS  ")

print_s()
