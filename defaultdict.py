# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import defaultdict

data = sys.stdin.read().split('\n')

n, m = int(data[0].split()[0]), int(data[0].split()[1])

d = defaultdict(list)

for i in range(1, n + 1, 1): d[data[i]].append(i)

for i in range(n + 1, len(data), 1):
    if d[data[i]]: print(''.join(str(d[data[i]]).strip('[]').split(',')))
    else: print('-1')
