# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

my_list = []

for index, line in enumerate(sys.stdin.read().split('\n')):
    if index % 2 != 0:
        my_list.append(([value for value in line.split()]))     
           
l1 = set(my_list[0])
l2 = set(my_list[1]) 

print(len(l1.difference(l2)))
