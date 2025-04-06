# Program that asks the user to enter the length of three sides
# Makanaka Mangwanda
# 08 March 2024

side_one = eval(input('Enter the length of side 1:\n'))
side_two = eval(input('Enter the length of side 2:\n'))
side_three = eval(input('Enter the length of side 3:\n'))

if (side_one+side_two)> side_three and (side_two + side_three)>side_one and (side_one + side_three) > side_two:
  if (side_one == side_two == side_three):
   print("All sides are the same length: It's an equilateral triangle.")
  elif side_one != side_two and side_two != side_three:
   print("The sides are different lengths: It's a scalene triangle.")
  elif side_one == side_two:
    print("Two sides are the same length: It's an isoceles triangle.")
  elif side_two == side_three:
    print("Two sides are the same length: It's an isoceles triangle.")
  elif side_one == side_three:
    print("Two sides are the same length: It's an isosceles triangle.")
  

else:
   print("Those sides don't make a triangle!")