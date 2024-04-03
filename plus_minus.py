#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    negatives = []
    positives = []
    zero = []
    length = len(arr)
    for item in arr:
        if item < 0:
            negatives.append(item)
        elif item == 0:
            zero.append(item)
        else:
            positives.append(item)
    
    format_positive = len(negatives) / length
    format_negative = len(positives) / length
    format_zero = len(zero) / length
    print("{:.6f}".format(format_negative))
    print("{:.6f}".format(format_positive))
    print("{:.6f}".format(format_zero))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
