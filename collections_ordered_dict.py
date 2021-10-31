# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
from collections import OrderedDict

ordered_dictionary = OrderedDict()

for item in sys.stdin.read().split('\n')[1:]:
    num = item.split()[-1]
    
    name = ' '.join(item.split()[:-1]).strip()
    
    if not ordered_dictionary.get(name):
        ordered_dictionary.setdefault(name, int(num))
    else:
        ordered_dictionary[name] += int(num)

for k, v in ordered_dictionary.items(): print(k, v)
