#!/bin/python3

import math
import os
import random
import re
import sys

def isPalindrome(arr):
    start = 0
    end = len(arr)-1

    
    while start <= end:
        if arr[start] != arr[end]:
            return False
        else:
            start = start +1
            end = end -1 
    return True

def get_nro_not_palindrome_cases(arr):
    np_cases =0 
    start = 0
    end = len(arr)-1
    while start <= end:
        if arr[start] != arr[end]:
            np_cases = np_cases+1
        start = start +1
        end = end - 1
    return np_cases
    

def highestValuePalindrome(s, n, k):
    arr = list(s)

    np_cases = get_nro_not_palindrome_cases(arr)

    start = 0
    end = len(arr)-1
    while start <= end :
        if arr[start] != arr[end]:
            if k> np_cases and k>=2 and arr[start]!= '9' and arr[end]!='9' :
                arr[start]  =  arr[end] = '9'
                k=k-2
                np_cases = np_cases -1
            elif k>=1:
                arr[start] = arr[end] = str(max( arr[start], arr[end]))
                k=k-1
                np_cases = np_cases -1
                
        else:
            if k> np_cases and k>=2 and arr[start]!= '9' and arr[end]!='9':
                arr[start] = arr[end] = '9'
                k=k-2
        start = start +1
        end = end - 1 

    if isPalindrome(arr):
        if k>0 and len(arr)%2 ==1 and arr[int(len(arr)/2)]!='9' :
            arr[int(len(arr)/2)]='9'
        return ''.join(arr)
    else:
        return '-1'

#https://www.hackerrank.com/challenges/richie-rich/problem
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
