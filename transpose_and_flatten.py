import numpy
import sys

data = sys.stdin.read().split('\n')[1:]

data = [','.join(item.split(' ')) for item in data]

data = [item.split(',') for item in data]

data = [list(map(int, item)) for item in data]

my_array = numpy.array(data)

print(numpy.transpose(my_array))
print(my_array.flatten())
