# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools

N = int(input())
letters = input().split()
K = int(input())

combinations = list(itertools.combinations(range(1, N + 1, 1), K))

numerator = 0
denominator = len(combinations)

for tup in combinations:
    match = False
    
    for num in tup:
        if letters[num - 1] == 'a': match = True
    
    if match == True: numerator += 1
        
output = (numerator / denominator)

print(output)      
