# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import cmath
import math

data = complex(sys.stdin.read())

x = data.real
y = data.imag

r = math.sqrt((x**2 + y**2))
phi = cmath.phase(complex(x,y))

print(r)
print(phi)
