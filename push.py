# Program of merging functions that merge adjacent equal values and eliminate gaps 
# Makanaka Mangwanda
# 20 April 2024



def push_up(grid):
    #merge the values upwards
    for i in range(4):
        merged = False
        for r in range(1,4):
            if grid[i][r] != 0:
                c = r
                # shift non-zero values upwards
                while c > 0 and (grid[c-1][i] == 0 or grid[c-1][i] == grid[c][i]):
                    grid[c-1][i] = grid[c][i]
                    grid[c][i] = 0
                    c = c -1
                    # merge adjacent equal values
                if c > 0 and grid [c-1][i] == grid [c][i]and not merged :
                    grid[c-1][i] *= 2 
                    grid [c][i] = 0
                    merged = True 
                    
def push_down(grid):
    #Merge grid values downwards
    for j in range(4):  # Iterate over columns
            merged = False
            for i in range(2, -1, -1):  # Iterate over rows in reverse
                if grid[i][j] != 0:
                    row = i
                    # shift non-zero values downwards
                    while row < 3 and grid[row + 1][j] == 0:
                        grid[row + 1][j] = grid[row][j]
                        grid[row][j] = 0
                        row += 1
                        # Merge adjacent values that are equal
                    if row < 3 and grid[row + 1][j] == grid[row][j] and not merged:
                        grid[row + 1][j] *= 2
                        grid[row][j] = 0
                        merged = True    
                    
def push_left(grid):
    #Merge grid values to the left
    for i in range(4):  # Iterate over rows
        merged = False
        for r in range(1, 4):  # Iterate over columns
            if grid[i][r] != 0:
                col1 = r
                # shift non-zero values to the left
                while col1 > 0 and grid[i][col1 - 1] == 0:
                    grid[i][col1 - 1] = grid[i][col1]
                    grid[i][col1] = 0
                    col1 -= 1
                    # merging adjacent equal values
                    if col1 > 0 and grid[i][col1 - 1] == grid[i][col1] and not merged:
                        grid[i][col1 - 1] *= 2
                        grid[i][col1] = 0
                        merged = True
                    elif col1 > 0 and grid[i][col1 - 1] != 0 and grid[i][col1 - 1] != grid[i][col1]:
                        col1 -= 1    
                     
     


def push_right(grid):
    #Merge grid values right
    for i in range(4):
        merged = False
        for r in range(1,4):
            if grid[i][r] != 0:
                c = r
                # shift non-zero values to the right
                while c > 0 and grid[c-1][i] == 0:
                    grid[c+1][i] = grid[c][i]
                    grid[c][i] = 0
                    c = c -1
                    # merge adjacent equal values
                if c > 0 and grid [c-1][i] == grid [c][i] and merged == False:
                    grid[c-1][i] *= 2 
                    grid [c][i] = 0
                    merged = True     
      
      
   
