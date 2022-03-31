import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def build_output(result_array):
    result=[]
    for r_array in result_array:
        result.append(''.join(r_array))
    return result

def bomberMan(n, grid):
    max_cols = len(grid[0])

    if n == 1:
        return grid


    first_explotion = []
    for i in range(0,len(grid)):
        first_explotion.append(['O'] * max_cols)
   
    if n%2 == 0:
        return build_output(first_explotion)
    
    for i in range(0,len(grid)):
            row= list(grid[i])
            for j in range(0,len(row)):
                if row[j]=='O':
                    up = max(i-1,0)
                    down = min(i+1,len(grid)-1)
                    left = max(j-1,0)
                    rigth = min(j+1,len(row)-1)
                    first_explotion[i][j]='.'
                    first_explotion[up][j]='.'
                    first_explotion[down][j]='.'
                    first_explotion[i][left]='.'
                    first_explotion[i][rigth]='.'
        
    if n%4 == 3 or n == 3:
        return build_output(first_explotion)
        
  
    if n%4==1 or n == 1:
        temporal = first_explotion.copy()

        second_explotion=[]
        for i in range(0,len(grid)):
            second_explotion.append(['O'] * max_cols)
        
        for i in range(0,len(grid)):
            for j in range(0,len(row)):
                if temporal[i][j]=='O':
                    up = max(i-1,0)
                    down = min(i+1,len(grid)-1)
                    left = max(j-1,0)
                    rigth = min(j+1,len(row)-1)
                    second_explotion[i][j]='.'
                    second_explotion[up][j]='.'
                    second_explotion[down][j]='.'
                    second_explotion[i][left]='.'
                    second_explotion[i][rigth]='.'

        return build_output(second_explotion)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
