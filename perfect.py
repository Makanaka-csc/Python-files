# Program to check if a given number is perfect or not
# Makanaka Mangwanda
# 04 March 2024

# get the inputs from user
num = eval(input('Enter a number:\n'))
print('The proper divisors of',num,'are:\n',end='')
print(1,end=' ')
mid = num//2
for i  in range (2,mid+1):
  if num % i == 0:
    print(i,end=' ')
  
# Check if num is perfect or not
sum = 0
for i in range (1,num):
  if num % i == 0:
    sum = sum+i

    
if sum == num:
  print('\n')
  print(num,'is a perfect number.',end='')
else:
  print('\n')
  print(num,'is not a perfect number.',end='')

    

 
