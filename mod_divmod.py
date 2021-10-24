# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

s = [int(line.rstrip()) for line in sys.stdin.readlines()]

print(s[0] // s[1])           # Integer division
print(s[0] % s[1])            # Modulo
print(divmod(s[0], s[1]))     # divmod
