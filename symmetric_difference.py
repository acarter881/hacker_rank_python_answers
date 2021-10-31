# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

lines = sys.stdin.read().split('\n')

s1 = set(map(int, lines[1].split()))

s2 = set(map(int, lines[3].split()))

for char in sorted(s1.symmetric_difference(s2)): print(char)
