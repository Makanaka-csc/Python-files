#Program that counts the number of uppercase characters in a given string and returns the total number of uppercase characters as an integer.
# Makanaka Mangwanda
# 26 April 2024
    
def count_uppercase(s):
    count = 0
    for letter in s:
        if letter.isupper():
            count += 1        
    return count
         

def find_uppercase(s):

    upper_1 = [ ]
    for letter in s:
        if letter.isupper():
            upper_1.append(letter)        
    return upper_1
    
            

def main():
    s = input("Enter a string:\n")
    
    # Count uppercase characters
    uppercase_count = count_uppercase(s)
    print(f"The number of uppercase characters in the string is: {uppercase_count}.")
    
    # Find uppercase characters
    uppercase_list = find_uppercase(s)
    
    # Print uppercase characters as a comma-separated list
    print("List of uppercase characters:")
    if len(s) == 0 or uppercase_count == 0:
        print("[]")
    else:
        print(", ".join(uppercase_list))


if __name__ == "__main__":
    main()

    