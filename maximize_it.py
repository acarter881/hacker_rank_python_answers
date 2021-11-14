# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

K, M = map(int, input().split())

s = list()

for _ in range(K):
    s.append(map(lambda x: x**2, map(int, input().split()[1:])))
    
print(max([sum(i) % M for i in product(*s)]))
