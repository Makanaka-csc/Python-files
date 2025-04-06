# Program that asks a user to enter an interest rate
# Makanaka Mangwanda
# 01 March 2024

# inputs from user
P = eval(input('Enter the loan amount:\n'))
r = eval(input('Enter the annual interest rate:\n'))
y = eval(input('Enter the loan duration(years):\n'))

# Formula
A = P*(1 + r%100*y)

if P > 0:
    print('The repayment amount is', % A,end='.')
else:
    print('The values for amount, rate and duration must be greater than zero',end='.')








            

