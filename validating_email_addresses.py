# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

items = sys.stdin.read().split('\n')

email_reg_ex = re.compile(r'^[a-zA-Z][a-zA-Z0-9\-\._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$')

for i in range(int(items[0])):
    if re.search(email_reg_ex, items[i+1].split()[1][1:-1]): print(items[i+1])
