# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

s = sys.stdin.read()

match = False

for i in range(len(s)):
    if s[i].isalnum():
        try:
            if s[i] == s[i-1]:
                match = True
                print(s[i])
                break
        except Exception as e:
            pass

if match == False: print(-1)             
