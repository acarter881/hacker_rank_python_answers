# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

items = sys.stdin.read().split('\n')

n = int(items[0])

methods = items[1:]

d = deque()

for item in methods:
    try:
        if item.split()[1]:
            num = int(item.split()[1])        
    except Exception as e:
        pass
    
    name = item.split()[0]
    
    if name == 'append':
        d.append(num)
    elif name == 'appendleft':
        d.appendleft(num)
    elif name == 'pop':
        d.pop()
    elif name == 'popleft':
        d.popleft()
        
for item in d:
    print(item, end=' ')
