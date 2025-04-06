#Program that contains a recursive function called ‘match(pattern, word)’, that can be  used to determine if a given pattern matches a given word.
# Makanaka Mangwanda
# 22 April 2024

def match(pattern,word):
    #base case: if both pattern and word are empty, they match
    if pattern == '' and word == '':
        return True
    #If pattern and word have different lengths, they don't match
    elif len(pattern)!= len(word):
        return False
    #If the characters at the current positions match or if the pattern has a '?', continue matching recursively
    elif pattern [0] == word[0] or pattern[0] == '?':
        return match(pattern[1:], word[1:])
    else:
        return False
    
def main ():
    pattern = input("Enter a pattern (or 'q' to quit):\n")
    #If user inputs 'q', quit the program
    if pattern == 'q':
        return     
    word = input('Enter a word\n')
    #Check if pattern matches word 
    if match(pattern,word) == True:
        print("It's a match.")
    else:
        print("They don't match.")
    
if __name__ == '__main__': main()        
    


 