# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

print(len(set([line.rstrip() for line in sys.stdin.readlines()[1:]])))
