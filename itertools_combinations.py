# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from itertools import combinations

s, k = sys.stdin.read().split()

big_l = []

for i in range(1, int(k) + 1, 1):
    combos = list(combinations(s, i))
    
    for combo in combos:
        big_l.append(''.join(combo))
        
big_l = sorted(sorted([''.join(sorted(thing)) for thing in big_l]), key=len)

for l in big_l:
    print(l)
