#Program that will search the ‘EnglishWords.txt’ file for sets of words that are that length and are anagrams of each other, and will write the results to a file with the given filename
#Makanaka Mangwanda
#04 May 2024


print('***** Anagram Set Search *****')
try:
    #get the input from the user
    word_length = int(input('Enter word length:\n'))
    
    
    
    print('Searching...')
    
    filename = input('Enter file name:\n') 


    Englishfile = open('EnglishWords.txt','r')
    for line in Englishfile:
                if 'START' in line.strip():
                    break 
                
                
    lines = Englishfile.readlines()
   
            
    
    
    Englishfile.close()
    
    # a list to store words of the specified length
    words = []
    for k in lines:
        if len(k.strip()) == word_length:
            words.append(k.strip())
        

    anagram_sets = []
    existing_anagrams = set()
    
    for i in range(len(words)):
        anagrams = [words[i]]
        for j in range(i + 1, len(words)):
            # Checking if the two words are anagrams
            if sorted(words[i]) == sorted(words[j]):
                anagrams.append(words[j])
                
        # If the number of anagrams is more than 1 and the sorted first anagram in the current set is not already in the list of anagram sets, then add the sorted anagram set to the list.               
        if len(anagrams) > 1 and sorted(anagrams) not in [sorted(s) for s in anagram_sets] and ''.join(sorted(anagrams[0])) not in existing_anagrams:
            anagram_sets.append(sorted(anagrams))
            existing_anagrams.add(''.join(sorted(anagrams[0])))  # Add the first anagram to existing_anagrams       
   
   
    anagram_sets.sort()
    
    # Write the anagrams to the output file
    with open(filename, 'w') as output:
        for anagram_set in sorted(anagram_sets):
            output.write(str(anagram_set)+ "\n")    
    print('Writing results...')
           
    #print out the set of anagrams
    for anagram_set in anagram_sets:
        print(anagram_set)     
  
  
    

except FileNotFoundError:
    print("Sorry, could not find file 'EnglishWords.txt'.")

