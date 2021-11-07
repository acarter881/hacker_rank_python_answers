# Enter your code here. Read input from STDIN. Print output to STDOUT
K = int(input())
room_list = list(map(int, input().split()))

the_dict = dict()

for room in room_list:
    the_dict.setdefault(room, 1)
    the_dict[room] += 1

min_value = min(the_dict.values())

for k, v in the_dict.items():
    if min_value == v: print(k)
