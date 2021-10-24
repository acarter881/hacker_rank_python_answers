# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

my_list = []

for index, line in enumerate(sys.stdin.read().split('\n')):
    if index % 2 != 0:
        my_list.append(' '.join(([value for value in line.split() if value != ' '])))

my_list = my_list[0] + ' ' + my_list[1]   

s = set(my_list.split())
        
print(len(s))
