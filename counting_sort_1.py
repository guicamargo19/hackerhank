#!/bin/python3

import math
import os
import random
import re
import sys
    
def countingSort(arr):
    size = len(arr)
    resultado = [0] * 100
    
    i = size - 1
    while i >= 0:
        resultado[arr[i]] += 1
        i -= 1

    print(len(resultado))
    return resultado
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
