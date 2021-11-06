import numpy
import sys
print(numpy.reshape(list(map(int, sys.stdin.read().split(' '))), (3,3)))
