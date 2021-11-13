from collections import Counter
for thing in Counter(sorted(input())).most_common(3): print(thing[0] + ' ' + str(thing[1]))
