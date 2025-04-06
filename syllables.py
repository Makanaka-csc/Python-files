# Program which repeatedly asks the user to enter a word (or ‘quit’) and then outputs (to the screen) the number of words that it contains.
# Makanaka Mangwanda
# 02 April 2024

# check if letter is a vowel
def is_vowel(letter):
        vowels =["a","e","i","o","u","y"]
        if letter in vowels:
                return True
        else:
                return False
        
# return the location of the next vowel in word
def next_vowel(word, index):      
        #i is less then the length of word
        for i in range(index,len(word)):
                if is_vowel(word[i]):
                        return i
        #if no vowel return the length f the word               
        return len(word)        
                 

# Given a word, calculate how many syllables it contains.
def count_syllables(word):
        i = 0
        count = 0
        word = word.lower()
        prev = False
        while i < len(word):  
                if is_vowel(word[i]):
                        if not prev:  # If the previous character was not a vowel
                                        count += 1
                                        prev = True
                else:
                        prev = False
                i += 1                       
             
                    
        # if word ends with 'e'
        if word[-1] == 'e' and count >1 and not is_vowel(word[-2]):
                count -= 1
               
          
        
        #have one syllable for empty words        
        if count == 0 and len(word) > 0:
                count = 1
                
        return count
        
   

def main():
        while True:
                
                word = input('Enter a word (or \'q\' to quit):\n')
                if word == 'q':
                        break
                if count_syllables(word)==1:
                        print("The word \'", word, '\' has ' ,count_syllables(word), " syllable.\n", sep="")
                else:
                        print("The word \'", word, '\' has ' ,count_syllables(word), " syllables.\n", sep="")   


if __name__ == '__main__':
        main()

