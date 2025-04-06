# Program for manipulating 2-dimensional arrays of size 4x4.
# Makanaka Mangwanda
# 13 April 2024

def create_grid(grid):
   for i in range (0,4):
      row = [ ]#empty list for each row
      for r in range(0,4):
         row.append(0)#append 0 to each column of a row
      grid.append(row)


def print_grid(grid):
   # print out a 4x4 grid in 5-width columns within a box"""
   print('+--------------------+')
   for i in range(4):
      print('|' ,end="")
      for r in range(4):
         if grid[i][r] != 0:
            print('{0:<5}'.format(grid[i][r]),end="")
         else:
            print(' '*5, end="")
      print('|')
   print('+--------------------+')

def check_lost( grid):
   #return True if there are no 0 values and there are no adjacent values that are equal; otherwise False 
   for i in range(4):
      for r in range(3):   
         if grid[i][r] == 0 or grid[i][r]==grid[i][r+1]:
            return False
      
   return True
     
def check_won(grid):
   #return True if a value>=32 is found in the grid; otherwise False
   for i in range(4): 
      for r in range(4):
         if grid[i][r] >= 32:
            return True
         
   return False   
  
  
def copy_grid (grid):
   #return a copy of the given grid
   copy = [ ]
   for i in range (4):
      row = [ ]# new row for each iteration of i
      for r in range (4):
         row.append(grid[i][r])
      copy.append(row)#append the row list to the copy list
      
   return copy 
  
  
def grid_equal (grid1, grid2):
   #check if 2 grids are equal - return boolean value
   for i in range(4): 
      for j in range(4):
         if grid1[i][j] != grid2[i][j]:
            return False
   return True
      
      
   
   