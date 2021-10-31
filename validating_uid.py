# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

UIDS = [line.strip('\n') for line in sys.stdin.readlines()]

for i in range(int(UIDS[0])):
    if len(UIDS[i+1]) != 10:                                        
        print('Invalid') # Must be 10 characters
    elif len(set(UIDS[i+1])) != len(UIDS[i+1]):                     
        print('Invalid') # Characters must not repeat
    elif [char.isdigit() for char in UIDS[i+1]].count(True) < 3:    
        print('Invalid') # At least 3 characters are digits
    elif [(char.isupper() and char.isalpha()) for char in UIDS[i+1]].count(True) < 2:
        print('Invalid') # At least 2 uppercase English alphabet characters
    elif False in [char.isalnum() for char in UIDS[i+1]]:
        print('Invalid') # All the characters must be alphanumeric
    else:
        print('Valid')
