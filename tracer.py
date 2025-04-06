# Program that will insert a trace statement at the beginning of each function definition.
# Makanaka Mangwanda
# 04 May 2024

print('*****Program Trace Utility*****')
sen = input ('Enter the name of the program file:')

File= open(sen, 'r')
File2 = File.readlines()
File.close()
File = open(sen, 'w')

print(File2)
if File2[0] != ' """DEBUG"""\n':
    File2.insert(0, '"""DEBUG"""\n')
    
    for i in range(1, len(File2)):
        
        if 'def' in File2[i]:
            string = File2[i][4:File2[i].find("(")]
            File2.insert(File2.index(File2[i])+1, '    """DEBUG"""'+ ";print('"+ string+"')\n")
    File.writelines(File2)
    print('Inserting...Done')
    
else:
    for line in File2:
        if line.strip().startswith('"""DEBUG"""'):
            File2.remove(line)
        File.writelines(File2)
        print('Removing...Done')
        
    
print(File2)
File.close()
            
            
