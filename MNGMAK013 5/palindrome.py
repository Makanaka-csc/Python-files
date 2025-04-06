 # Program that uses a recursive function to calculate whether or not a string is a palindrome (reads the same if reversed)
 # Makanaka Mangwanda
 # 22 April 2024
 
def check(word):
    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word [-1]:
        return check (word [1: len(word)-1])
    return False

def main ():
    word = input('Enter a string:\n')
    if check(word) == False:
        print('Not a palindrome!')
    else:
        print ('Palindrome!')
if __name__ =='__main__': main()