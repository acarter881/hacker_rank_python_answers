# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()

grouping = [list(g) for k, g in groupby(s)] # [['1'], ['2', '2', '2'], ['3'], ['1', '1']]

for thing in grouping:
    print(tuple((len(thing), int(thing[0]))), end=' ')
