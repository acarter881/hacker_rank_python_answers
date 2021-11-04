# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

data = sys.stdin.read().split('\n')[1:]

float_regEx = re.compile(r'^[\+\-\.]?[0-9]*\.?[0-9]+$')

for i in range(len(data)):
    if data[i].count('.') != 1: print(False)
    elif not re.search(pattern=float_regEx, string=data[i]): print(False)
    else: print(True)
