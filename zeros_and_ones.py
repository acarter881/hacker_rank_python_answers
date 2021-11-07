import numpy
import sys

A = tuple(map(int, sys.stdin.read().split()))

print(numpy.zeros(A, dtype=numpy.int))
print(numpy.ones(A, dtype=numpy.int))
