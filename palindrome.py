 # Program that uses a recursive function to calculate whether or not a string is a palindrome (reads the same if reversed)
 # Makanaka Mangwanda
 # 22 April 2024
 
def palindrome(word):
    #Base case: if the word is empty or has only one character, it's a palindrome
    if len(word) == 0 or len(word) == 1:
        return True
     #If the first and last characters match, check recursively for the substring without those character
    if word[0] == word [-1]:
        return palindrome(word [1: len(word)-1])
    #If the first and last characters don't match, it's not a palindrome
    return False

def main ():
    word = input('Enter a string:\n')
    #Check if the input string is a palindrome and print the result
    if palindrome(word) == False:
        print('Not a palindrome!')
    else:
        print ('Palindrome!')
if __name__ =='__main__': main()