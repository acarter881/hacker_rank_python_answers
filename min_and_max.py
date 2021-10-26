import numpy
import sys

print(numpy.max(numpy.min([list(map(int, line.split())) for line in sys.stdin.readlines()][1:], axis=1)))
