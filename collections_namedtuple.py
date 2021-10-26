# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import namedtuple

z = [line.split() for line in sys.stdin.readlines()][1:]
the_index = z[0].index('MARKS')

total = 0

for line in z[1:]: total += int(line[the_index])
    
print(total/(len(z)-1))
