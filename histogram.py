# Program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT.
# Makanaka Mangwanda
# 13 April 2024

# counter for each cartegory
def count(marks):
    fail= 0
    third= 0
    lower_2nd = 0
    upper_2nd = 0
    first = 0
  
    
    #iteration of marks
    for mark in marks:
        if mark < 50:
            fail+= 1
        if 50 <= mark <60:
            third+=1
        if 60 <= mark < 70:
            lower_2nd +=1
        if 70 <= mark < 75:
            upper_2nd +=1
        if mark >= 75:
            first += 1
            
    return first,upper_2nd,lower_2nd,third,fail

# labels on the histogram
def histogram(labels):
    lab = ['1 ','2+','2-','3 ','F ']
    
    # make the histogram
    for i in range (len(labels)):
        print(lab[i]+ '|'+'X'* labels[i])

def main():
    # marks inputed from the user
    marks_1 = input('Enter a space-separated list of marks:\n')
    marks = (map(int,marks_1.split()))

    
    labels = count(marks)
    histogram(labels)
    
        
if __name__ == "__main__":
    main()    

    
    
    