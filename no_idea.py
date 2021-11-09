# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

n, m = list(map(int, input().split())) 

array = list(map(int, input().split()))
array_to_dict = Counter(array)

A = list(map(int, input().split()))
B = list(map(int, input().split()))

output = 0

for num in A: output += array_to_dict[num]
for num in B: output -= array_to_dict[num]

print(output)
