# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.read().split('\n')

A = set(data[0].split())

res = True

for i in range(2, len(data), 1):
    s = set(data[i].split())
    
    for char in s:
        if char in A and len(A) > len(s):
            pass
        else:
            res = False

print(res)
