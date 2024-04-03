#!/bin/python3

import math
import os
import random
import re
import sys

def flippingBits(n):
    binary_str = bin(n)[2:]
    binary_32_bit = binary_str.zfill(32)
    
    new_binary_32_bit = ''
    for number in binary_32_bit:
        if number == '0':
            new_binary_32_bit += '1'
        elif number == '1':
            new_binary_32_bit += '0'

    return int(new_binary_32_bit, 2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
