#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    time_divided = []
    for i in s:
        time_divided.append(i)
    
    new_string = ''
    correct_hour = 0
    new_string += time_divided[0]
    new_string += time_divided[1]
    if time_divided[8] == 'P':
        if new_string == '12':
            new_string = '00'
        new_string = int(new_string)
        correct_hour = new_string + 12
        new_string = str(correct_hour)
    elif time_divided[8] == 'A' and new_string == '12':
        new_string = '00'
    else:
        new_string = str(new_string)
    
    time_divided[0] = new_string[0]
    time_divided[1] = new_string[1]
    time_divided[8] = ''
    time_divided[9] = ''

    new_string = ''
    for n in time_divided:
        new_string += n
    return new_string
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
