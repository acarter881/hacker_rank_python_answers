# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

my_list = []

for line in sys.stdin.readlines()[1:]:
    line = line.strip()
    my_list.append(map(float, line.split()))
    
s = list(zip(*my_list)) # unpacking

for avg in [sum(s[i]) / len(s[i]) for i in range(len(s))]:
    print(avg)
