# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import product

s = [list(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]

A = s[0]
B = s[1]

z = list(product(A, B))

for tup in z:
    print(tup, end = ' ')
