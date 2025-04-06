def main():
   n = int(input('Enter a number:'))
   sum = 0
   for i in range(11,n+1):
      if i % 2 != 0:
         sum += i
         
   print(sum)
            
        
    
    
    
if __name__ == '__main__':main()
