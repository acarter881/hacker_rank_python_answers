# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

my_list = [int(line.rstrip()) for line in sys.stdin.readlines()]

print((my_list[0] ** my_list[1]) + (my_list[2] ** my_list[3]))
