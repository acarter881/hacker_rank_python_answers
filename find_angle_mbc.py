# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *

AB = int(input())
BC = int(input())

print("%.0f" % degrees(atan2(float(AB), float(BC))) + u'\N{DEGREE SIGN}')
