#!/bin/python3

import math
import os
import random
import re
import sys


def icecreamParlor(m, arr):
    d = []
    
    for idx, el in enumerate(arr):
        if el < m:
            t = (el, idx + 1)
            d.append(t)

    new_arr = d
    for i in range(len(new_arr)):
        for j in range(i+1, len(new_arr)):
            if new_arr[i][0] + new_arr[j][0] == m:
                sol = [new_arr[i][1], new_arr[j][1]]
                sol.sort()
                return sol

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()