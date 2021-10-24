#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s = s.split()
    return s[0][0].upper() + s[0][1:] + ' ' + s[1][0].upper() + s[1][1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
