import numpy
import sys
numpy.set_printoptions(legacy='1.13')

N, M = list(map(int, sys.stdin.read().split()))

print(numpy.eye(N, M))
