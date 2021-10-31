# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.read().split('\n')[1:]

s1 = list()
s2 = list()

for i in range(len(data)):
    if i % 2 == 0: pass
    elif len(s1) == 0: s1.append(data[i].split())
    else:
        s2.append(data[i].split())
        
        if False not in [char in s2[0] for char in s1[0]]: print(True)
        else: print(False)
        
        s1 = list()
        s2 = list()     
