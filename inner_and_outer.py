import numpy
import sys

a, b = sys.stdin.read().split('\n')

a = list(map(int, a.split()))
b = list(map(int, b.split()))

A = numpy.array(a)
B = numpy.array(b)

print(numpy.inner(A,B))
print(numpy.outer(A,B))
