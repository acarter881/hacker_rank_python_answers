# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import calendar

date = [list(map(int, line.split())) for line in sys.stdin.readlines()][0]

day_num = calendar.weekday(year=date[2], month=date[0], day=date[1])

print(dict(zip(range(7), list(map(str.upper, calendar.day_name))))[day_num])
