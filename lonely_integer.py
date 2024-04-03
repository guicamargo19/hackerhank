#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    
    
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] == a[j+1]:
                a[j], a[j+1] = 0, 0
    
    for number in a:
        if number != 0:
            return number
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
