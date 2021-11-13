# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import deque

data = sys.stdin.read().split('\n')[1:]

blocks = [deque(map(int, data[i].split())) for i in range(len(data)) if i % 2 == 1]

y = list()

for i in range(len(blocks)):
    res = 'Yes'
    previous_pop = None
    
    for _ in range(len(blocks[i])):
        l = blocks[i][0]
        r = blocks[i][-1]
        
        if l > r: current_pop = blocks[i].popleft()
        else: current_pop = blocks[i].pop()
            
        if previous_pop == None: previous_pop = current_pop  
        elif current_pop > previous_pop:
            res = 'No'
            break
        elif current_pop <= previous_pop: previous_pop = current_pop
        
    y.append(res)

print(*y, sep='\n')
