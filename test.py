# Program thatasks user to enter a series of number sand words
# Makanaka Mangwanda
# 12 April 2024

pairs= 1
prev = -1
i = 1
while True:
    txt = input("Enter an integer or string (or 'DONE' to exit):\n") 
      
    if txt == 'DONE':
        break
    
    if int(prev)< int(i) :
        prev = i
        pairs+= 1
      
print('The number of adjacent pairs integers in descending order:',pairs)    