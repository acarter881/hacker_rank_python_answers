import numpy as np

n, m = map(int, input().split())

a = np.array([input().split() for i in range(n)], dtype=int)
b = np.array([input().split() for i in range(n)], dtype=int)

print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))        
