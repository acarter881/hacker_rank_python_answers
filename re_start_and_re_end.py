# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

s, k = sys.stdin.read().split('\n')

match = False

for i in range(len(s)):
    if s[i:i+len(k)] == k:
        print((i, i + len(k) - 1))
        match = True
        
if match is False: print((-1, -1))
