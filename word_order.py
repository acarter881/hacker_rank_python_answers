# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n = int(input())

c = Counter()

for i in range(n): c[input()] += 1
    
print(len(c))

for v in c.values(): print(v, end=' ')
