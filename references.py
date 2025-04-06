# Program to reformat references
# Makanaka Mangwanda
# 18 March 2024

ref = input('Enter the reference:\n')

print('Reformatted reference:')
# reformat the reference
surname = ref[ : ref.find(',')]
ref=ref[ ref.find(',')+2:]

name = ref[:ref.find('(')]
ref = ref[ ref.find('('):]

year = ref[:ref.find(' ')]
ref = ref[ ref.find(' ')+1:]

title = ref[:ref.find(',')]
ref = ref[ ref.find(','):]

other_info =ref
#other_info = str(SAICSIT Conference 2014, ACM, pp23-34, 2014')


# change to capital letters
surname =surname[0].upper() + surname[1:]
#print(surname, end=' ')
name= name[0].title() + name[1:]
#print(first_name, end=' ')
title = title.capitalize()
#print(title, end=' ')

print(end='')
print(surname + ", " + name+ ""+ year + " "+ title + other_info)


            


