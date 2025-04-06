# Program that accepts a sentence as input and translates it to a variant of Pig Latin
# Makanaka Mangwanda
# 19 March 2024

# get the input from user
sen = input('Enter a sentence:\n')

#make the sentence lower case
sen = sen.lower()
          
        
#first space
spaceOne = 0

pig_latin = ''
        
#position of the next space
while True:
            spaceTwo = sen.find(" ", spaceOne)
            #if they are no more spaces break 
            if spaceTwo == -1:
                        word = sen[spaceOne:]
                        break
            #word between spaceOne and spaceTwo
            word = sen[spaceOne:spaceTwo]
            
            
            # if the word starts with a vowel add 'way' at the end
            if word[0] in 'aeiou':
                        pig_latin += word + "way "
            else:
                        for i in range(len(word)):
                                    if word[i] in 'aeiou':
                                                break
                        pig_latin += word[i:]+"a"+word[0:i]+'ay '  
            #start searchong from space 2
            spaceOne = spaceTwo+1
         
                        
            
#convert the last word into pig_latin 
#if the word starts with a vowel add 'way' at the end
if word[0] in 'aeiou':
            pig_latin += word + "way"
           
else:
            for i in range(len(word)):
                        if word[i] in 'aeiou':
                                    break
            pig_latin += ''+word[i:]+"a"+word[:i]+'ay' 
           

#print the translation            
print(pig_latin)


            
            
           