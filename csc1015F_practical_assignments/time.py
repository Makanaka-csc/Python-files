# Program to check the validity of a time entered by a user
# Makanaka Mangwanda
# 27 February 2024

# input values 
hours = eval(input('Enter the number of hours: \n'))
minutes = eval(input('Enter number of minutes: \n')) 
seconds = eval(input('Enter the number of seconds: \n'))

# check validity of a time entered by user
if 0 <= hours <= 24 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print('Your time is valid.')
else:
    print('Your time is invalid.')


 
    

    

