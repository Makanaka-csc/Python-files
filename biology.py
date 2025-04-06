# Program to determine the type of an animal 
# Makanaka Mangwanda
# 04 March 2024


print('Welcome to the Biology Expert')
print('-----------------------------')
print('Answer the following questions by selecting from among the options.')

# get the inputs from user
skeleton = input('The skeleton is (internal/external)?\n')
if (skeleton == 'external'):
    print('Type of animal: Arthropod')
else:
    b = input('The fertilisation of eggs occurs (within the body/outside the body)?\n')
    if b == 'within the body':
        c = input('Young are produced by (waterproof eggs/live birth)?\n')
        if c == 'waterproof eggs':
            d = input('The skin is covered by (scales/feathers)?\n')
            if d == 'scales':
                print('Type of animal: Reptile')
            else:
                print('Type of animal: Bird')
        else:
            print('Type of animal: Mammal')
    else:
        e = input('It lives (in water/near water)?\n')
        if e == 'in water':
            print('Type of animal: Fish')
        else:
            print('Type of animal: Amphibian')
                
     







