# Program to determine whether a year is a leap year or not
# Makanaka Mangwanda
# 28 February 2024

# input from user
year = eval(input('Enter a year:\n'))

# determine whether leap year or not
if (year %400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,'is a leap year.')
    
else:
    print(year, 'is not a leap year.')
    

