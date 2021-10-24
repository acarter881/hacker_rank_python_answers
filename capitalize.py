#!/bin/python3
import math
import os
import random
import re
import sys
import re

def to_upper(s):
    return s.group(1) + s.group(2).upper()

def solve(s):
    return re.sub('(^|\s)(\S)', to_upper, s)
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
