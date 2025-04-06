# Program that will print out every 7th number in the range n to n+41
# Makanaka Mangwanda
# 11 March 2024

n = eval(input('Enter a number between -6 and 2:\n'))

if -6<n<2:
    for n in range(n,n+41,7):
        if 0<= n < 10:
            print(f'{n:>2}')
        else:
            print(n)
            
else:
    print("Invalid input! The value of 'n' should be between -6 and 2.")
    


