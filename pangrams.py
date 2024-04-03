#!/bin/python3

import math
import os
import random
import re
import sys
import string

def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    for letter in alphabet:
        if letter not in s:
            return 'not pangram'
    return 'pangram'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
