# Program that accepts a number,n, where -6<n<2
# Makanaka Mangwanda
# 11 March 2024

# get input from user
n = eval(input('Enter a number between -6 and 2:\n'))

# check if number is valid or not
if -6<n<2:
    for i in range(0,6):
        if 0 <= n < 10:
            print(f'{n:>2}',end='')
        
        else:
            print(f'{n:>2}',end='')
        n = n +1        
        for j in range(0,6):
            if 0 <= n < 10:
                print(f'{n:>3}',end='')
            
            else:
                print(f'{n:>3}', end='')
            n = n +1
        print("\n", end = "")
        

else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")
            
            
       
   
        
                      
  
       