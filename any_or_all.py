# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

data = sys.stdin.read().split('\n')[1] # The space separated integers

if '-' in data: 
    print(False)           # Check if there's a negative sign
else:
    match = False

    for num in data.split():
        if any([len(num) == 1, num == num[::-1]]):
            match = True

    print(match)
