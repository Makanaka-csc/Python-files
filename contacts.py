# Programs that use basic data structures such lists, searching and sorting as well as file IO to manipulate data.
# Makanaka Mangwanda
# 06 May 2024

def path_exists(file_path):
    try:
        open(file_path)
        return True
    except FileNotFoundError:
        return False
    
    
  
def add_contact(file_path, name,phone,email):
    #if contact already exists print 'contact already exists'
    contacts = read_contacts(file_path)
    for contact in contacts:
        if contact[0] == name and contact[1] == phone and contact[2] == email:
            return'Contact already exists.'
            
            
    
    #if the contact does not exist ,add it   
    contact =[]
    file = open( file_path,'a')
    contact.append(name)
    contact.append(phone)
    contact.append(email)
    file.close()
    print(' Contact added successfully.')
 

 
def custom_sort(contacts):
    # Extract names from the contacts list
    names = [contact[0] for contact in contacts]

    # Sort the names alphabetically
    names.sort()

    # Create a sorted list of contacts based on the sorted names
    sorted_contacts = []
    for name in names:
        for contact in contacts:
            if contact[0] == name:
                sorted_contacts.append(contact)
                break  # Exit inner loop once contact is found for the name

    return sorted_contacts
       
    

def search_contact(file_path, query):
    #searches for contacts in the contacts list based on the query supplied by the user
   
    results =[]
    query = query.lower()
    #if the queryy is a * then output the whole list contact
    if query == '*':
        return list_contacts(file_path)
      
        
        
    file = open(file_path,'r')
    for line in file:
        #Split the line into name, phone, and email using commas as separator
        try:
            name, phone, email = line.strip().split(',')
        except ValueError:
            # Skip lines that don't contain the expected number of elements
            continue
        
        #make each first letter capital in the name and surname
        name = name.title()
        #check if query matches with the name
        if query in name.lower():
            results.append((name, phone, email))
        
    #close the file       
    file.close()
    
    if results:
        print('Found contact(s):')
        print('============================================================')
        print('| {:<20} | {:<15} | {:<25} |'.format('Name', 'Phone', 'Email'))
        print('============================================================')

        for contact in results:
            print('| {:<20} | {:<15} | {:<25} |'.format(contact[0], contact[1], contact[2]))
            print('------------------------------------------------------------')

    else:
        print('No contact found.')
        
    return ''
        
    


    
                        
                        
                        
def read_contacts(file_path):
    # function that reads contacts from the cntacts file
    
    contacts =[]
    file = open(file_path,'r')
    for line in file:
        #split each line using commas as a separator
        try:
            name,phone,email =line.strip().split(',')
        except ValueError:
            #skip lines that don't contain the number of elements
            continue
        
        # a list of lists
        contacts.append([name,phone,email])
        
    return contacts

def list_contacts(file_path):
    # function lists all contacts sorted alphabetically by name
    
    contacts = read_contacts(file_path)
    sort_contacts = custom_sort(contacts)
    
    print('\nFound contact(s):')
    print('============================================================')
    print('| {:<20} | {:<15} | {:<25} |'.format('Name', 'Phone', 'Email'))
    print('============================================================')
   
    
    for contact in sort_contacts:
        print('| {:<20} | {:<15} | {:<25} |'.format(contact[0],contact[1],contact[2]))
        print('------------------------------------------------------------')
    
    
    
def wildcard(query,text):
    length_of_query = len(query) 
    length_of_text = len(text)
    
    if length_of_text == length_of_query:
        return True
    else:
        return False
    
    if query[0] == text[0] or query[0] == '*':
            #recursively slice the query and text
            return wildcard(query[1:], text[1:])
    return False



def main():
    contacts = input('Enter the name for the contacts file:\n')
    
    file_path = contacts + '.txt'
    
    # If the file does not exist, create it
    if not path_exists(file_path):
        open(file_path, 'w').close()
        print('Contacts file \'' + file_path + '\' created.')
  
        
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. List Contacts")
        print("4. Exit")
                
        choice = input('Enter your choice:')
        
        if choice == '1':
            name = input(' Enter name:')
            phone = input(' Enter phone number:')
            email = input(' Enter email:')
            add_contact(file_path, name,phone,email)
            
        elif  choice == '2':
            search = input(' Enter first name, last name, phone number, or email to search:\n')
            
            results = search_contact(file_path, search)
           
            
        elif choice == '3':
            # List all the contacts
            list_contacts(file_path)
        
        elif choice == '4':
             # Exit the program
            print(" Exiting program.")
            break
        
        else:
            # Invalid choice
            print("Invalid choice. Please enter a number between 1 and 4.")
            
if __name__ == '__main__' : main()
            
            
            
            
            
    
    
    

    
