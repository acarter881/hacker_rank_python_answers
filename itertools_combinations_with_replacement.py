import sys
from itertools import combinations_with_replacement

s, k = sys.stdin.read().split()

big_l = []

for i in range(1, int(k) + 1, 1):
    combos = list(combinations_with_replacement(s, int(k)))
    
    for combo in combos:
        big_l.append(''.join(combo))
        
big_l = sorted(sorted([''.join(sorted(thing)) for thing in big_l]), key=len)

big_l = sorted(list(set(big_l)))

for l in big_l:
    print(l)
