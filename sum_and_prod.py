import numpy
import sys

print(numpy.prod(numpy.sum([list(map(int, line.split())) for line in sys.stdin.readlines()][1:], axis=0)))
