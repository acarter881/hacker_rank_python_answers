# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

for case in sys.stdin.read().split('\n')[1:]:
    try: print(int(case[0]) // int(case[-1]))
    except Exception as e: print(f'Error Code: ' + str(e))
