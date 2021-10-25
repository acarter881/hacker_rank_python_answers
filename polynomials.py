import numpy
import sys

s = [list(map(float, line.rstrip().split())) for line in sys.stdin.readlines()]

A = s[0]
B = s[1]

print(float((numpy.polyval(A, B))))
