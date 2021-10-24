# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

s = [line.rstrip() for line in sys.stdin.readlines()]

print(int(s[0]) // int(s[1]))           # Integer division
print(int(s[0]) % int(s[1]))            # Modulo
print(divmod(int(s[0]), int(s[1])))     # divmod
