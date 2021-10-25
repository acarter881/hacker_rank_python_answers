# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import permutations

s = [line.rstrip().split() for line in sys.stdin.readlines()]

word = s[0][0]     # HACK
num = int(s[0][1]) # 2

z = list(permutations(word, num))
z = [''.join(tup) for tup in z]
z = sorted(z)

for thing in z:
    print(thing)
