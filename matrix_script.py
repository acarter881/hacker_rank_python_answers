#!/bin/python3
import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ''    

for item in list(zip(*matrix)):
    for thing in item:
        decoded += thing

print(re.sub(pattern='([\w])([!@#\$%&\s]+)([\w])', repl=r'\1 \3', string=decoded))
