# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

p_phone_numbers = [line.split('\n')[0] for line in sys.stdin.readlines()]

phone_reg_ex = re.compile(r'^[7-9]\d{9}$')

for i in range(int(p_phone_numbers[0])):
    if re.search(phone_reg_ex, p_phone_numbers[i+1]): print('YES')
    else: print('NO')
