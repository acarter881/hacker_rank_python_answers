# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

my_list = []

for line in sys.stdin:
    line = line.rstrip()
    my_list.append(int(line))

print(pow(my_list[0], my_list[1]))
print(pow(my_list[0], my_list[1], my_list[2]))
