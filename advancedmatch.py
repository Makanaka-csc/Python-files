# Program that can be used to determine if a given pattern matches a given word.
# Makanaka Mangwanda
# 22 April 2024

def match(pattern,word):
    #Base case: if both pattern and word are empty, they match
    if pattern == '' and word == '':
        return True
    #if youve reached the end of the pattern and not the word then its not a match and vice-versa   
    elif pattern == '' or word =='':
        return False 
    #Base case: if we've reached the end of the word or we are at a star
    elif pattern == '*' or word == '' :
        return True
    #If the current characters in pattern and word match, or if pattern has a wildcard '?' or '*', continue matching
    elif pattern [0] == word[0] or pattern[0] == '?':
        return match(pattern[1:], word[1:])
    #If the current character in pattern is '*',match zero or more characters in word  
    elif pattern[0] == '*':
        # check if the rest of the word matches the pattern or the rest of 
        return match(pattern,word[1:]) or match(pattern[1:],word)
    
    
      
      
      
def main():
    pattern = input("Enter a pattern (or 'q' to quit):\n")
    if pattern == 'q':
        return
    word = input ('Enter a word:\n')
    #check if pattern and word match
    if match(pattern,word) == True:
        print("It's a match.")
    else:
        print("They don't match.")
  
if __name__ == '__main__': main()


    