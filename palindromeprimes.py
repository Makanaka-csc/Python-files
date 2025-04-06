# Program that uses recursive functions to find all palindromic primes between two integers N,M, supplied as input.
# Makanaka Mangwanda
# 23 April 2024

import sys 
sys.setrecursionlimit (30000)

def palindrome(number):
    #Function to check if a number is a palindrome
    number = str(number)
    if len(number) == 0 or len(number) == 1:
        return True
  
    if number[0] == number [-1]:
        return palindrome (number [1: len(number)-1])
    return False


def prime(number,divisor):
    # if number is divisible by 2, then it is not a prime
    if divisor == number:
        return True
    if number % divisor == 0:
        return False
    # if the number is less than 2 then it is not a prime number
    if number < 2:
        return False
    return prime(number,divisor+1)
    
def palindrome_primes(N,M):
    pali = ''
    #Base case: if N is greater M, return empty string
    if N > M:
        return pali
    else:
         #Check if N is both a palindrome and prime
        if palindrome(N) == True and prime(N,2) == True:
            N  = str(N)
            #Add N to the list of palindromic primes
            pali = pali + N + '\n'
            print(N)
            
            N = int(N)
        #Recursive call with N+1
        palindrome_primes(N+1,M)
            

def main():
    # get the inputs from the user
    start = eval(input('Enter the starting point N:\n'))
    end = eval(input('Enter the ending point M:\n'))
    
   
    print('The palindromic primes are: ')
    palindrome_primes(start,end)
   
        
if __name__ == '__main__' : main()