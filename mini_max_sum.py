#!/bin/python3

import math
import os
import random
import re
import sys

def ordering(arr):
    for n in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
            

def miniMaxSum(arr):
    total_max = 0
    for n in arr[1:5]:
        total_max = total_max + n
    
    total_min = 0
    for n in arr[:4]:
        total_min = total_min + n
    
    print(total_min, total_max)

if __name__ == '__main__':
    
    arr = list(map(int, input().rstrip().split()))
    arr = ordering(arr)
    miniMaxSum(arr)
