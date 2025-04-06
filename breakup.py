# Program that accepts a sentence as input and that outputs it as a comma-separated list of lowercase words with a full-stop at the end.
# Makanaka Mangwanda
# 20 March 2024

#get the input from the user
sen = input('Enter a sentence:\n')

#make the sentence lower case
sen = sen.lower()

print('The word list:',end=' ')  

#first space
spaceOne = 0

#position of the next space
while True:
    spaceTwo = sen.find(" ",spaceOne)
    #if they are no more spaces break 
    if spaceTwo == -1:
        word = sen[spaceOne:]
        print(word,end='.')
        break
    #word between spaceOne and spaceTwo
    word = sen[spaceOne:spaceTwo]
    #add commas to sen
    print(word,end=', ')
    #use spaceTwo to search for the next word 
    spaceOne=spaceTwo+1
  
 

