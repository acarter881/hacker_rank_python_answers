# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import Counter

s = [list(map(int, line.rstrip().split())) for line in sys.stdin.readlines()]

my_list = Counter(s[1])

total = 0

for thing in s[3:]:
    if my_list[thing[0]]:
        my_list[thing[0]] -= 1
        total += thing[1]
        
print(total)
