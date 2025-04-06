# Program to convert an amount of minutes into an equivalent amount of days, hours and minutes
# Name : Stephen Jamieson Name 

# input the number of minutes
input_str = input('Enter a quantity of minutes: ')
minutes = int(input_str)
 
hours = minutes//60
 
days = hours//24
print('The number of days is', days, end=', ')
hours = hours%24
print('the number hours is', hours, end=', ')
minutes = minutes%60
print('and the number of minutes is', minutes, end='')
print('.')




