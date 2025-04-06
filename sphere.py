# Program that asks the user to enter the radius of a sphere and calculates and prints the volume
# Makanaka Mangwanda
# 05 April 2024

from math import pi, pow

def volume(radius):
 return round((4/3)*pow(radius,3)*pi,15)
 
   

def main():
  radius = eval(input('Enter the radius of the sphere:\n'))
  if radius > 0:
 
  
   print(f'The volume is {volume(radius):.2f}.')
  else:
   print('The radius must not be a negative value.')
  

if __name__ == '__main__':
 main()