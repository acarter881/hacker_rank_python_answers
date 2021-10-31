# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

s = sys.stdin.read() # The string to read and iterate over

my_regEx = re.compile(pattern=r'[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]?([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]')

if re.findall(pattern=my_regEx, string=s):
    for item in re.findall(pattern=my_regEx, string=s):
        print(item)
else:
    print('-1')
