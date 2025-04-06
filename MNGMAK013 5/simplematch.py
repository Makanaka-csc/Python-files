#Program that contains a recursive function called ‘match(pattern, word)’, that can be  used to determine if a given pattern matches a given word.
# Makanaka Mangwanda
# 22 April 2024

def match(pattern,word):
    if pattern == '' and word == '':
        return True
    elif len(pattern)!= len(word):
        return False
    elif pattern [0] == word[0] or pattern[0] == '?':
        return match(pattern[1:], word[1:])
    else:
        return False
    
def main ():
    pattern = input("Enter a pattern (or 'q' to quit):\n")
    if pattern == 'q':
        return     
    word = input('Enter a word\n')
    if match(pattern,word) == True:
        print("It's a match.")
    else:
        print("They don't match.")
    
if __name__ == '__main__': main()        
    


 