import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    return numpy.array(list(arr), float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
