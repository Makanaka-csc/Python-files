# Program that searches a file for anagrams of a given word, printing the results in alphabetical order
# Makanaka Mangwanda
#30 April 2024

def frequency_of_word(word):
    """
    Returns the frequency of each letter in the word.
    
    """
    #started with an empty dictionary
    dict = {}
    for letter in word:
        if letter not in dict:
            dict[letter] = 1
            #if letter is already in dict,then add 1
        else:
            dict[letter]+=1
    return dict    

def find_anagrams(word,list_of_words):
    
    anagrams = []
    for w in list_of_words:
        k = w.strip('\n')
        
        if frequency_of_word(word) == frequency_of_word(k):
            if k != word:
                anagrams.append(k)
    return anagrams

def main():
    
        print('***** Anagram Finder *****')
        
        
       
        try:
            file = open('EnglishWords.txt','r')
            line = file.readline().strip()
            while line != "START":
                line = file.readline().strip()
                           
            word = input ('Enter a word:\n')
            word = word.lower()
            w1 = file.readlines()
            anagram_results = find_anagrams(word,w1)
            
            anagram_results.sort()
            
            if len(anagram_results) == 0:
                print("Sorry, anagrams of ",word," could not be found.",sep="'")
            else :
                print(anagram_results)
            
           
        except FileNotFoundError:
            print("Sorry, could not find file 'EnglishWords.txt'.")
            
if __name__ == '__main__':main()
            
    
    
    
