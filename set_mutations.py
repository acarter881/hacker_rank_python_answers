# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.read().split('\n')

A = set(data[1].split())

for i in range(3, len(data), 1):
    thing = data[i].split()
    
    if thing[0][0].isalnum():
        command = data[i-1].split()[0]
        
        if command == 'intersection_update':
            A.intersection_update(set(thing))
        elif command == 'update':
            A.update(set(thing))
        elif command == 'symmetric_difference_update':
            A.symmetric_difference_update(set(thing))
        elif command == 'difference_update':
            A.difference_update(set(thing))
            
print(sum(map(int, A)))
