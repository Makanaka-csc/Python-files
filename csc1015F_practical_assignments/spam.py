# Program to generate a personalised spam message based on the user's full name,country and a sum of money
# Makanaka Mangwanda 
# 28 February 2024

# get the inputs from the user
name1 = input('Enter first name: \n')
name2= input('Enter last name: \n')
money = input('Enter sum of money in USD: \n')
country = input('Enter country name: \n')

print('Dearest', name1)
print('It is with a heavy heart that I inform you of the death of my father,')
print('General Fayk', name2 + ",",'your long lost relative from Mapsfostol.')
print('My father left the sum of', money, 'USD for us, your distant cousins.')
print('Unfortunately, we cannot access the money as it is in a bank in' , country + '.')
print('I desperately need your assistance to access this money.')
print('I will even pay you generously, 30% of the amount -', money,'USD,')
print('for your help.  Please get in touch with me at this email adress asap.')
print('Yours sincerely')
print('Frank', name2)



