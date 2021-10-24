# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

real_lines = []

for line in sys.stdin:
    line = line.rstrip()
    real_lines.append(line)

real_lines = real_lines[1:]    
    
for line in real_lines:
    try:
        re.compile(line)
        print('True')
    except re.error:
        print('False')  
