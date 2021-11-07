# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

N, M = list(map(int, sys.stdin.read().split())) # 7 and 21, respectively

s1 = '.|.'
s2 = 'WELCOME'

for i in range(N // 2):
    print((s1*((i*2)+1)).center(M,'-'))
    
print(s2.center(M,'-'))

for i in range(N // 2, 0, -1):
    print((s1*((i*2)-1)).center(M,'-')) 
