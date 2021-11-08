# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

s = input()

series = '[a-z]', '[A-Z]','[13579]', '[02468]'

print(''.join(map(lambda x: ''.join(sorted(re.findall(x, s))),series)))
