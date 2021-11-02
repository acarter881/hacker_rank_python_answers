# TIP: Use Python3 instead of Pypy3
import sys

n = int(input())
s = set(map(int, input().split()))

data = sys.stdin.read().split('\n')

for i in range(1, len(data), 1):
    if data[i].split()[0] == 'pop': s.pop()
    elif data[i].split()[0] == 'remove': s.remove(int(data[i].split()[1]))
    elif data[i].split()[0] == 'discard': s.discard(int(data[i].split()[1]))

print(sum(s))
