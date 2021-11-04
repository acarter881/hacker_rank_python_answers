# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

data = sys.stdin.read().split('\n')[1:]

hex_regEx = re.compile(r':?\s?(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})\)?[;,]')

for line in data:
    if re.search(pattern=hex_regEx, string=line):
        print(*re.findall(pattern=hex_regEx, string=line), sep='\n')
