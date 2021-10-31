import numpy
import sys

data = sys.stdin.read().split('\n')

N, M, P = data[0][0], data[0][2], data[0][4]

array_1 = list()
array_2 = list()

for i in range(1, int(M) + 2, 1): array_1.append(list(map(int, data[i].split())))

for i in range(int(M) + 2, len(data), 1): array_2.append(list(map(int, data[i].split())))

print(numpy.concatenate((array_1, array_2), axis=0))
