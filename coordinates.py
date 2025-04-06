# Program  to check if a set of six numbers is a pair of geographical coordinates or not
# Makanaka Mangwanda
# 05 March 2024

# get the input from user
latD = eval(input('Enter first number:\n'))
latM = eval(input('Enter second number:\n'))
latS = eval(input('Enter third number:\n'))
longD =eval(input('Enter fourth number:\n'))
longM =eval(input('Enter fifth number:\n'))
longS =eval(input('Enter sixth number:\n'))

flag = True
 

if (latD<-90 or latD>90):
    flag = False

if (latM<0 or latM>59):
    flag = False
    
if (latS<0 or latS>59):
    flag = False

if (longD<-180 or longD>180):
    flag = False
    
if (longM<0 or longM>59):
    flag = False
    
if (longS<0 or longS>59):
    flag = False


    
    
if (flag == True):
    print('WOW! Looks like geographic coordinates!')
else:
    print('Hmm ... looks like 6 random numbers')  
    
                   
                       
                